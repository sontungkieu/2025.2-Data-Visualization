# Kaggle Churn Model Comparison Summary

- Kernel: `kieutung/datavis-churn-model-comparison-20260612`
- Dataset: `kieutung/datavis-customer-churn-phase2-corr`
- Test rows: `126115`
- Test churn rate: `9.9148%`
- Main ranking metric: ROC-AUC, with PR-AUC/AP and F1 as supporting metrics.

| Rank | Model | Feature set | ROC-AUC | PR-AUC/AP | F1 | Precision | Recall | Accuracy | Balanced accuracy | Train seconds |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | CatBoost | raw+grouped | 0.688138 | 0.209795 | 0.268756 | 0.186733 | 0.479287 | 0.741411 | 0.624773 | 232.397 |
| 2 | XGBoost | raw+grouped | 0.685972 | 0.207431 | 0.267326 | 0.195722 | 0.421545 | 0.770900 | 0.615447 | 20.222 |
| 3 | LightGBM | raw+grouped | 0.685205 | 0.205119 | 0.266964 | 0.186566 | 0.469130 | 0.744566 | 0.622005 | 16.062 |
| 4 | RandomForest | raw+grouped | 0.683469 | 0.202672 | 0.266574 | 0.193693 | 0.427383 | 0.766832 | 0.615787 | 106.545 |
| 5 | RandomForest | grouped | 0.676510 | 0.192770 | 0.260651 | 0.186713 | 0.431542 | 0.757269 | 0.612330 | 42.486 |

## Interpretation

CatBoost is the best overall model by ROC-AUC, PR-AUC/AP, F1, recall, and balanced accuracy. XGBoost gives the best precision among the validation-threshold runs and is much faster than CatBoost. LightGBM is close to XGBoost and is the fastest boosting option. Adding raw numeric/categorical features to grouped features improves Random Forest over the grouped-only baseline.

The improvement over grouped Random Forest is real but moderate: ROC-AUC rises from `0.676510` to `0.688138`, and PR-AUC/AP rises from `0.192770` to `0.209795`. This suggests that model choice and raw features help, but the dataset still has limited single-customer signal.

Accuracy should not be the main conclusion because the test churn rate is only `9.9148%`. A trivial all-not-churn classifier would have high accuracy but zero recall for churn. Use ROC-AUC, PR-AUC/AP, F1, precision, recall, and balanced accuracy for the report.
