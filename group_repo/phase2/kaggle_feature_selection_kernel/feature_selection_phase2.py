from __future__ import annotations

import json
import os
import re
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


RANDOM_STATE = 42
OUTPUT_ROOT = Path(os.environ.get("KAGGLE_WORKING_ROOT", "/kaggle/working")) / "feature_selection_outputs"

PHASE2_RAW_FEATURES = [
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

PHASE2_MODEL_FEATURES = [
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

RAW_NUMERIC_CANDIDATES = [
    "age",
    "annual_income",
    "dependents",
    "senior_citizen",
    "tenure",
    "monthlycharges",
    "totalcharges",
    "num_services",
    "has_phone_service",
    "has_internet_service",
    "has_online_security",
    "has_online_backup",
    "has_device_protection",
    "has_tech_support",
    "has_streaming_tv",
    "has_streaming_movies",
    "customer_satisfaction",
    "num_complaints",
    "num_service_calls",
    "late_payments",
    "avg_monthly_gb",
    "days_since_last_interaction",
    "credit_score",
]

COLUMN_ALIASES = {
    "customerid": "customer_id",
    "customer_id": "customer_id",
    "customer id": "customer_id",
    "signup_date": "signup_date",
    "signup date": "signup_date",
    "join_date": "signup_date",
    "churn": "churn",
    "churned": "churn",
    "churn_label": "churn",
    "churn status": "churn",
    "customer_churn": "churn",
    "annual_income": "annual_income",
    "annual income": "annual_income",
    "income": "annual_income",
    "monthlycharges": "monthlycharges",
    "monthly_charges": "monthlycharges",
    "monthly charges": "monthlycharges",
    "monthly_charge": "monthlycharges",
    "totalcharges": "totalcharges",
    "total_charges": "totalcharges",
    "total charges": "totalcharges",
    "customer_satisfaction": "customer_satisfaction",
    "customer satisfaction": "customer_satisfaction",
    "satisfaction": "customer_satisfaction",
    "num_complaints": "num_complaints",
    "number_of_complaints": "num_complaints",
    "number of complaints": "num_complaints",
    "complaints": "num_complaints",
    "num_service_calls": "num_service_calls",
    "number_of_service_calls": "num_service_calls",
    "number of service calls": "num_service_calls",
    "service_calls": "num_service_calls",
    "late_payments": "late_payments",
    "late payments": "late_payments",
    "num_services": "num_services",
    "number_of_services": "num_services",
    "number of services": "num_services",
    "has_tech_support": "has_tech_support",
    "tech_support": "has_tech_support",
    "tech support": "has_tech_support",
    "technical_support": "has_tech_support",
    "paperless_billing": "paperless_billing",
    "paperless billing": "paperless_billing",
    "avg_monthly_gb": "avg_monthly_gb",
    "average_monthly_gb": "avg_monthly_gb",
    "average monthly gb": "avg_monthly_gb",
    "days_since_last_interaction": "days_since_last_interaction",
    "days since last interaction": "days_since_last_interaction",
    "credit_score": "credit_score",
    "credit score": "credit_score",
}


@dataclass
class SplitSummary:
    split: str
    rows: int
    non_churn_0: int
    churn_1: int
    churn_pct: float


def normalize_column_name(column: str) -> str:
    raw = str(column).strip()
    lower = raw.lower().strip()
    lower = re.sub(r"[^a-z0-9]+", "_", lower).strip("_")
    spaced = lower.replace("_", " ")
    return COLUMN_ALIASES.get(lower, COLUMN_ALIASES.get(spaced, lower))


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [normalize_column_name(column) for column in out.columns]
    out = out.loc[:, ~out.columns.duplicated()]
    return out


def find_candidate_csvs() -> list[Path]:
    roots = [Path(os.environ.get("KAGGLE_INPUT_ROOT", "/kaggle/input"))]
    csvs: list[Path] = []
    for root in roots:
        if root.exists():
            csvs.extend(root.rglob("*.csv"))
    return sorted(csvs, key=lambda path: path.stat().st_size, reverse=True)


def dataset_score(columns: Iterable[str]) -> int:
    names = set(columns)
    score = 0
    if "churn" in names:
        score += 100
    score += sum(1 for feature in PHASE2_RAW_FEATURES if feature in names) * 10
    score += sum(1 for feature in RAW_NUMERIC_CANDIDATES if feature in names)
    return score


def load_best_dataset() -> tuple[pd.DataFrame, Path]:
    candidates = find_candidate_csvs()
    if not candidates:
        raise FileNotFoundError("No CSV files found under /kaggle/input.")

    scored: list[tuple[int, Path]] = []
    for path in candidates:
        try:
            sample = normalize_columns(pd.read_csv(path, nrows=1000))
        except Exception as exc:
            print(f"Skipping unreadable CSV {path}: {exc}")
            continue
        scored.append((dataset_score(sample.columns), path))

    if not scored:
        raise FileNotFoundError("No readable CSV files found under /kaggle/input.")

    score, best_path = max(scored, key=lambda item: item[0])
    if score < 100:
        raise ValueError(
            "Could not find a CSV with a churn target. Candidate scores: "
            + str([(s, str(p)) for s, p in scored[:10]])
        )

    df = normalize_columns(pd.read_csv(best_path))
    return df, best_path


def normalize_binary(series: pd.Series, column: str) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors="coerce").fillna(0).astype(int)

    values = series.astype("string").str.strip().str.lower()
    mapping = {
        "yes": 1,
        "y": 1,
        "true": 1,
        "1": 1,
        "churn": 1,
        "churned": 1,
        "leave": 1,
        "left": 1,
        "no": 0,
        "n": 0,
        "false": 0,
        "0": 0,
        "not churn": 0,
        "not_churn": 0,
        "not churned": 0,
        "stayed": 0,
        "stay": 0,
    }
    normalized = values.map(mapping)
    if normalized.isna().any():
        unknown = sorted(values[normalized.isna()].dropna().unique().tolist())[:10]
        raise ValueError(f"Column {column} has unmapped binary values: {unknown}")
    return normalized.astype(int)


def standardize_values(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "customer_id" not in out.columns:
        out.insert(0, "customer_id", [f"ROW{i:09d}" for i in range(len(out))])

    out["churn"] = normalize_binary(out["churn"], "churn")

    for column in out.select_dtypes(include=["object", "string"]).columns:
        if column == "customer_id":
            continue
        out[column] = (
            out[column]
            .astype("string")
            .str.strip()
            .str.lower()
            .str.replace(r"[^a-z0-9]+", "_", regex=True)
            .str.strip("_")
        )

    for column in RAW_NUMERIC_CANDIDATES:
        if column in out.columns:
            out[column] = pd.to_numeric(out[column], errors="coerce")

    binary_candidates = [
        "has_tech_support",
        "has_phone_service",
        "has_internet_service",
        "has_online_security",
        "has_online_backup",
        "has_device_protection",
        "has_streaming_tv",
        "has_streaming_movies",
        "paperless_billing",
    ]
    for column in binary_candidates:
        if column in out.columns and not pd.api.types.is_numeric_dtype(out[column]):
            mapped = out[column].map({"yes": 1, "no": 0, "true": 1, "false": 0}).fillna(out[column])
            converted = pd.to_numeric(mapped, errors="coerce")
            out[column] = converted if converted.notna().all() else mapped

    return out


def ensure_columns(df: pd.DataFrame, columns: Iterable[str], context: str) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{context} is missing required columns: {missing}. Available columns: {list(df.columns)}")


def add_feature_groups(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    out["tenure_group"] = pd.cut(
        out["tenure"],
        bins=[0, 6, 15, 31, np.inf],
        labels=["tenure_1_6", "tenure_7_15", "tenure_16_31", "tenure_32_plus"],
        right=True,
    ).astype("string")

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

    out["monthlycharges_group"] = np.where(out["monthlycharges"] < 200, "monthly_lt_200", "monthly_ge_200")

    out["num_services_group"] = pd.cut(
        out["num_services"],
        bins=[0, 2, 4, 6, np.inf],
        labels=["services_1_2", "services_3_4", "services_5_6", "services_7_plus"],
        right=True,
    ).astype("string")

    return out


def encode_features(df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    matrix = df[features].copy()
    categorical_cols = matrix.select_dtypes(include=["object", "string", "category"]).columns.tolist()
    return pd.get_dummies(matrix, columns=categorical_cols, dtype="uint8")


def feature_family(encoded_feature: str, model_features: list[str]) -> str:
    for feature in sorted(model_features, key=len, reverse=True):
        if encoded_feature == feature or encoded_feature.startswith(f"{feature}_"):
            return feature
    return encoded_feature


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
        "threshold": round(float(threshold), 6),
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


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows._"
    headers = [str(column) for column in df.columns]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for _, row in df.iterrows():
        values = [str(row[column]) for column in df.columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def correlation_outputs(encoded: pd.DataFrame, raw: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    feature_cols = [column for column in encoded.columns if column not in ["customer_id", "churn"]]
    corr_input = encoded[["churn", *feature_cols]].astype("float32")
    correlation_matrix = corr_input.corr(numeric_only=True).round(6)
    correlation_matrix.to_csv(OUTPUT_ROOT / "overall_encoded_correlation_matrix.csv")

    target_corr = (
        correlation_matrix["churn"]
        .drop(labels=["churn"])
        .dropna()
        .rename("correlation_with_churn")
        .reset_index()
        .rename(columns={"index": "encoded_feature"})
    )
    target_corr["abs_correlation_with_churn"] = target_corr["correlation_with_churn"].abs().round(6)
    target_corr["feature_family"] = target_corr["encoded_feature"].map(lambda col: feature_family(col, PHASE2_MODEL_FEATURES))
    target_corr = target_corr.sort_values("abs_correlation_with_churn", ascending=False)
    target_corr.to_csv(OUTPUT_ROOT / "overall_churn_target_correlations.csv", index=False)

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
    family_summary.to_csv(OUTPUT_ROOT / "overall_feature_family_correlation_summary.csv", index=False)

    raw_numeric = [column for column in RAW_NUMERIC_CANDIDATES if column in raw.columns]
    raw_corr_input = raw[["churn", *raw_numeric]].copy()
    for column in raw_corr_input.columns:
        raw_corr_input[column] = pd.to_numeric(raw_corr_input[column], errors="coerce")
    raw_corr = raw_corr_input.corr(numeric_only=True).round(6)
    raw_corr.to_csv(OUTPUT_ROOT / "raw_numeric_correlation_matrix.csv")
    raw_target_corr = (
        raw_corr["churn"]
        .drop(labels=["churn"])
        .dropna()
        .rename("correlation_with_churn")
        .reset_index()
        .rename(columns={"index": "raw_numeric_feature"})
        .sort_values("correlation_with_churn", key=lambda s: s.abs(), ascending=False)
    )
    raw_target_corr.to_csv(OUTPUT_ROOT / "raw_numeric_target_correlations.csv", index=False)

    top_features = ["churn", *target_corr.head(20)["encoded_feature"].tolist()]
    correlation_matrix.loc[top_features, top_features].to_csv(OUTPUT_ROOT / "top20_encoded_correlation_matrix.csv")

    return target_corr, family_summary, raw_target_corr


def run_random_forest(encoded: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    feature_cols = [column for column in encoded.columns if column not in ["customer_id", "churn"]]

    train_df, temp_df = train_test_split(
        encoded,
        test_size=0.30,
        random_state=RANDOM_STATE,
        stratify=encoded["churn"],
    )
    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.50,
        random_state=RANDOM_STATE,
        stratify=temp_df["churn"],
    )

    split_summary = [asdict(summarize_split("full", encoded))]
    split_summary.extend(
        asdict(summarize_split(name, part))
        for name, part in [("train", train_df), ("validation", val_df), ("test", test_df)]
    )
    pd.DataFrame(split_summary).to_csv(OUTPUT_ROOT / "split_summary.csv", index=False)

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        min_samples_leaf=50,
        class_weight="balanced_subsample",
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(train_df[feature_cols], train_df["churn"])

    val_prob = model.predict_proba(val_df[feature_cols])[:, 1]
    threshold = choose_threshold(val_df["churn"], val_prob)
    test_prob = model.predict_proba(test_df[feature_cols])[:, 1]
    test_pred = (test_prob >= threshold).astype(int)

    metrics = {
        "model": "RandomForestClassifier",
        "phase2_reproducible_split": "70% train, 15% validation, 15% test",
        "random_state": RANDOM_STATE,
        "n_estimators": 200,
        "max_depth": 12,
        "min_samples_leaf": 50,
        "class_weight": "balanced_subsample",
        "selected_threshold_from_validation": round(float(threshold), 6),
        "validation_default_0_5": threshold_metrics(val_df["churn"], val_prob, 0.5),
        "validation_selected_threshold": threshold_metrics(val_df["churn"], val_prob, threshold),
        "test_default_0_5": threshold_metrics(test_df["churn"], test_prob, 0.5),
        "test_selected_threshold": threshold_metrics(test_df["churn"], test_prob, threshold),
        "test_classification_report_selected_threshold": classification_report(
            test_df["churn"], test_pred, output_dict=True, zero_division=0
        ),
    }
    (OUTPUT_ROOT / "random_forest_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    importances = pd.DataFrame({"encoded_feature": feature_cols, "importance": model.feature_importances_})
    importances["feature_family"] = importances["encoded_feature"].map(lambda col: feature_family(col, PHASE2_MODEL_FEATURES))
    importances = importances.sort_values("importance", ascending=False)
    importances.to_csv(OUTPUT_ROOT / "random_forest_feature_importance.csv", index=False)

    family_importance = (
        importances.groupby("feature_family", as_index=False)
        .agg(
            total_importance=("importance", "sum"),
            max_encoded_feature_importance=("importance", "max"),
            mean_encoded_feature_importance=("importance", "mean"),
            encoded_feature_count=("encoded_feature", "size"),
        )
        .sort_values("total_importance", ascending=False)
    )
    family_importance.to_csv(OUTPUT_ROOT / "random_forest_feature_family_importance.csv", index=False)

    joblib.dump(
        {
            "model": model,
            "feature_columns": feature_cols,
            "threshold": threshold,
            "model_features": PHASE2_MODEL_FEATURES,
        },
        OUTPUT_ROOT / "random_forest_model.joblib",
    )
    return importances, metrics


def combined_recommendations(
    target_corr: pd.DataFrame,
    family_summary: pd.DataFrame,
    importances: pd.DataFrame,
) -> pd.DataFrame:
    family_importance = (
        importances.groupby("feature_family", as_index=False)
        .agg(total_importance=("importance", "sum"), max_importance=("importance", "max"))
        .sort_values("total_importance", ascending=False)
    )
    merged = family_summary.merge(family_importance, on="feature_family", how="outer").fillna(0)
    merged["correlation_rank"] = merged["max_abs_correlation_with_churn"].rank(method="min", ascending=False)
    merged["importance_rank"] = merged["total_importance"].rank(method="min", ascending=False)
    merged["combined_rank_score"] = merged["correlation_rank"] + merged["importance_rank"]
    merged = merged.sort_values(["combined_rank_score", "importance_rank", "correlation_rank"])
    merged.to_csv(OUTPUT_ROOT / "feature_family_selection_recommendation.csv", index=False)

    encoded = target_corr.merge(importances, on=["encoded_feature", "feature_family"], how="outer").fillna(0)
    encoded["correlation_rank"] = encoded["abs_correlation_with_churn"].rank(method="min", ascending=False)
    encoded["importance_rank"] = encoded["importance"].rank(method="min", ascending=False)
    encoded["combined_rank_score"] = encoded["correlation_rank"] + encoded["importance_rank"]
    encoded = encoded.sort_values(["combined_rank_score", "importance_rank", "correlation_rank"])
    encoded.to_csv(OUTPUT_ROOT / "encoded_feature_selection_recommendation.csv", index=False)
    return merged


def write_summary(
    dataset_path: Path,
    clean: pd.DataFrame,
    target_corr: pd.DataFrame,
    raw_target_corr: pd.DataFrame,
    family_summary: pd.DataFrame,
    importances: pd.DataFrame,
    recommendation: pd.DataFrame,
    metrics: dict,
) -> None:
    test_metrics = metrics["test_selected_threshold"]
    lines = [
        "# Phase 2 Feature Selection: Correlation + Random Forest",
        "",
        f"- Source dataset file: `{dataset_path}`",
        f"- Rows: {len(clean):,}",
        f"- Columns after normalization: {len(clean.columns):,}",
        f"- Churn rate: {clean['churn'].mean() * 100:.4f}%",
        "- Split: reproducible 70% train, 15% validation, 15% test with `random_state=42` and stratified churn.",
        "- Algorithm: RandomForestClassifier with the same phase-2 settings: 200 trees, max_depth=12, min_samples_leaf=50, class_weight=balanced_subsample.",
        "",
        "## Test Metrics at Validation-Selected Threshold",
        "",
        dataframe_to_markdown(pd.DataFrame([test_metrics])),
        "",
        "## Top Encoded Features by Absolute Correlation with Churn",
        "",
        dataframe_to_markdown(target_corr.head(25)),
        "",
        "## Top Raw Numeric Features by Absolute Correlation with Churn",
        "",
        dataframe_to_markdown(raw_target_corr.head(25)),
        "",
        "## Feature Family Correlation Summary",
        "",
        dataframe_to_markdown(family_summary),
        "",
        "## Random Forest Feature Importance: Top Encoded Features",
        "",
        dataframe_to_markdown(importances.head(25)),
        "",
        "## Recommended Feature Families",
        "",
        dataframe_to_markdown(recommendation),
        "",
        "## Interpretation Rule",
        "",
        "Correlation is used as a univariate screening signal. Random Forest importance is used as a model-based signal. Feature families that score high on both are the strongest candidates for phase 2.",
        "",
    ]
    (OUTPUT_ROOT / "feature_selection_summary.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n=== Dataset ===")
    print(f"Source file: {dataset_path}")
    print(f"Shape: {clean.shape}")
    print(f"Churn rate: {clean['churn'].mean() * 100:.4f}%")
    print("\n=== Top encoded correlations with churn ===")
    print(target_corr.head(25).to_string(index=False))
    print("\n=== Raw numeric correlations with churn ===")
    print(raw_target_corr.head(25).to_string(index=False))
    print("\n=== Feature family recommendation ===")
    print(recommendation.to_string(index=False))
    print("\n=== Test metrics selected threshold ===")
    print(json.dumps(test_metrics, indent=2))
    print(f"\nOutputs written to {OUTPUT_ROOT}")


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    raw, dataset_path = load_best_dataset()
    clean = standardize_values(raw)
    ensure_columns(clean, ["customer_id", "churn", *PHASE2_RAW_FEATURES], "source dataset")

    grouped = add_feature_groups(clean)
    encoded_x = encode_features(grouped, PHASE2_MODEL_FEATURES)
    encoded = pd.concat([grouped[["customer_id", "churn"]], encoded_x], axis=1)

    clean.head(1000).to_csv(OUTPUT_ROOT / "normalized_source_dataset_head_1000.csv", index=False)
    grouped[["customer_id", "churn", *PHASE2_RAW_FEATURES, *PHASE2_MODEL_FEATURES]].head(1000).to_csv(
        OUTPUT_ROOT / "phase2_grouped_dataset_head_1000.csv",
        index=False,
    )

    target_corr, family_summary, raw_target_corr = correlation_outputs(encoded, grouped)
    importances, metrics = run_random_forest(encoded)
    recommendation = combined_recommendations(target_corr, family_summary, importances)
    write_summary(dataset_path, clean, target_corr, raw_target_corr, family_summary, importances, recommendation, metrics)


if __name__ == "__main__":
    main()
