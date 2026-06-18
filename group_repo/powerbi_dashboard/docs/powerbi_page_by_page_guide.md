# Power BI Page-by-Page Guide

## Before Building

Save the report first:

`File > Save as > DataVis_Churn_Dashboard.pbix`

Use these visual tools from the Visualizations pane:

- Card
- Line chart
- Clustered bar chart
- Donut chart
- Slicer
- Matrix
- Table

Use these data tables:

- `KPISummary`
- `OverallGroupSummary`
- `SignupTrend`
- `RiskLevelSummary`
- `RiskByFeature`
- `RiskTop5000`
- `ModelMetrics`
- `ConfusionMatrix`
- `SplitSummary`
- `FeatureImportance`
- `ChurnOnlyProfile`

## Page 1: Overview

Goal: show the overall business situation.

Rename page:

`Page 1 > Overview`

### Visual 1: Total Customers

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `Total Customers`

Title:

`Total Customers`

### Visual 2: Churned Customers

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `Churned Customers`

Title:

`Churned Customers`

### Visual 3: Overall Churn Rate

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `Overall Churn Rate`

Format:

- Display as percentage.

Title:

`Overall Churn Rate`

### Visual 4: High-risk Active Customers

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `High-risk Active Customers`

Title:

`High-risk Active Customers`

### Visual 5: Churn Rate Over Time

Tool: Line chart

Fields:

- X-axis: `SignupTrend[signup_month]`
- Y-axis: `SignupTrend[churn_rate_pct]`

Title:

`Churn Rate by Signup Month`

Format:

- Y-axis display units: None
- Y-axis title: `Churn Rate (%)`
- Data labels: On

### Visual 6: Customers by Risk Level

Tool: Donut chart or Clustered bar chart

Fields:

- Legend or Axis: `RiskLevelSummary[risk_level]`
- Values: `RiskLevelSummary[customers]`

Title:

`Active Customers by Risk Level`

### Visual 7: Driver Selector

Tool: Slicer

Field:

- `OverallGroupSummary[feature_display]`

Title:

`Select Churn Driver`

Use this slicer to control the next visual.

### Visual 8: Churn Rate by Selected Driver

Tool: Clustered bar chart

Fields:

- Y-axis: `OverallGroupSummary[category]`
- X-axis: `OverallGroupSummary[churn_rate_pct]`

Title:

`Churn Rate by Driver Group`

Format:

- Sort by `churn_rate_pct`, descending.
- Data labels: On.

## Page 2: Churn Drivers

Goal: explain which groups have higher churn.

Create new page:

`+ > rename to Churn Drivers`

### Visual 1: Feature Selector

Tool: Slicer

Field:

- `OverallGroupSummary[feature_display]`

Recommended default selected feature:

- `Contract Type`

Title:

`Feature`

### Visual 2: Churn Rate by Category

Tool: Clustered bar chart

Fields:

- Y-axis: `OverallGroupSummary[category]`
- X-axis: `OverallGroupSummary[churn_rate_pct]`

Title:

`Churn Rate by Category`

Format:

- Sort descending by `churn_rate_pct`.
- Data labels: On.
- X-axis title: `Churn Rate (%)`

### Visual 3: Customer Count by Category

Tool: Clustered bar chart

Fields:

- Y-axis: `OverallGroupSummary[category]`
- X-axis: `OverallGroupSummary[total_customers]`

Title:

`Total Customers by Category`

### Visual 4: Driver Detail Table

Tool: Matrix

Rows:

- `OverallGroupSummary[feature_display]`
- `OverallGroupSummary[category]`

Values:

- `OverallGroupSummary[total_customers]`
- `OverallGroupSummary[churned_customers]`
- `OverallGroupSummary[churn_rate_pct]`

Title:

`Churn Driver Detail`

### Visual 5: Model Feature Importance

Tool: Clustered bar chart

Fields:

- Y-axis: `FeatureImportance[feature_clean]`
- X-axis: `FeatureImportance[importance]`

Title:

`Random Forest Feature Importance`

Format:

- Sort descending by `importance`.
- Data labels: On.

## Page 3: Prediction

Goal: show which active customers are at risk.

Create new page:

`+ > rename to Prediction`

### Visual 1: Predicted Churn Customers

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `Medium-risk Active Customers`

Alternative:

- Use `RiskLevelSummary[predicted_churn]` if you want total predicted churn customers.

Title:

`Predicted Churn Customers`

### Visual 2: High Risk Customers

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `High-risk Active Customers`

Title:

`High Risk Customers`

### Visual 3: Average Churn Probability

Tool: Card

Field:

- `KPISummary[value]`

Filter this visual:

- `KPISummary[kpi]` is `Test ROC AUC`

Alternative:

- Use `RiskLevelSummary[avg_churn_probability_pct]` averaged by risk level if you want probability by customer risk.

Title:

`Model ROC AUC`

### Visual 4: Risk Level Distribution

Tool: Clustered bar chart

Fields:

- Axis: `RiskLevelSummary[risk_level]`
- Values: `RiskLevelSummary[customers]`

Title:

`Customers by Risk Level`

### Visual 5: Risk by Feature

Tool: Clustered bar chart

Fields:

- Y-axis: `RiskByFeature[category]`
- X-axis: `RiskByFeature[avg_churn_probability_pct]`

Slicer:

- `RiskByFeature[feature_display]`

Title:

`Average Churn Probability by Feature`

Format:

- Sort descending by `avg_churn_probability_pct`.
- Data labels: On.

### Visual 6: Top Risk Customers

Tool: Table

Fields:

- `RiskTop5000[customer_id]`
- `RiskTop5000[churn_probability]`
- `RiskTop5000[risk_level]`
- `RiskTop5000[contract_display]`
- `RiskTop5000[customer_satisfaction]`
- `RiskTop5000[num_service_calls]`
- `RiskTop5000[num_complaints]`
- `RiskTop5000[has_tech_support_label]`

Title:

`Top Customers at Risk`

Format:

- Sort descending by `churn_probability`.
- Conditional formatting on `churn_probability`: red for high values.

## Page 4: Churn-Only Support

Goal: support the main dashboard with profiling of customers who already churned.

Create new page:

`+ > rename to Churn-Only Support`

Important wording:

Use `Percentage of Churned Customers`, not `Churn Rate`.

### Visual 1: Feature Selector

Tool: Slicer

Field:

- `ChurnOnlyProfile[feature_display]`

Title:

`Churn-only Feature`

### Visual 2: Percentage of Churned Customers by Category

Tool: Clustered bar chart

Fields:

- Y-axis: `ChurnOnlyProfile[category]`
- X-axis: `ChurnOnlyProfile[percentage_of_churned_customers]`

Title:

`Percentage of Churned Customers by Category`

Format:

- Sort descending by `percentage_of_churned_customers`.
- Data labels: On.

### Visual 3: Churn-only Detail

Tool: Matrix

Rows:

- `ChurnOnlyProfile[feature_display]`
- `ChurnOnlyProfile[category]`

Values:

- `ChurnOnlyProfile[churned_customers]`
- `ChurnOnlyProfile[percentage_of_churned_customers]`

Title:

`Churn-only Profile Detail`

### Visual 4: Explanation Text

Tool: Text box

Text:

`This page uses churn_only data, which contains only customers who have already churned. It supports the overall dashboard by showing the distribution of churned customers, but it is not used as a standalone churn prediction model.`

## Page 5: Model Evaluation

Goal: show model quality and train/test split.

Create new page:

`+ > rename to Model Evaluation`

### Visual 1: Model Metrics Cards

Tool: Card

Create one card each using:

- `ModelMetrics[value]` filtered to `Test ROC AUC`
- `ModelMetrics[value]` filtered to `Test accuracy`
- `ModelMetrics[value]` filtered to `Test precision`
- `ModelMetrics[value]` filtered to `Test recall`
- `ModelMetrics[value]` filtered to `Test F1-score`

Titles:

- `ROC AUC`
- `Accuracy`
- `Precision`
- `Recall`
- `F1-score`

Format:

- Display as percentage.

### Visual 2: Confusion Matrix

Tool: Matrix

Rows:

- `ConfusionMatrix[actual]`

Columns:

- `ConfusionMatrix[predicted]`

Values:

- `ConfusionMatrix[customers]`

Title:

`Confusion Matrix`

### Visual 3: Split Summary

Tool: Table

Fields:

- `SplitSummary[split]`
- `SplitSummary[rows]`
- `SplitSummary[non_churn_0]`
- `SplitSummary[churn_1]`
- `SplitSummary[churn_pct]`

Title:

`Train / Validation / Test Split`

### Visual 4: Feature Importance

Tool: Clustered bar chart

Fields:

- Y-axis: `FeatureImportance[feature_clean]`
- X-axis: `FeatureImportance[importance]`

Title:

`Most Important Features`

## Recommended Layout Style

For every page:

- Put KPI cards at the top.
- Put slicers on the left or top-right.
- Put the largest chart in the center.
- Put matrix/table on the bottom.
- Use consistent colors:
  - Dark blue for neutral values.
  - Red for churn/high risk.
  - Green for low risk.

Suggested page size:

`Format page > Canvas settings > 16:9`
