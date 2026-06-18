# Kaggle Churn All-Feature Model Comparison

- Dataset: `/kaggle/input/datasets/kieutung/datavis-customer-churn-phase2-corr/customer_churn_dataset_clean.csv`
- Feature set: `all_features_engineered`
- Total features after engineering: `98`
- Numeric features: `69`
- Categorical features: `29`
- Test churn rate: `0.099148`
- Train/validation/test rows: `588535` / `126115` / `126115`

## Ranked Results

| model_name | feature_set | roc_auc | average_precision | f1_selected | precision_selected | recall_selected | accuracy_selected | balanced_accuracy_selected | accuracy_at_0_5 | train_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CatBoost | all_features_engineered | 0.687579 | 0.208972 | 0.269713 | 0.190582 | 0.461212 | 0.752369 | 0.622813 | 0.635975 | 714.097 |
| XGBoost | all_features_engineered | 0.685814 | 0.207655 | 0.267877 | 0.189749 | 0.455374 | 0.753209 | 0.620682 | 0.641312 | 97.003 |
| LightGBM | all_features_engineered | 0.683223 | 0.204742 | 0.267263 | 0.19393 | 0.429782 | 0.766348 | 0.616586 | 0.656401 | 51.726 |
| RandomForest | all_features_engineered | 0.682496 | 0.203125 | 0.264052 | 0.187681 | 0.445218 | 0.753939 | 0.616567 | 0.708853 | 214.499 |
| ExtraTrees | all_features_engineered | 0.681263 | 0.198967 | 0.264402 | 0.184245 | 0.46801 | 0.741807 | 0.619976 | 0.669984 | 321.211 |

## Notes

- Threshold-dependent metrics use the threshold that maximizes F1 on the validation split.
- Accuracy is reported for reference only because the churn class is imbalanced.
- Average precision is PR-AUC/AP and is more informative than accuracy for this imbalanced binary task.
- `signup_date` is represented through time-derived features rather than a raw high-cardinality timestamp.