from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
CLEAN_CSV = ROOT / "customer_churn_dataset_clean.csv"
CHURN_ONLY_CSV = ROOT / "customer_churn_only.csv"
OUTPUT_ROOT = ROOT / "phase2_outputs"

OVERALL_RAW_FEATURES = [
    "tenure",
    "contract",
    "customer_satisfaction",
    "num_complaints",
    "num_service_calls",
    "late_payments",
    "monthlycharges",
    "num_services",
    "has_tech_support",
]

CHURN_ONLY_RAW_FEATURES = [
    "annual_income",
    "education",
    "contract",
    "paperless_billing",
    "num_complaints",
    "num_service_calls",
    "late_payments",
    "monthlycharges",
]

OVERALL_MODEL_FEATURES = [
    "tenure_group",
    "contract",
    "customer_satisfaction_group",
    "num_complaints_group",
    "num_service_calls_group",
    "late_payments_group",
    "monthlycharges_group",
    "num_services_group",
    "has_tech_support",
]

CHURN_ONLY_SUPPORT_FEATURES = [
    "annual_income_group",
    "education_group",
    "contract",
    "paperless_billing_flag",
    "num_complaints_group",
    "num_service_calls_group",
    "late_payments_group",
    "monthlycharges_group",
]


@dataclass
class SplitSummary:
    split: str
    rows: int
    non_churn_0: int
    churn_1: int
    churn_pct: float


def ensure_columns(df: pd.DataFrame, columns: Iterable[str], context: str) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{context} is missing columns: {missing}")


def resolve_input_csv(path_like: str, filename: str) -> Path:
    candidate = Path(path_like)
    if candidate.exists():
        return candidate

    search_roots = [ROOT, Path("/kaggle/input")]
    for search_root in search_roots:
        if not search_root.exists():
            continue
        matches = sorted(search_root.rglob(filename))
        if matches:
            return matches[0]

    raise FileNotFoundError(
        f"Could not find {filename}. Checked explicit path {candidate} and recursive search roots: "
        + ", ".join(str(root) for root in search_roots)
    )


def add_feature_groups(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    out["annual_income_group"] = pd.cut(
        out["annual_income"],
        bins=[-np.inf, 30_000, 60_000, 90_000, np.inf],
        labels=["income_lt_30k", "income_30_60k", "income_60_90k", "income_gt_90k"],
        right=False,
    ).astype("string")

    out["education_group"] = np.where(
        out["education"].isin(["master", "phd"]),
        "graduate",
        "non_graduate",
    )

    if "tenure" in out.columns:
        out["tenure_group"] = pd.cut(
            out["tenure"],
            bins=[0, 6, 15, 31, np.inf],
            labels=["tenure_1_6", "tenure_7_15", "tenure_16_31", "tenure_32_plus"],
            right=True,
        ).astype("string")

    if "customer_satisfaction" in out.columns:
        out["customer_satisfaction_group"] = pd.cut(
            out["customer_satisfaction"],
            bins=[0, 3, 6, 9],
            labels=["satisfaction_1_3", "satisfaction_4_6", "satisfaction_7_9"],
            right=True,
        ).astype("string")

    out["num_complaints_group"] = pd.cut(
        out["num_complaints"],
        bins=[-np.inf, 1, np.inf],
        labels=["complaints_le_1", "complaints_gt_1"],
        right=True,
    ).astype("string")

    out["num_service_calls_group"] = pd.cut(
        out["num_service_calls"],
        bins=[-np.inf, 3, np.inf],
        labels=["service_calls_le_3", "service_calls_gt_3"],
        right=True,
    ).astype("string")

    out["late_payments_group"] = pd.cut(
        out["late_payments"],
        bins=[-np.inf, 0, 2, np.inf],
        labels=["late_0", "late_1_2", "late_3_plus"],
        right=True,
    ).astype("string")

    out["monthlycharges_group"] = np.where(
        out["monthlycharges"] < 200,
        "monthly_lt_200",
        "monthly_ge_200",
    )

    if "num_services" in out.columns:
        out["num_services_group"] = pd.cut(
            out["num_services"],
            bins=[0, 2, 4, 6],
            labels=["services_1_2", "services_3_4", "services_5_6"],
            right=True,
        ).astype("string")

    if "paperless_billing" in out.columns:
        out["paperless_billing_flag"] = out["paperless_billing"].map({"No": 0, "Yes": 1})

    return out


def encode_features(df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    matrix = df[features].copy()
    categorical_cols = matrix.select_dtypes(include=["object", "string", "category"]).columns.tolist()
    encoded = pd.get_dummies(matrix, columns=categorical_cols, dtype="uint8")
    return encoded


def summarize_split(name: str, df: pd.DataFrame) -> SplitSummary:
    churn_count = int(df["churn"].sum())
    non_churn_count = int((df["churn"] == 0).sum())
    return SplitSummary(
        split=name,
        rows=int(len(df)),
        non_churn_0=non_churn_count,
        churn_1=churn_count,
        churn_pct=round(float(df["churn"].mean() * 100), 4),
    )


def threshold_metrics(y_true: pd.Series, probabilities: np.ndarray, threshold: float) -> dict:
    y_pred = (probabilities >= threshold).astype(int)
    return {
        "threshold": round(float(threshold), 4),
        "accuracy": round(float(accuracy_score(y_true, y_pred)), 6),
        "precision": round(float(precision_score(y_true, y_pred, zero_division=0)), 6),
        "recall": round(float(recall_score(y_true, y_pred, zero_division=0)), 6),
        "f1": round(float(f1_score(y_true, y_pred, zero_division=0)), 6),
        "roc_auc": round(float(roc_auc_score(y_true, probabilities)), 6),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }


def choose_threshold(y_true: pd.Series, probabilities: np.ndarray) -> float:
    precision, recall, thresholds = precision_recall_curve(y_true, probabilities)
    if len(thresholds) == 0:
        return 0.5
    f1_scores = 2 * precision[:-1] * recall[:-1] / np.maximum(precision[:-1] + recall[:-1], 1e-12)
    return float(thresholds[int(np.nanargmax(f1_scores))])


def risk_level(probability: float, threshold: float) -> str:
    high = max(0.65, threshold)
    medium = max(0.35, threshold * 0.6)
    if probability >= high:
        return "High Risk"
    if probability >= medium:
        return "Medium Risk"
    return "Low Risk"


def write_feature_mapping(output_dir: Path) -> None:
    mapping = [
        {"version": "churn_only", "raw_feature": "annual_income", "engineered_feature": "annual_income_group", "rule": "<30K, 30-60K, 60-90K, >90K"},
        {"version": "churn_only", "raw_feature": "education", "engineered_feature": "education_group", "rule": "master/phd = graduate; others = non_graduate"},
        {"version": "overall", "raw_feature": "tenure", "engineered_feature": "tenure_group", "rule": "1-6, 7-15, 16-31, 32+"},
        {"version": "overall, churn_only", "raw_feature": "contract", "engineered_feature": "contract", "rule": "one-hot encoded original contract category"},
        {"version": "churn_only", "raw_feature": "paperless_billing", "engineered_feature": "paperless_billing_flag", "rule": "No = 0, Yes = 1"},
        {"version": "overall", "raw_feature": "customer_satisfaction", "engineered_feature": "customer_satisfaction_group", "rule": "1-3, 4-6, 7-9"},
        {"version": "overall, churn_only", "raw_feature": "num_complaints", "engineered_feature": "num_complaints_group", "rule": "<=1, >1"},
        {"version": "overall, churn_only", "raw_feature": "num_service_calls", "engineered_feature": "num_service_calls_group", "rule": "<=3, >3"},
        {"version": "overall, churn_only", "raw_feature": "late_payments", "engineered_feature": "late_payments_group", "rule": "0, 1-2, 3+"},
        {"version": "overall, churn_only", "raw_feature": "monthlycharges", "engineered_feature": "monthlycharges_group", "rule": "<200, >=200"},
        {"version": "overall", "raw_feature": "num_services", "engineered_feature": "num_services_group", "rule": "1-2, 3-4, 5-6"},
        {"version": "overall", "raw_feature": "has_tech_support", "engineered_feature": "has_tech_support", "rule": "binary 0/1"},
    ]
    pd.DataFrame(mapping).to_csv(output_dir / "feature_mapping_note.csv", index=False)


def grouped_distribution(df: pd.DataFrame, feature: str, target_col: str | None = None) -> pd.DataFrame:
    if target_col:
        grouped = (
            df.groupby(feature, dropna=False, observed=True)
            .agg(total_customers=(target_col, "size"), churned_customers=(target_col, "sum"))
            .reset_index()
        )
        grouped["churn_rate_pct"] = (grouped["churned_customers"] / grouped["total_customers"] * 100).round(2)
        return grouped.sort_values("churn_rate_pct", ascending=False)

    grouped = df.groupby(feature, dropna=False, observed=True).size().reset_index(name="churned_customers")
    grouped["percentage_of_churned_customers"] = (grouped["churned_customers"] / len(df) * 100).round(2)
    return grouped.sort_values("percentage_of_churned_customers", ascending=False)


def make_summary_tables(df: pd.DataFrame, features: list[str], output_file: Path, target_col: str | None) -> None:
    pieces = []
    for feature in features:
        if feature not in df.columns:
            continue
        table = grouped_distribution(df, feature, target_col)
        table.insert(0, "feature", feature)
        pieces.append(table)
    pd.concat(pieces, ignore_index=True).to_csv(output_file, index=False)


def encoded_feature_family(column: str, model_features: list[str]) -> str:
    for feature in sorted(model_features, key=len, reverse=True):
        if column == feature or column.startswith(f"{feature}_"):
            return feature
    return column


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows._"
    headers = [str(column) for column in df.columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in df.iterrows():
        values = [str(row[column]) for column in df.columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def write_overall_correlation_analysis(
    encoded: pd.DataFrame,
    model_features: list[str],
    output_root: Path,
) -> None:
    output_dir = output_root / "feature_selection"
    output_dir.mkdir(parents=True, exist_ok=True)

    feature_cols = [column for column in encoded.columns if column not in ["customer_id", "churn"]]
    corr_input = encoded[["churn", *feature_cols]].astype("float32")
    correlation_matrix = corr_input.corr(numeric_only=True).round(6)
    correlation_matrix.to_csv(output_dir / "overall_encoded_correlation_matrix.csv")

    target_corr = (
        correlation_matrix["churn"]
        .drop(labels=["churn"])
        .dropna()
        .rename("correlation_with_churn")
        .reset_index()
        .rename(columns={"index": "encoded_feature"})
    )
    target_corr["abs_correlation_with_churn"] = target_corr["correlation_with_churn"].abs().round(6)
    target_corr["feature_family"] = target_corr["encoded_feature"].map(lambda col: encoded_feature_family(col, model_features))
    target_corr = target_corr.sort_values("abs_correlation_with_churn", ascending=False)
    target_corr.to_csv(output_dir / "overall_churn_target_correlations.csv", index=False)

    family_rows = []
    for family, part in target_corr.groupby("feature_family", sort=False):
        top = part.iloc[0]
        family_rows.append(
            {
                "feature_family": family,
                "max_abs_correlation_with_churn": round(float(part["abs_correlation_with_churn"].max()), 6),
                "mean_abs_correlation_with_churn": round(float(part["abs_correlation_with_churn"].mean()), 6),
                "top_encoded_feature": top["encoded_feature"],
                "top_encoded_feature_correlation": round(float(top["correlation_with_churn"]), 6),
            }
        )
    family_summary = pd.DataFrame(family_rows).sort_values("max_abs_correlation_with_churn", ascending=False)
    family_summary.to_csv(output_dir / "overall_feature_family_correlation_summary.csv", index=False)

    markdown = [
        "# Phase 2 Correlation-Based Feature Selection",
        "",
        "This analysis uses the full overall dataset after phase-2 feature grouping and one-hot encoding.",
        "Correlation is a univariate screening signal, not a final model-selection rule.",
        "It should be interpreted together with Random Forest feature importance and business actionability.",
        "",
        "## Top Encoded Features by Absolute Correlation with Churn",
        "",
        dataframe_to_markdown(target_corr.head(20)),
        "",
        "## Feature Family Summary",
        "",
        dataframe_to_markdown(family_summary),
        "",
        "## Churn-Only Note",
        "",
        "`customer_churn_only.csv` contains only churned customers, so correlation with the churn target is undefined.",
        "Use churn-only outputs for customer profiling, not for selecting binary churn classifier features.",
        "",
    ]
    (output_dir / "correlation_feature_selection_summary.md").write_text("\n".join(markdown), encoding="utf-8")

    print("\n=== Overall encoded feature correlation with churn: top 20 by absolute value ===")
    print(target_corr.head(20).to_string(index=False))
    print("\n=== Feature-family correlation summary ===")
    print(family_summary.to_string(index=False))
    print(f"\nCorrelation outputs written to: {output_dir}")


def write_churn_only_correlation_note(encoded: pd.DataFrame, model_features: list[str], output_root: Path) -> None:
    output_dir = output_root / "feature_selection"
    output_dir.mkdir(parents=True, exist_ok=True)

    feature_cols = [column for column in encoded.columns if column not in ["customer_id", "churn"]]
    support_matrix = encoded[feature_cols].astype("float32").corr(numeric_only=True).round(6)
    support_matrix.to_csv(output_dir / "churn_only_support_feature_correlation_matrix.csv")
    note = {
        "dataset": "customer_churn_only.csv",
        "target_unique_values": sorted(encoded["churn"].dropna().unique().tolist()),
        "target_correlation_available": False,
        "reason": "The churn_only dataset contains only churn=1 rows, so correlation with the churn target is undefined.",
        "support_matrix": "churn_only_support_feature_correlation_matrix.csv",
        "support_features": model_features,
    }
    (output_dir / "churn_only_correlation_note.json").write_text(json.dumps(note, indent=2), encoding="utf-8")


def run_overall(args: argparse.Namespace) -> tuple[RandomForestClassifier, pd.DataFrame, float, list[str]]:
    output_root = Path(args.output_root)
    output_dir = output_root / "overall"
    output_dir.mkdir(parents=True, exist_ok=True)

    clean_csv = resolve_input_csv(args.clean_csv, "customer_churn_dataset_clean.csv")
    clean = pd.read_csv(clean_csv)
    ensure_columns(clean, ["customer_id", "churn", *OVERALL_RAW_FEATURES], "overall clean dataset")
    grouped = add_feature_groups(clean)

    keep_cols = ["customer_id", "churn", *OVERALL_RAW_FEATURES, *OVERALL_MODEL_FEATURES]
    grouped[keep_cols].to_csv(output_dir / "overall_grouped_dataset.csv", index=False)
    make_summary_tables(
        grouped,
        [
            "tenure_group",
            "contract",
            "customer_satisfaction_group",
            "num_complaints_group",
            "num_service_calls_group",
            "late_payments_group",
            "monthlycharges_group",
            "num_services_group",
            "has_tech_support",
        ],
        output_dir / "overall_group_summary.csv",
        "churn",
    )

    encoded_x = encode_features(grouped, OVERALL_MODEL_FEATURES)
    encoded = pd.concat([grouped[["customer_id", "churn"]], encoded_x], axis=1)
    encoded.to_csv(output_dir / "overall_encoded_dataset.csv", index=False)
    write_overall_correlation_analysis(encoded, OVERALL_MODEL_FEATURES, output_root)

    train_df, temp_df = train_test_split(
        encoded,
        test_size=0.30,
        random_state=args.random_state,
        stratify=encoded["churn"],
    )
    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.50,
        random_state=args.random_state,
        stratify=temp_df["churn"],
    )

    for name, part in [("train", train_df), ("validation", val_df), ("test", test_df)]:
        part.to_csv(output_dir / f"overall_{name}.csv", index=False)

    split_summary = [asdict(summarize_split("full", encoded))]
    split_summary.extend(asdict(summarize_split(name, part)) for name, part in [("train", train_df), ("validation", val_df), ("test", test_df)])
    pd.DataFrame(split_summary).to_csv(output_dir / "overall_split_summary.csv", index=False)

    feature_cols = [column for column in encoded.columns if column not in ["customer_id", "churn"]]
    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        min_samples_leaf=args.min_samples_leaf,
        class_weight="balanced_subsample",
        random_state=args.random_state,
        n_jobs=-1,
    )

    model.fit(train_df[feature_cols], train_df["churn"])

    val_prob = model.predict_proba(val_df[feature_cols])[:, 1]
    threshold = choose_threshold(val_df["churn"], val_prob)
    test_prob = model.predict_proba(test_df[feature_cols])[:, 1]
    test_pred = (test_prob >= threshold).astype(int)

    metrics = {
        "model": "RandomForestClassifier",
        "n_estimators": args.n_estimators,
        "max_depth": args.max_depth,
        "min_samples_leaf": args.min_samples_leaf,
        "class_weight": "balanced_subsample",
        "random_state": args.random_state,
        "selected_threshold_from_validation": round(float(threshold), 6),
        "validation_default_0_5": threshold_metrics(val_df["churn"], val_prob, 0.5),
        "validation_selected_threshold": threshold_metrics(val_df["churn"], val_prob, threshold),
        "test_default_0_5": threshold_metrics(test_df["churn"], test_prob, 0.5),
        "test_selected_threshold": threshold_metrics(test_df["churn"], test_prob, threshold),
        "test_classification_report_selected_threshold": classification_report(test_df["churn"], test_pred, output_dict=True, zero_division=0),
    }
    (output_dir / "overall_model_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    importances = pd.DataFrame(
        {
            "feature": feature_cols,
            "importance": model.feature_importances_,
        }
    ).sort_values("importance", ascending=False)
    importances.to_csv(output_dir / "overall_feature_importance.csv", index=False)

    joblib.dump(
        {
            "model": model,
            "feature_columns": feature_cols,
            "threshold": threshold,
            "model_features": OVERALL_MODEL_FEATURES,
        },
        output_dir / "overall_random_forest_model.joblib",
    )

    non_churn = grouped.loc[grouped["churn"] == 0].copy()
    non_churn_x = encode_features(non_churn, OVERALL_MODEL_FEATURES).reindex(columns=feature_cols, fill_value=0)
    non_churn_prob = model.predict_proba(non_churn_x)[:, 1]
    non_churn_scores = non_churn[["customer_id", *OVERALL_RAW_FEATURES]].copy()
    non_churn_scores["churn_probability"] = np.round(non_churn_prob, 6)
    non_churn_scores["predicted_churn"] = (non_churn_prob >= threshold).astype(int)
    non_churn_scores["risk_level"] = [risk_level(float(prob), threshold) for prob in non_churn_prob]
    non_churn_scores.sort_values("churn_probability", ascending=False).to_csv(
        output_dir / "overall_non_churn_risk_scores.csv",
        index=False,
    )

    return model, grouped, threshold, feature_cols


def run_churn_only(
    args: argparse.Namespace,
    overall_model: RandomForestClassifier | None,
    overall_threshold: float | None,
    overall_feature_cols: list[str] | None,
) -> None:
    output_root = Path(args.output_root)
    output_dir = output_root / "churn_only"
    output_dir.mkdir(parents=True, exist_ok=True)

    churn_only_csv = resolve_input_csv(args.churn_only_csv, "customer_churn_only.csv")
    churn = pd.read_csv(churn_only_csv)
    ensure_columns(churn, ["customer_id", "churn", *CHURN_ONLY_RAW_FEATURES], "churn_only dataset")
    grouped = add_feature_groups(churn)

    keep_cols = ["customer_id", "churn", *CHURN_ONLY_RAW_FEATURES, *CHURN_ONLY_SUPPORT_FEATURES]
    grouped[keep_cols].to_csv(output_dir / "churn_only_grouped_dataset.csv", index=False)
    encoded_x = encode_features(grouped, CHURN_ONLY_SUPPORT_FEATURES)
    encoded = pd.concat([grouped[["customer_id", "churn"]], encoded_x], axis=1)
    encoded.to_csv(output_dir / "churn_only_encoded_dataset.csv", index=False)
    write_churn_only_correlation_note(encoded, CHURN_ONLY_SUPPORT_FEATURES, output_root)

    make_summary_tables(
        grouped,
        [
            "annual_income_group",
            "education_group",
            "contract",
            "paperless_billing_flag",
            "num_complaints_group",
            "num_service_calls_group",
            "late_payments_group",
            "monthlycharges_group",
        ],
        output_dir / "churn_only_profile_summary.csv",
        None,
    )

    split_note = {
        "rows": int(len(grouped)),
        "churn_1": int(grouped["churn"].sum()),
        "non_churn_0": int((grouped["churn"] == 0).sum()),
        "can_train_binary_churn_classifier": False,
        "reason": "customer_churn_only.csv contains only churn=1 rows, so it is a support/profiling dataset rather than a standalone binary classifier training set.",
    }
    (output_dir / "churn_only_phase2_note.json").write_text(json.dumps(split_note, indent=2), encoding="utf-8")

    if overall_model is None or overall_threshold is None or overall_feature_cols is None:
        return

    scoring_x = encode_features(grouped, OVERALL_MODEL_FEATURES).reindex(columns=overall_feature_cols, fill_value=0)
    probabilities = overall_model.predict_proba(scoring_x)[:, 1]
    scores = grouped[["customer_id", *CHURN_ONLY_RAW_FEATURES]].copy()
    scores["churn_probability_from_overall_model"] = np.round(probabilities, 6)
    scores["predicted_churn_from_overall_model"] = (probabilities >= overall_threshold).astype(int)
    scores["risk_level_from_overall_model"] = [risk_level(float(prob), overall_threshold) for prob in probabilities]
    scores.sort_values("churn_probability_from_overall_model", ascending=False).to_csv(
        output_dir / "churn_only_scored_by_overall_model.csv",
        index=False,
    )

    risk_summary = (
        scores.groupby("risk_level_from_overall_model")
        .agg(churned_customers=("customer_id", "size"), mean_probability=("churn_probability_from_overall_model", "mean"))
        .reset_index()
    )
    risk_summary["percentage_of_churned_customers"] = (risk_summary["churned_customers"] / len(scores) * 100).round(2)
    risk_summary["mean_probability"] = risk_summary["mean_probability"].round(6)
    risk_summary.to_csv(output_dir / "churn_only_overall_model_risk_summary.csv", index=False)


def write_kaggle_files() -> None:
    kaggle_dir = ROOT / "phase2" / "kaggle_kernel"
    local_pipeline = ROOT / "phase2" / "phase2_pipeline.py"
    if not local_pipeline.exists():
        return
    kaggle_dir.mkdir(parents=True, exist_ok=True)
    pipeline_source = local_pipeline.read_text(encoding="utf-8")
    (kaggle_dir / "phase2_pipeline.py").write_text(pipeline_source, encoding="utf-8")
    future_import = "from __future__ import annotations\n\n"
    prefix = ""
    if pipeline_source.startswith(future_import):
        prefix = future_import
        pipeline_source = pipeline_source[len(future_import):]
    (kaggle_dir / "run_phase2.py").write_text(
        prefix
        + "import sys\n"
        "sys.argv = [\n"
        "    'run_phase2.py',\n"
        "    '--clean-csv', '/kaggle/input/datavis-customer-churn-phase2/customer_churn_dataset_clean.csv',\n"
        "    '--churn-only-csv', '/kaggle/input/datavis-customer-churn-phase2/customer_churn_only.csv',\n"
        "    '--output-root', '/kaggle/working/phase2_outputs',\n"
        "    '--no-write-kaggle-files',\n"
        "]\n\n"
        + pipeline_source,
        encoding="utf-8",
    )
    metadata = {
        "id": "minhhuyen3012nguyen/datavis-phase-2-random-forest",
        "title": "DataVis Phase 2 Random Forest",
        "code_file": "run_phase2.py",
        "language": "python",
        "kernel_type": "script",
        "is_private": True,
        "enable_gpu": False,
        "enable_internet": False,
        "dataset_sources": ["minhhuyen3012nguyen/datavis-customer-churn-phase2"],
        "competition_sources": [],
        "kernel_sources": [],
    }
    (kaggle_dir / "kernel-metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 2 pipeline for overall and churn_only versions.")
    parser.add_argument("--n-estimators", type=int, default=200)
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument("--min-samples-leaf", type=int, default=50)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--clean-csv", default=str(CLEAN_CSV))
    parser.add_argument("--churn-only-csv", default=str(CHURN_ONLY_CSV))
    parser.add_argument("--output-root", default=str(OUTPUT_ROOT))
    parser.add_argument("--skip-model", action="store_true")
    parser.add_argument("--no-write-kaggle-files", action="store_true")
    args = parser.parse_args()

    output_root = Path(args.output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    write_feature_mapping(output_root)
    if not args.no_write_kaggle_files:
        write_kaggle_files()

    if args.skip_model:
        run_churn_only(args, None, None, None)
        return

    model, _, threshold, feature_cols = run_overall(args)
    run_churn_only(args, model, threshold, feature_cols)


if __name__ == "__main__":
    main()
