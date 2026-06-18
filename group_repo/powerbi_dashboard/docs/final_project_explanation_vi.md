# Giai thich project Customer Churn Dashboard

## 1. Muc tieu project

Project nay xay dung dashboard cho bai toan Customer Churn trong linh vuc telecom/customer subscription.

Muc tieu chinh:

- Hieu tinh hinh churn cua toan bo tap khach hang.
- Tim cac nhom khach hang co churn rate cao.
- Dung cac feature duoc boi xanh trong file Excel de lam phan Phase 2.
- Dua ket qua Random Forest vao Power BI de dashboard co them goc nhin prediction/risk.
- Dung tap churn_only de ho tro phan tich rieng nhom khach da churn.

## 2. Du lieu su dung

File du lieu chinh:

- `customer_churn_dataset_clean.csv`: tap overall, gom ca khach churn va khong churn.
- `customer_churn_only.csv`: tap churn_only, chi gom khach da churn.
- `DATA VISUALIZATION.xlsx`: datasheet danh dau feature mau xanh dung cho Phase 2.

Dataset source can neu trong report:

- Synthetic telecom/customer churn dataset tu Kaggle.
- Dataset co the tim qua Google Dataset Search/Kaggle.

## 3. Phase 1 la gi?

Phase 1 la phan dashboard mo ta du lieu.

Phase 1 tra loi:

- Tong so khach hang la bao nhieu?
- Bao nhieu khach da churn?
- Churn rate la bao nhieu?
- Churn rate thay doi theo nhom nao?
- Nhom contract, tenure, monthly charges, complaints, service calls co lien quan gi den churn?

Trong Power BI, Phase 1 tuong ung voi cac page:

- Overview.
- Churn Drivers.
- Churn-Only Support.

## 4. Phase 2 la gi?

Phase 2 la phan phan tich nang cao bang machine learning.

Phase 2 dung Random Forest de:

- Train model du doan churn tren tap overall.
- Tao feature importance.
- Tao confusion matrix va model metrics.
- Tao churn probability/risk level cho khach hang active/non-churn.
- Ho tro dashboard Prediction/Retention Priority.

Important:

- Overall co ca churn = 0 va churn = 1, nen co the train binary classifier.
- Churn_only chi co churn = 1, nen khong train classifier rieng tren churn_only.
- Churn_only chi dung de profiling va support insight cho overall.

## 5. Feature Phase 2 da chot theo Excel

Overall dung 9 feature boi xanh:

- tenure
- contract
- customer_satisfaction
- num_complaints
- num_service_calls
- late_payments
- monthlycharges
- num_services
- has_tech_support

Churn_only dung 8 feature boi xanh:

- Annual Income
- Education
- contract
- paperless_billing
- num_complaints
- num_service_calls
- late_payments
- monthlycharges

## 6. Ket qua Phase 2 final hien tai

Random Forest da duoc rerun voi feature list dung theo Excel.

Metric tren test set:

- Selected threshold: 0.571637
- ROC AUC: 0.676510
- Accuracy: 0.761694
- Precision: 0.187745
- Recall: 0.421945
- F1-score: 0.259863
- Confusion matrix: [[90785, 22826], [7228, 5276]]

Giai thich ngan:

- ROC AUC khoang 0.676 cho thay model co kha nang phan biet churn/non-churn o muc trung binh.
- Recall khoang 42.2% nghia la model bat duoc gan mot nua so khach churn that.
- Precision thap vi bai toan churn bi imbalance: ti le churn trong tap du lieu chi khoang 9.9%.
- Dashboard nen dung model nhu mot cong cu uu tien retention, khong nen noi model du doan hoan hao.

## 7. File Power BI can dung

File input final:

`D:\DataVis\powerbi_dashboard\DataVis_PowerBI_Input.xlsx`

Import file nay vao Power BI Desktop bang:

Home > Get data > Excel workbook

Sau do load tat ca sheet can dung.

## 8. Cac page dashboard nen hoan thien

### Page 1: Overview

Muc dich: cho nguoi xem nam tinh hinh tong quan.

Visual can co:

- KPI cards: Total Customers, Churned Customers, Churn Rate, High Risk Customers.
- Line chart: Churn Rate by Signup Month.
- Bar chart: Customers by Risk Level.
- Bar chart: Churn Rate by selected feature/category.

### Page 2: Churn Drivers

Muc dich: giai thich yeu to nao lien quan den churn.

Visual can co:

- Bar chart: churn_rate_pct theo category.
- Slicer: feature_display.
- Matrix: feature_display, category, total_customers, churned_customers, churn_rate_pct.
- Bar chart: FeatureImportance.

### Page 3: Prediction and Retention Priority

Muc dich: dung output model de uu tien cham soc khach hang.

Visual can co:

- KPI cards: Predicted Churn Customers, High Risk Customers, Average Churn Probability.
- Table: RiskTop5000.
- Bar chart: avg_churn_probability_pct by feature/category.
- Stacked bar: risk_level by contract/tech support/service calls.

### Page 4: Churn-Only Support

Muc dich: phan tich rieng nhom khach da churn.

Visual can co:

- KPI card: Churn-Only Customers.
- Bar chart: percentage_of_churned_customers by category.
- Matrix: feature_display, category, churned_customers, percentage_of_churned_customers.

Luu y: page nay khong goi la churn rate, vi mau so chi gom khach churn. Dung cach noi "Percentage of Churned Customers".

### Page 5: Model Evaluation

Muc dich: bao cao chat luong model.

Visual can co:

- KPI cards: ROC AUC, Accuracy, Precision, Recall, F1.
- Matrix: ConfusionMatrix.
- Table: SplitSummary.

## 9. Checklist truoc khi nop

- Power BI file co it nhat 4-5 page nhu tren.
- Co neu source dataset la Kaggle/Google Dataset Search.
- Co giai thich Phase 1 va Phase 2.
- Co noi ro overall la main version.
- Co noi ro churn_only la support version, khong train model rieng.
- Dashboard co model metrics va feature importance.
- Dashboard co risk/high-risk customer insight.
- Cac chart dung dung wording: churn_only page khong dung "churn rate".

