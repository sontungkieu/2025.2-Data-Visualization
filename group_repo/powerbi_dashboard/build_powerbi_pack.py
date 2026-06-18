from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PHASE2 = ROOT / "phase2_outputs" / "kaggle_downloaded" / "phase2_outputs"
OUT = ROOT / "powerbi_dashboard"
DATA = OUT / "data"
DOCS = OUT / "docs"


DISPLAY_NAMES = {
    "annual_income_group": "Annual Income",
    "education_group": "Education",
    "tenure_group": "Tenure",
    "contract": "Contract Type",
    "customer_satisfaction_group": "Customer Satisfaction",
    "num_complaints_group": "Number of Complaints",
    "num_service_calls_group": "Number of Service Calls",
    "late_payments_group": "Late Payments",
    "monthlycharges_group": "Monthly Charges",
    "num_services_group": "Number of Services",
    "has_tech_support": "Tech Support",
    "paperless_billing_flag": "Paperless Billing",
    "contract_display": "Contract Type",
    "has_tech_support_label": "Tech Support",
    "num_services": "Number of Services",
    "num_service_calls": "Number of Service Calls",
    "num_complaints": "Number of Complaints",
}

ORDERED_OVERALL_FEATURES = [
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

ORDERED_CHURN_ONLY_FEATURES = [
    "contract",
    "annual_income_group",
    "education_group",
    "paperless_billing_flag",
    "num_complaints_group",
    "num_service_calls_group",
    "late_payments_group",
    "monthlycharges_group",
]


def mkdirs() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def category_label(value) -> str:
    if pd.isna(value):
        return ""
    text = str(value)
    labels = {
        "income_lt_30k": "<30K",
        "income_30_60k": "30K-60K",
        "income_60_90k": "60K-90K",
        "income_gt_90k": ">90K",
        "graduate": "Graduate",
        "non_graduate": "Non-graduate",
        "tenure_1_6": "1-6 months",
        "tenure_7_15": "7-15 months",
        "tenure_16_31": "16-31 months",
        "tenure_32_plus": "32+ months",
        "satisfaction_1_3": "Low (1-3)",
        "satisfaction_4_6": "Medium (4-6)",
        "satisfaction_7_9": "High (7-9)",
        "complaints_le_1": "<=1 complaint",
        "complaints_gt_1": ">1 complaint",
        "service_calls_le_3": "<=3 calls",
        "service_calls_gt_3": ">3 calls",
        "late_0": "0 late payments",
        "late_1_2": "1-2 late payments",
        "late_3_plus": "3+ late payments",
        "monthly_lt_200": "<200",
        "monthly_ge_200": ">=200",
        "services_1_2": "1-2 services",
        "services_3_4": "3-4 services",
        "services_5_6": "5-6 services",
        "month_to_month": "Month-to-month",
        "one_year": "One year",
        "two_year": "Two year",
        "0": "No",
        "1": "Yes",
        "0.0": "No",
        "1.0": "Yes",
    }
    return labels.get(text, text.replace("_", " ").title())


def make_overall_group_summary() -> pd.DataFrame:
    source = pd.read_csv(PHASE2 / "overall" / "overall_group_summary.csv")
    rows = []
    for _, row in source.iterrows():
        feature = row["feature"]
        category = row.get(feature)
        rows.append(
            {
                "feature": feature,
                "feature_display": DISPLAY_NAMES.get(feature, feature),
                "feature_order": ORDERED_OVERALL_FEATURES.index(feature) + 1
                if feature in ORDERED_OVERALL_FEATURES
                else 999,
                "category": category_label(category),
                "category_raw": category,
                "total_customers": int(row["total_customers"]),
                "churned_customers": int(row["churned_customers"]),
                "non_churn_customers": int(row["total_customers"] - row["churned_customers"]),
                "churn_rate_pct": float(row["churn_rate_pct"]),
            }
        )
    out = pd.DataFrame(rows).sort_values(["feature_order", "churn_rate_pct"], ascending=[True, False])
    out.to_csv(DATA / "overall_group_summary_long.csv", index=False)
    return out


def make_churn_only_profile_summary() -> pd.DataFrame:
    source = pd.read_csv(PHASE2 / "churn_only" / "churn_only_profile_summary.csv")
    rows = []
    for _, row in source.iterrows():
        feature = row["feature"]
        category = row.get(feature)
        rows.append(
            {
                "feature": feature,
                "feature_display": DISPLAY_NAMES.get(feature, feature),
                "feature_order": ORDERED_CHURN_ONLY_FEATURES.index(feature) + 1
                if feature in ORDERED_CHURN_ONLY_FEATURES
                else 999,
                "category": category_label(category),
                "category_raw": category,
                "churned_customers": int(row["churned_customers"]),
                "percentage_of_churned_customers": float(row["percentage_of_churned_customers"]),
            }
        )
    out = pd.DataFrame(rows).sort_values(["feature_order", "percentage_of_churned_customers"], ascending=[True, False])
    out.to_csv(DATA / "churn_only_profile_summary_long.csv", index=False)
    return out


def make_selected_customer_table() -> None:
    usecols = [
        "customer_id",
        "churn",
        "tenure",
        "contract",
        "customer_satisfaction",
        "num_complaints",
        "num_service_calls",
        "late_payments",
        "monthlycharges",
        "num_services",
        "has_tech_support",
        "tenure_group",
        "customer_satisfaction_group",
        "num_complaints_group",
        "num_service_calls_group",
        "late_payments_group",
        "monthlycharges_group",
        "num_services_group",
    ]
    source = PHASE2 / "overall" / "overall_grouped_dataset.csv"
    selected = pd.read_csv(source, usecols=usecols)
    selected["churn_label"] = selected["churn"].map({0: "Not Churned", 1: "Churned"})
    selected["contract_display"] = selected["contract"].map(category_label)
    selected["has_tech_support_label"] = selected["has_tech_support"].astype(str).map(category_label)
    selected.to_csv(DATA / "overall_customers_selected.csv", index=False)


def make_trend_table() -> None:
    clean = pd.read_csv(ROOT / "customer_churn_dataset_clean.csv", usecols=["signup_date", "churn"])
    clean["signup_date"] = pd.to_datetime(clean["signup_date"], errors="coerce")
    clean["signup_month"] = clean["signup_date"].dt.to_period("M").dt.to_timestamp()
    trend = (
        clean.dropna(subset=["signup_month"])
        .groupby("signup_month")
        .agg(total_customers=("churn", "size"), churned_customers=("churn", "sum"))
        .reset_index()
    )
    trend["non_churn_customers"] = trend["total_customers"] - trend["churned_customers"]
    trend["churn_rate_pct"] = (trend["churned_customers"] / trend["total_customers"] * 100).round(2)
    trend["signup_month"] = trend["signup_month"].dt.strftime("%Y-%m")
    trend.to_csv(DATA / "overall_signup_month_trend.csv", index=False)


def make_metrics_tables() -> None:
    metrics = json.loads((PHASE2 / "overall" / "overall_model_metrics.json").read_text(encoding="utf-8"))
    selected = metrics["test_selected_threshold"]
    default = metrics["test_default_0_5"]
    rows = [
        {"metric": "Selected threshold", "value": metrics["selected_threshold_from_validation"], "format": "number"},
        {"metric": "Test ROC AUC", "value": selected["roc_auc"], "format": "percent"},
        {"metric": "Test accuracy", "value": selected["accuracy"], "format": "percent"},
        {"metric": "Test precision", "value": selected["precision"], "format": "percent"},
        {"metric": "Test recall", "value": selected["recall"], "format": "percent"},
        {"metric": "Test F1-score", "value": selected["f1"], "format": "percent"},
        {"metric": "Default threshold recall", "value": default["recall"], "format": "percent"},
    ]
    pd.DataFrame(rows).to_csv(DATA / "model_metrics_flat.csv", index=False)

    cm = selected["confusion_matrix"]
    cm_rows = [
        {"actual": "Not Churned", "predicted": "Not Churned", "customers": cm[0][0]},
        {"actual": "Not Churned", "predicted": "Churned", "customers": cm[0][1]},
        {"actual": "Churned", "predicted": "Not Churned", "customers": cm[1][0]},
        {"actual": "Churned", "predicted": "Churned", "customers": cm[1][1]},
    ]
    pd.DataFrame(cm_rows).to_csv(DATA / "model_confusion_matrix.csv", index=False)

    split = pd.read_csv(PHASE2 / "overall" / "overall_split_summary.csv")
    split.to_csv(DATA / "model_split_summary.csv", index=False)

    importance = pd.read_csv(PHASE2 / "overall" / "overall_feature_importance.csv")
    importance["feature_clean"] = importance["feature"].str.replace("_", " ").str.title()
    importance.to_csv(DATA / "model_feature_importance.csv", index=False)


def make_risk_tables() -> None:
    risk = pd.read_csv(PHASE2 / "overall" / "overall_non_churn_risk_scores.csv")
    risk["contract_display"] = risk["contract"].map(category_label)
    risk["has_tech_support_label"] = risk["has_tech_support"].astype(str).map(category_label)
    risk.sort_values("churn_probability", ascending=False).head(5000).to_csv(DATA / "risk_top_5000_customers.csv", index=False)

    risk_summary = (
        risk.groupby("risk_level")
        .agg(
            customers=("customer_id", "size"),
            predicted_churn=("predicted_churn", "sum"),
            avg_churn_probability=("churn_probability", "mean"),
        )
        .reset_index()
    )
    risk_summary["avg_churn_probability_pct"] = (risk_summary["avg_churn_probability"] * 100).round(2)
    risk_summary.to_csv(DATA / "risk_level_summary.csv", index=False)

    pieces = []
    for feature in ["contract_display", "num_services", "has_tech_support_label", "num_service_calls", "num_complaints"]:
        grouped = (
            risk.groupby(feature)
            .agg(
                customers=("customer_id", "size"),
                predicted_churn=("predicted_churn", "sum"),
                avg_churn_probability=("churn_probability", "mean"),
            )
            .reset_index()
            .rename(columns={feature: "category"})
        )
        grouped.insert(0, "feature", feature)
        grouped["feature_display"] = DISPLAY_NAMES.get(feature, feature.replace("_", " ").title())
        grouped["avg_churn_probability_pct"] = (grouped["avg_churn_probability"] * 100).round(2)
        pieces.append(grouped)
    pd.concat(pieces, ignore_index=True).to_csv(DATA / "risk_summary_by_feature.csv", index=False)


def make_kpi_summary() -> None:
    split = pd.read_csv(PHASE2 / "overall" / "overall_split_summary.csv")
    full = split.loc[split["split"] == "full"].iloc[0]
    metrics = json.loads((PHASE2 / "overall" / "overall_model_metrics.json").read_text(encoding="utf-8"))
    risk_summary = pd.read_csv(DATA / "risk_level_summary.csv")
    high_risk = risk_summary.loc[risk_summary["risk_level"] == "High Risk", "customers"].sum()
    medium_risk = risk_summary.loc[risk_summary["risk_level"] == "Medium Risk", "customers"].sum()

    rows = [
        {"kpi": "Total Customers", "value": int(full["rows"]), "format": "integer"},
        {"kpi": "Churned Customers", "value": int(full["churn_1"]), "format": "integer"},
        {"kpi": "Non-churn Customers", "value": int(full["non_churn_0"]), "format": "integer"},
        {"kpi": "Overall Churn Rate", "value": float(full["churn_pct"]) / 100, "format": "percent"},
        {"kpi": "High-risk Active Customers", "value": int(high_risk), "format": "integer"},
        {"kpi": "Medium-risk Active Customers", "value": int(medium_risk), "format": "integer"},
        {"kpi": "Test ROC AUC", "value": metrics["test_selected_threshold"]["roc_auc"], "format": "percent"},
        {"kpi": "Test Recall", "value": metrics["test_selected_threshold"]["recall"], "format": "percent"},
    ]
    pd.DataFrame(rows).to_csv(DATA / "kpi_summary.csv", index=False)


def write_docs() -> None:
    dax = """-- Power BI DAX measures for DataVis churn dashboard
-- These measures assume you import DataVis_PowerBI_Input.xlsx and keep the sheet names.

Total Customers =
MAXX(
    FILTER(SplitSummary, SplitSummary[split] = "full"),
    SplitSummary[rows]
)

Churned Customers =
MAXX(
    FILTER(SplitSummary, SplitSummary[split] = "full"),
    SplitSummary[churn_1]
)

Non Churn Customers =
MAXX(
    FILTER(SplitSummary, SplitSummary[split] = "full"),
    SplitSummary[non_churn_0]
)

Churn Rate =
DIVIDE([Churned Customers], [Total Customers])

Predicted Churn Customers =
SUM(RiskLevelSummary[predicted_churn])

High Risk Customers =
CALCULATE(
    SUM(RiskLevelSummary[customers]),
    RiskLevelSummary[risk_level] = "High Risk"
)

Average Churn Probability =
DIVIDE(
    SUMX(RiskLevelSummary, RiskLevelSummary[customers] * RiskLevelSummary[avg_churn_probability]),
    SUM(RiskLevelSummary[customers])
)

Churn-Only Customers =
MAXX(
    FILTER(SplitSummary, SplitSummary[split] = "full"),
    SplitSummary[churn_1]
)
"""
    (DOCS / "DAX_measures.dax").write_text(dax, encoding="utf-8")

    blueprint = """# Power BI Dashboard Blueprint

## Data tables to import
- data/overall_customers_selected.csv -> OverallCustomers
- data/overall_group_summary_long.csv -> OverallGroupSummary
- data/overall_signup_month_trend.csv -> OverallSignupTrend
- data/risk_top_5000_customers.csv -> RiskTopCustomers
- data/risk_level_summary.csv -> RiskLevelSummary
- data/risk_summary_by_feature.csv -> RiskSummaryByFeature
- data/model_feature_importance.csv -> ModelFeatureImportance
- data/model_metrics_flat.csv -> ModelMetrics
- data/model_confusion_matrix.csv -> ModelConfusionMatrix
- data/model_split_summary.csv -> ModelSplitSummary
- data/churn_only_profile_summary_long.csv -> ChurnOnlyProfile

## Page 1: Overall Churn Overview
Purpose: main dashboard page.
Visuals:
- KPI cards: Total Customers, Churned Customers, Overall Churn Rate, High-risk Active Customers.
- Line chart: OverallSignupTrend[signup_month] vs churn_rate_pct.
- Bar chart: OverallGroupSummary category by churn_rate_pct with slicer feature_display.
- Donut or stacked bar: RiskLevelSummary[risk_level] by customers.

## Page 2: Churn Drivers
Purpose: explain which feature groups drive churn.
Visuals:
- Bar chart: OverallGroupSummary[category] by churn_rate_pct.
- Matrix: feature_display, category, total_customers, churned_customers, churn_rate_pct.
- Bar chart: ModelFeatureImportance[feature_clean] by importance.
- Slicers: feature_display, contract, churn_label.

## Page 3: Prediction and Retention Priority
Purpose: show model output and who needs attention.
Visuals:
- KPI cards: Predicted Churn Customers, High Risk Customers, Average Churn Probability.
- Table: RiskTopCustomers top customers sorted by churn_probability.
- Bar chart: RiskSummaryByFeature category by avg_churn_probability_pct.
- Stacked bar: risk_level by contract_display or has_tech_support_label.

## Page 4: Churn-Only Support
Purpose: support page for already churned customers only.
Visuals:
- KPI card: 83,362 churn-only customers.
- Bar chart: ChurnOnlyProfile category by percentage_of_churned_customers.
- Matrix: feature_display, category, churned_customers, percentage_of_churned_customers.
Important wording: use "Percentage of Churned Customers", not "Churn Rate", because this page uses churn-only data.

## Page 5: Model Evaluation
Purpose: report model quality.
Visuals:
- KPI cards from ModelMetrics: ROC AUC, Accuracy, Precision, Recall, F1.
- Matrix: ModelConfusionMatrix actual x predicted.
- Table: ModelSplitSummary.
"""
    (DOCS / "dashboard_blueprint.md").write_text(blueprint, encoding="utf-8")

    readme = """# DataVis Power BI Dashboard Pack

This folder contains cleaned Power BI-ready source tables for the customer churn dashboard.

Main version: overall.
Support version: churn_only.

Use Power BI Desktop -> Get Data -> Text/CSV and import the files from the data folder.
Then add the measures from docs/DAX_measures.dax and build pages following docs/dashboard_blueprint.md.

Dataset source note for the report:
The project uses a synthetic telecom customer churn dataset from Kaggle/Google Dataset Search. The clean file contains both churned and non-churned customers, while churn_only is used only as support profiling for already churned customers.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    mkdirs()
    make_overall_group_summary()
    make_churn_only_profile_summary()
    make_selected_customer_table()
    make_trend_table()
    make_metrics_tables()
    make_risk_tables()
    make_kpi_summary()
    write_docs()


if __name__ == "__main__":
    main()
