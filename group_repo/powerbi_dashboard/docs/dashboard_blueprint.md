# Power BI Dashboard Blueprint

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
