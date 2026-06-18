# DataVis 2025.2 - Customer Churn Dashboard

This project builds a Power BI dashboard for a customer churn dataset with two analysis versions:

- **overall**: main version, using the full dataset with churned and non-churned customers.
- **churn_only**: support version, using only churned customers for profiling and explanation.

The dashboard follows the course requirement: build a dashboard for a dataset that can be found through Google Dataset Search/Kaggle.

## Project Scope

### Phase 1: Descriptive Dashboard

Phase 1 focuses on Power BI visual analysis:

- total customers
- churned customers
- churn rate
- churn by contract, tenure, satisfaction, complaints, service calls, payments, services, and tech support
- churn-only customer profile

### Phase 2: Random Forest Prediction

Phase 2 uses the green-highlighted features from the provided datasheet.

Final **overall** model features:

- tenure
- contract
- customer_satisfaction
- num_complaints
- num_service_calls
- late_payments
- monthlycharges
- num_services
- has_tech_support

Final **churn_only** support features:

- Annual Income
- Education
- contract
- paperless_billing
- num_complaints
- num_service_calls
- late_payments
- monthlycharges

`churn_only` is not used to train a standalone classifier because it contains only churned customers. It supports the overall dashboard by profiling already churned customers.

Feature selection evidence from the Kaggle notebook ranks the Phase 2 feature
families as: `contract`, `customer_satisfaction`, `num_complaints`,
`num_service_calls`, `has_tech_support`, `late_payments`, `num_services`,
`tenure`, and `monthlycharges`. The first four are the strongest candidates
because they rank high in both churn-target correlation and Random Forest
importance. `avg_monthly_gb`, `days_since_last_interaction`, and `credit_score`
have very weak standalone churn correlations in the public source scan, so they
are better treated as dashboard context unless a later model proves interaction
value.

## Key Outputs

- Power BI final file: `dashboard_final.pbix`
- Power BI input workbook: `powerbi_dashboard/DataVis_PowerBI_Input.xlsx`
- Phase 2 pipeline: `phase2/phase2_pipeline.py`
- Phase 2 correlation outputs: `phase2_outputs/feature_selection/`
- Public-source feature selection notebook: `phase2/kaggle_feature_selection_kernel/`
- Power BI data pack scripts:
  - `powerbi_dashboard/build_powerbi_pack.py`
  - `powerbi_dashboard/build_powerbi_excel_input.py`
- Dashboard explanation/checklist:
  - `powerbi_dashboard/docs/final_project_explanation_vi.md`

## Model Result

Final Random Forest test metrics:

- ROC AUC: 0.676510
- Accuracy: 0.761694
- Precision: 0.187745
- Recall: 0.421945
- F1-score: 0.259863

Because the churn class is imbalanced, the model is used as a retention-priority tool rather than a perfect churn classifier.

## Recommended Dashboard Pages

1. **Overview** - high-level churn situation and main KPIs.
2. **Churn Drivers** - churn rate by feature category and Random Forest feature importance.
3. **Prediction** - high-risk customers and retention priority.
4. **Churn Only** - profile of already churned customers.
5. **Model Evaluation** - model metrics, confusion matrix, and train/validation/test split.

## Dataset Note

The raw dataset is not committed because it is large. The project uses a synthetic telecom/customer churn dataset available from Kaggle/Google Dataset Search. The compact Power BI workbook and summary tables are included for dashboard construction.

For Kaggle execution, note the dataset distinction:

- Original public source: `isandeep06/customer-churn-prediction-dataset-1m`.
- Private staging source: `minhhuyen3012nguyen/datavis-customer-churn-phase2`.

The private staging source stores the cleaned/split working files used by the
older Phase 2 kernel. If that private dataset is not accessible, use
`phase2/kaggle_feature_selection_kernel/feature_selection_phase2.ipynb`,
which loads the public source,
normalizes the schema, computes churn correlations, makes a reproducible
train/validation/test split, and runs the same Random Forest settings.
