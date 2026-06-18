# Kaggle Phase 2 Correlation Result Summary

- Kernel: `kieutung/datavis-phase-2-correlation-and-random-forest`
- Dataset used for execution: `kieutung/datavis-customer-churn-phase2-corr`
- Original report source dataset: `isandeep06/customer-churn-prediction-dataset-1m`
- Note: the execution dataset is a private Kaggle staging copy of the cleaned/split files, not the same slug as the public source dataset.

## Model Metrics at Selected Threshold

- roc_auc: 0.67651
- accuracy: 0.757269
- precision: 0.186713
- recall: 0.431542
- f1: 0.260651
- threshold: 0.5716

## Feature Family Ranking

| Rank | Feature family | Max abs corr with churn | Mean abs corr | RF importance sum | Top encoded feature | Top encoded corr |
|---:|---|---:|---:|---:|---|---:|
| 1 | contract | 0.123686 | 0.101167 | 0.524498 | contract_two_year | -0.123686 |
| 2 | customer_satisfaction_group | 0.080981 | 0.049728 | 0.183078 | customer_satisfaction_group_satisfaction_1_3 | 0.080981 |
| 3 | num_complaints_group | 0.066236 | 0.066236 | 0.087888 | num_complaints_group_complaints_le_1 | -0.066236 |
| 4 | num_service_calls_group | 0.060627 | 0.060627 | 0.055279 | num_service_calls_group_service_calls_le_3 | -0.060627 |
| 5 | has_tech_support | 0.045187 | 0.045187 | 0.048740 | has_tech_support | -0.045187 |
| 6 | late_payments_group | 0.041126 | 0.033550 | 0.047911 | late_payments_group_late_0 | -0.041126 |
| 7 | num_services_group | 0.027798 | 0.021552 | 0.032838 | num_services_group_services_1_2 | 0.027798 |
| 8 | tenure_group | 0.011551 | 0.005833 | 0.019722 | tenure_group_tenure_32_plus | -0.011551 |
| 9 | monthlycharges_group | 0.000050 | 0.000050 | 0.000047 | monthlycharges_group_monthly_ge_200 | -0.000050 |

## Recommended Phase 2 Feature Set

- `contract`
- `customer_satisfaction_group`
- `num_complaints_group`
- `num_service_calls_group`
- `has_tech_support`
- `late_payments_group`
- `num_services_group`

Features to treat as weak/supporting from this run:
- `tenure_group`
- `monthlycharges_group`

`churn_only` contains only churned customers, so target correlation with churn is undefined there. Use churn-only files for profiling, not binary feature selection.
