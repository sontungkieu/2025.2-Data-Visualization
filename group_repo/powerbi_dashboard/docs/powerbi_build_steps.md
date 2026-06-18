# Power BI Build Steps

## 1. Import data
Open Power BI Desktop, then use Get Data > Text/CSV.

Import these files from `D:\DataVis\powerbi_dashboard\data`:

- `overall_customers_selected.csv`
- `overall_group_summary_long.csv`
- `overall_signup_month_trend.csv`
- `risk_top_5000_customers.csv`
- `risk_level_summary.csv`
- `risk_summary_by_feature.csv`
- `model_feature_importance.csv`
- `model_metrics_flat.csv`
- `model_confusion_matrix.csv`
- `model_split_summary.csv`
- `churn_only_profile_summary_long.csv`
- `kpi_summary.csv`

Rename tables to:

- `OverallCustomers`
- `OverallGroupSummary`
- `OverallSignupTrend`
- `RiskTopCustomers`
- `RiskLevelSummary`
- `RiskSummaryByFeature`
- `ModelFeatureImportance`
- `ModelMetrics`
- `ModelConfusionMatrix`
- `ModelSplitSummary`
- `ChurnOnlyProfile`
- `KPISummary`

## 2. Data type checks
Set these types:

- Counts: Whole number.
- Percent fields ending in `_pct`: Decimal number.
- Probability fields: Decimal number.
- `signup_month`: Text or Date. If Date is preferred, append `-01` in Power Query and convert to Date.

## 3. Add measures
Create a measure table or add measures to `OverallCustomers`.
Copy measures from `docs/DAX_measures.dax`.

Format:

- `Churn Rate` as percentage.
- `Average Churn Probability` as percentage.
- Customer count measures as whole numbers.

## 4. Build pages
Use `docs/dashboard_blueprint.md` as the page-by-page layout.

The main dashboard is the `overall` version. The `churn_only` page is support only and should use wording like "Percentage of Churned Customers", not "Churn Rate".

## 5. Suggested theme
Use a clean business dashboard style:

- Background: white or very light gray.
- Primary color: dark blue.
- Alert color: muted red for churn/high risk.
- Positive/low risk color: muted green.
- Use consistent card headers and avoid too many pie charts.
