# Kaggle All-Feature Churn Model Summary

- Kernel: `kieutung/datavis-all-feature-churn-models-20260612`
- Status: `COMPLETE`
- Dataset: `kieutung/datavis-customer-churn-phase2-corr`
- Feature set: `all_features_engineered`
- Total engineered features: `98` (`69` numeric, `29` categorical)
- Split: `588535` train / `126115` validation / `126115` test
- Test churn rate: `9.9148%`

| Rank | Model | ROC-AUC | PR-AUC/AP | F1 | Precision | Recall | Accuracy | Balanced accuracy | Train seconds |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | CatBoost | 0.687579 | 0.208972 | 0.269713 | 0.190582 | 0.461212 | 0.752369 | 0.622813 | 714.097 |
| 2 | XGBoost | 0.685814 | 0.207655 | 0.267877 | 0.189749 | 0.455374 | 0.753209 | 0.620682 | 97.003 |
| 3 | LightGBM | 0.683223 | 0.204742 | 0.267263 | 0.193930 | 0.429782 | 0.766348 | 0.616586 | 51.726 |
| 4 | RandomForest | 0.682496 | 0.203125 | 0.264052 | 0.187681 | 0.445218 | 0.753939 | 0.616567 | 214.499 |
| 5 | ExtraTrees | 0.681263 | 0.198967 | 0.264402 | 0.184245 | 0.468010 | 0.741807 | 0.619976 | 321.211 |

## Interpretation

The all-feature engineered run completed successfully, but it does not beat the previous raw+grouped CatBoost run on ROC-AUC or PR-AUC. It slightly improves F1 over the previous best (`0.269713` vs `0.268756`) and gives CatBoost the best all-feature result.

Compared with the previous raw+grouped comparison, the extra engineered features add complexity but only marginal performance. The most practical model remains XGBoost or LightGBM when speed matters, and CatBoost when the report emphasizes the best F1/ROC-AUC result.
