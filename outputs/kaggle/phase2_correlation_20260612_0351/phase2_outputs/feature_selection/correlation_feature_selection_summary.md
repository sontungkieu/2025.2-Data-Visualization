# Phase 2 Correlation-Based Feature Selection

This analysis uses the full overall dataset after phase-2 feature grouping and one-hot encoding.
Correlation is a univariate screening signal, not a final model-selection rule.
It should be interpreted together with Random Forest feature importance and business actionability.

## Top Encoded Features by Absolute Correlation with Churn

| encoded_feature | correlation_with_churn | abs_correlation_with_churn | feature_family |
| --- | --- | --- | --- |
| contract_two_year | -0.123686 | 0.123686 | contract |
| contract_one_year | 0.100979 | 0.100979 | contract |
| customer_satisfaction_group_satisfaction_1_3 | 0.080981 | 0.080981 | customer_satisfaction_group |
| contract_month_to_month | 0.078836 | 0.078836 | contract |
| num_complaints_group_complaints_le_1 | -0.066236 | 0.066236 | num_complaints_group |
| num_complaints_group_complaints_gt_1 | 0.066236 | 0.066236 | num_complaints_group |
| customer_satisfaction_group_satisfaction_7_9 | -0.063678 | 0.063678 | customer_satisfaction_group |
| num_service_calls_group_service_calls_le_3 | -0.060627 | 0.060627 | num_service_calls_group |
| num_service_calls_group_service_calls_gt_3 | 0.060627 | 0.060627 | num_service_calls_group |
| has_tech_support | -0.045187 | 0.045187 | has_tech_support |
| late_payments_group_late_0 | -0.041126 | 0.041126 | late_payments_group |
| late_payments_group_late_1_2 | 0.037129 | 0.037129 | late_payments_group |
| num_services_group_services_1_2 | 0.027798 | 0.027798 | num_services_group |
| num_services_group_services_5_6 | -0.022531 | 0.022531 | num_services_group |
| late_payments_group_late_3_plus | 0.022395 | 0.022395 | late_payments_group |
| num_services_group_services_3_4 | -0.014326 | 0.014326 | num_services_group |
| tenure_group_tenure_32_plus | -0.011551 | 0.011551 | tenure_group |
| tenure_group_tenure_1_6 | 0.008935 | 0.008935 | tenure_group |
| customer_satisfaction_group_satisfaction_4_6 | 0.004526 | 0.004526 | customer_satisfaction_group |
| tenure_group_tenure_7_15 | 0.002469 | 0.002469 | tenure_group |

## Feature Family Summary

| feature_family | max_abs_correlation_with_churn | mean_abs_correlation_with_churn | top_encoded_feature | top_encoded_feature_correlation |
| --- | --- | --- | --- | --- |
| contract | 0.123686 | 0.101167 | contract_two_year | -0.123686 |
| customer_satisfaction_group | 0.080981 | 0.049728 | customer_satisfaction_group_satisfaction_1_3 | 0.080981 |
| num_complaints_group | 0.066236 | 0.066236 | num_complaints_group_complaints_le_1 | -0.066236 |
| num_service_calls_group | 0.060627 | 0.060627 | num_service_calls_group_service_calls_le_3 | -0.060627 |
| has_tech_support | 0.045187 | 0.045187 | has_tech_support | -0.045187 |
| late_payments_group | 0.041126 | 0.03355 | late_payments_group_late_0 | -0.041126 |
| num_services_group | 0.027798 | 0.021552 | num_services_group_services_1_2 | 0.027798 |
| tenure_group | 0.011551 | 0.005833 | tenure_group_tenure_32_plus | -0.011551 |
| monthlycharges_group | 5e-05 | 5e-05 | monthlycharges_group_monthly_ge_200 | -5e-05 |

## Churn-Only Note

`customer_churn_only.csv` contains only churned customers, so correlation with the churn target is undefined.
Use churn-only outputs for customer profiling, not for selecting binary churn classifier features.
