# DataVis Power BI Dashboard Pack

This folder contains cleaned Power BI-ready source tables for the customer churn dashboard.

Main version: overall.
Support version: churn_only.

Main Power BI input workbook:
`D:\DataVis\powerbi_dashboard\DataVis_PowerBI_Input.xlsx`

Use Power BI Desktop -> Get Data -> Excel workbook and import this workbook.
Then add the measures from docs/DAX_measures.dax and build pages following docs/dashboard_blueprint.md.

Final Vietnamese explanation and submission checklist:
`D:\DataVis\powerbi_dashboard\docs\final_project_explanation_vi.md`

Final Phase 2 feature scope:
- overall: tenure, contract, customer_satisfaction, num_complaints, num_service_calls, late_payments, monthlycharges, num_services, has_tech_support.
- churn_only: Annual Income, Education, contract, paperless_billing, num_complaints, num_service_calls, late_payments, monthlycharges.

Dataset source note for the report:
The project uses a synthetic telecom customer churn dataset from Kaggle/Google Dataset Search. The clean file contains both churned and non-churned customers, while churn_only is used only as support profiling for already churned customers.
