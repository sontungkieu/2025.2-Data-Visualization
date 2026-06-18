# Kaggle Churn Model Comparison

- Dataset: `/kaggle/input/datasets/kieutung/datavis-customer-churn-phase2-corr/customer_churn_dataset_clean.csv`
- Test churn rate: `0.099148`
- Train/validation/test rows: `588535` / `126115` / `126115`

## Ranked Results

| model_name | feature_set | roc_auc | average_precision | f1_selected | precision_selected | recall_selected | accuracy_selected | balanced_accuracy_selected | accuracy_at_0_5 | train_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CatBoost | raw+grouped | 0.688138 | 0.209795 | 0.268756 | 0.186733 | 0.479287 | 0.741411 | 0.624773 | 0.634278 | 232.397 |
| XGBoost | raw+grouped | 0.685972 | 0.207431 | 0.267326 | 0.195722 | 0.421545 | 0.7709 | 0.615447 | 0.637648 | 20.222 |
| LightGBM | raw+grouped | 0.685205 | 0.205119 | 0.266964 | 0.186566 | 0.46913 | 0.744566 | 0.622005 | 0.642525 | 16.062 |
| RandomForest | raw+grouped | 0.683469 | 0.202672 | 0.266574 | 0.193693 | 0.427383 | 0.766832 | 0.615787 | 0.693145 | 106.545 |
| RandomForest | grouped | 0.67651 | 0.19277 | 0.260651 | 0.186713 | 0.431542 | 0.757269 | 0.61233 | 0.607913 | 42.486 |

## Notes

- Threshold-dependent metrics use the threshold that maximizes F1 on the validation split.
- Accuracy is reported for reference only because the churn class is imbalanced.
- Average precision is PR-AUC/AP and is more informative than accuracy for this imbalanced binary task.