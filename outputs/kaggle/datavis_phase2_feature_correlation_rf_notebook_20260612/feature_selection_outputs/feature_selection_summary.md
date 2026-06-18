# Phase 2 Feature Selection: Correlation + Random Forest

- Source dataset file: `/kaggle/input/datasets/isandeep06/customer-churn-prediction-dataset-1m/customer_churn_1M.csv`
- Rows: 1,000,000
- Columns after normalization: 32
- Churn rate: 9.9227%
- Split: reproducible 70% train, 15% validation, 15% test with `random_state=42` and stratified churn.
- Algorithm: RandomForestClassifier with the same phase-2 settings: 200 trees, max_depth=12, min_samples_leaf=50, class_weight=balanced_subsample.

## Test Metrics at Validation-Selected Threshold

| threshold | accuracy | precision | recall | f1 | roc_auc | confusion_matrix |
| --- | --- | --- | --- | --- | --- | --- |
| 0.561498 | 0.726247 | 0.17732 | 0.483271 | 0.259446 | 0.675973 | [[101744, 33372], [7691, 7193]] |

## Top Encoded Features by Absolute Correlation with Churn

| encoded_feature | correlation_with_churn | abs_correlation_with_churn | feature_family |
| --- | --- | --- | --- |
| contract_two_year | -0.12396 | 0.12396 | contract |
| contract_one_year | 0.101061 | 0.101061 | contract |
| customer_satisfaction_group_satisfaction_1_3 | 0.080436 | 0.080436 | customer_satisfaction_group |
| contract_month_to_month | 0.079223 | 0.079223 | contract |
| num_complaints_group_complaints_gt_1 | 0.06492 | 0.06492 | num_complaints_group |
| customer_satisfaction_group_satisfaction_7_9 | -0.062483 | 0.062483 | customer_satisfaction_group |
| num_service_calls_group_service_calls_le_3 | -0.060786 | 0.060786 | num_service_calls_group |
| num_service_calls_group_service_calls_gt_3 | 0.060786 | 0.060786 | num_service_calls_group |
| num_complaints_group_complaints_le_1 | -0.060434 | 0.060434 | num_complaints_group |
| has_tech_support | -0.045477 | 0.045477 | has_tech_support |
| late_payments_group_late_0 | -0.041223 | 0.041223 | late_payments_group |
| late_payments_group_late_1_2 | 0.037382 | 0.037382 | late_payments_group |
| num_services_group_services_1_2 | 0.028274 | 0.028274 | num_services_group |
| num_services_group_services_5_6 | -0.022597 | 0.022597 | num_services_group |
| late_payments_group_late_3_plus | 0.021619 | 0.021619 | late_payments_group |
| num_services_group_services_3_4 | -0.014786 | 0.014786 | num_services_group |
| tenure_group_tenure_32_plus | -0.011372 | 0.011372 | tenure_group |
| tenure_group_tenure_1_6 | 0.009132 | 0.009132 | tenure_group |
| customer_satisfaction_group_satisfaction_4_6 | 0.004357 | 0.004357 | customer_satisfaction_group |
| tenure_group_tenure_7_15 | 0.002431 | 0.002431 | tenure_group |
| monthlycharges_group_monthly_ge_200 | 0.000198 | 0.000198 | monthlycharges_group |
| monthlycharges_group_monthly_lt_200 | -0.000198 | 0.000198 | monthlycharges_group |
| tenure_group_tenure_16_31 | 3.2e-05 | 3.2e-05 | tenure_group |

## Top Raw Numeric Features by Absolute Correlation with Churn

| raw_numeric_feature | correlation_with_churn |
| --- | --- |
| customer_satisfaction | -0.084749 |
| num_complaints | 0.079985 |
| num_service_calls | 0.077284 |
| late_payments | 0.047705 |
| has_tech_support | -0.045477 |
| has_online_security | -0.034106 |
| num_services | -0.033378 |
| totalcharges | -0.016501 |
| has_internet_service | -0.015261 |
| monthlycharges | -0.013849 |
| tenure | -0.012709 |
| avg_monthly_gb | -0.006144 |
| has_online_backup | -0.004919 |
| has_device_protection | -0.004908 |
| has_phone_service | -0.002274 |
| has_streaming_movies | 0.001915 |
| has_streaming_tv | 0.000695 |
| annual_income | 0.000466 |
| days_since_last_interaction | 0.000391 |
| credit_score | -0.000378 |
| senior_citizen | 0.000344 |
| age | 0.000264 |
| dependents | -0.000145 |

## Feature Family Correlation Summary

| feature_family | max_abs_correlation_with_churn | mean_abs_correlation_with_churn | top_encoded_feature | top_encoded_feature_correlation |
| --- | --- | --- | --- | --- |
| contract | 0.12396 | 0.101415 | contract_two_year | -0.12396 |
| customer_satisfaction_group | 0.080436 | 0.049092 | customer_satisfaction_group_satisfaction_1_3 | 0.080436 |
| num_complaints_group | 0.06492 | 0.062677 | num_complaints_group_complaints_gt_1 | 0.06492 |
| num_service_calls_group | 0.060786 | 0.060786 | num_service_calls_group_service_calls_le_3 | -0.060786 |
| has_tech_support | 0.045477 | 0.045477 | has_tech_support | -0.045477 |
| late_payments_group | 0.041223 | 0.033408 | late_payments_group_late_0 | -0.041223 |
| num_services_group | 0.028274 | 0.021886 | num_services_group_services_1_2 | 0.028274 |
| tenure_group | 0.011372 | 0.005742 | tenure_group_tenure_32_plus | -0.011372 |
| monthlycharges_group | 0.000198 | 0.000198 | monthlycharges_group_monthly_ge_200 | 0.000198 |

## Random Forest Feature Importance: Top Encoded Features

| encoded_feature | importance | feature_family |
| --- | --- | --- |
| contract_two_year | 0.28081045167593993 | contract |
| contract_one_year | 0.17318403222827933 | contract |
| customer_satisfaction_group_satisfaction_1_3 | 0.10418120046500491 | customer_satisfaction_group |
| contract_month_to_month | 0.0719608958528016 | contract |
| customer_satisfaction_group_satisfaction_7_9 | 0.06370925016188775 | customer_satisfaction_group |
| has_tech_support | 0.04793846680850483 | has_tech_support |
| num_complaints_group_complaints_gt_1 | 0.045618713396438346 | num_complaints_group |
| num_complaints_group_complaints_le_1 | 0.036205431837036665 | num_complaints_group |
| num_service_calls_group_service_calls_gt_3 | 0.032316188277056256 | num_service_calls_group |
| num_service_calls_group_service_calls_le_3 | 0.03050528073037 | num_service_calls_group |
| late_payments_group_late_0 | 0.024634242268845218 | late_payments_group |
| customer_satisfaction_group_satisfaction_4_6 | 0.019472498444505385 | customer_satisfaction_group |
| late_payments_group_late_1_2 | 0.01652725783217184 | late_payments_group |
| num_services_group_services_1_2 | 0.014865436922275984 | num_services_group |
| num_services_group_services_5_6 | 0.009431219718829901 | num_services_group |
| num_services_group_services_3_4 | 0.006862676829058632 | num_services_group |
| tenure_group_tenure_32_plus | 0.0049642494769352175 | tenure_group |
| tenure_group_tenure_1_6 | 0.004848483284884883 | tenure_group |
| tenure_group_tenure_7_15 | 0.0042151952464706925 | tenure_group |
| late_payments_group_late_3_plus | 0.004069474016263574 | late_payments_group |
| tenure_group_tenure_16_31 | 0.0036522942609537945 | tenure_group |
| monthlycharges_group_monthly_lt_200 | 1.6303587065327537e-05 | monthlycharges_group |
| monthlycharges_group_monthly_ge_200 | 1.0756678420062925e-05 | monthlycharges_group |

## Recommended Feature Families

| feature_family | max_abs_correlation_with_churn | mean_abs_correlation_with_churn | top_encoded_feature | top_encoded_feature_correlation | total_importance | max_importance | correlation_rank | importance_rank | combined_rank_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| contract | 0.12396 | 0.101415 | contract_two_year | -0.12396 | 0.5259553797570209 | 0.28081045167593993 | 1.0 | 1.0 | 2.0 |
| customer_satisfaction_group | 0.080436 | 0.049092 | customer_satisfaction_group_satisfaction_1_3 | 0.080436 | 0.18736294907139805 | 0.10418120046500491 | 2.0 | 2.0 | 4.0 |
| num_complaints_group | 0.06492 | 0.062677 | num_complaints_group_complaints_gt_1 | 0.06492 | 0.081824145233475 | 0.045618713396438346 | 3.0 | 3.0 | 6.0 |
| num_service_calls_group | 0.060786 | 0.060786 | num_service_calls_group_service_calls_le_3 | -0.060786 | 0.06282146900742626 | 0.032316188277056256 | 4.0 | 4.0 | 8.0 |
| has_tech_support | 0.045477 | 0.045477 | has_tech_support | -0.045477 | 0.04793846680850483 | 0.04793846680850483 | 5.0 | 5.0 | 10.0 |
| late_payments_group | 0.041223 | 0.033408 | late_payments_group_late_0 | -0.041223 | 0.04523097411728063 | 0.024634242268845218 | 6.0 | 6.0 | 12.0 |
| num_services_group | 0.028274 | 0.021886 | num_services_group_services_1_2 | 0.028274 | 0.031159333470164516 | 0.014865436922275984 | 7.0 | 7.0 | 14.0 |
| tenure_group | 0.011372 | 0.005742 | tenure_group_tenure_32_plus | -0.011372 | 0.017680222269244587 | 0.0049642494769352175 | 8.0 | 8.0 | 16.0 |
| monthlycharges_group | 0.000198 | 0.000198 | monthlycharges_group_monthly_ge_200 | 0.000198 | 2.7060265485390462e-05 | 1.6303587065327537e-05 | 9.0 | 9.0 | 18.0 |

## Interpretation Rule

Correlation is used as a univariate screening signal. Random Forest importance is used as a model-based signal. Feature families that score high on both are the strongest candidates for phase 2.
