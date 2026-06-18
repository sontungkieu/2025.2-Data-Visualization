# Distilled Data Visualization Knowledge

File này là bản cô đọng từ 10 bộ slide môn Data Visualization. Mục tiêu là
giữ lại các nguyên lý có thể dùng ngay khi viết report, đánh giá chart, hoặc
thiết kế dashboard churn.

## 1. Tư Duy Gốc

Visualization không phải là trang trí dữ liệu. Visualization là cách biến dữ
liệu thành hình ảnh để người đọc nhìn ra cấu trúc, so sánh, pattern, bất
thường, và quyết định hành động.

Một visualization tốt phải trả lời được ba câu hỏi:

- Người xem là ai?
- Họ cần biết hoặc làm gì sau khi xem?
- Chart này giúp họ thấy điều đó nhanh và đúng hơn bảng số liệu không?

Với bài toán churn, mục tiêu không chỉ là biết có bao nhiêu khách hàng churn.
Mục tiêu đúng hơn là tìm nhóm khách hàng nào có rủi ro cao hơn baseline và vì
sao nhóm đó đáng được ưu tiên retention.

## 2. Workflow Chuẩn Khi Thiết Kế Visualization

1. Xác định câu hỏi phân tích.
2. Xác định audience và hành động mong muốn.
3. Phân loại dữ liệu: nominal, ordinal, quantitative, time, spatial, network.
4. Chọn chart theo task: compare, distribution, proportion, relationship,
   trend, uncertainty.
5. Chọn encoding theo khả năng nhận thức của con người.
6. Thiết kế figure rõ ràng: title, label, caption, color, layout, baseline.
7. Kiểm tra chart có gây hiểu sai không.
8. Biến kết quả exploratory thành câu chuyện explanatory.

## 3. Phân Loại Dữ Liệu Và Cách Vẽ

| Loại dữ liệu | Ý nghĩa | Encoding/chart phù hợp | Lưu ý |
|---|---|---|---|
| Nominal | Nhóm không có thứ tự, ví dụ gender, contract type | Bar chart, grouped bar, color hue | Không sắp như số nếu category code chỉ là nhãn |
| Ordinal | Nhóm có thứ tự, ví dụ low-medium-high, satisfaction group | Ordered bar, heatmap có thứ tự | Luôn giữ thứ tự tự nhiên |
| Quantitative | Số đo, ví dụ monthly charges, GB usage, credit score | Histogram, box plot, scatter, line, binned bar | Không cắt nhóm tùy tiện nếu chưa giải thích |
| Proportion/rate | Tỷ lệ, ví dụ churn rate | Bar chart với baseline, 100% stacked nếu part-to-whole rõ | Luôn nói rõ mẫu số |
| Time/trend | Dữ liệu theo thời gian | Line chart, trend line, confidence band | Không dùng line nếu trục x không có thứ tự thời gian |
| Spatial | Có vị trí địa lý | Map, choropleth, symbol map | Cần normalize theo population/customer count |
| Network/graph | Có node-edge | Node-link, matrix, tree layout | Không dùng nếu dataset không có quan hệ thực |

## 4. Chọn Chart Theo Task

| Task | Chart nên dùng | Ví dụ trong churn |
|---|---|---|
| So sánh số lượng | Bar chart, grouped bar | Count churn/not churn theo satisfaction group |
| So sánh rủi ro | Bar chart rate + baseline line | Churn rate theo num complaints |
| Xem phân phối | Histogram, density, box plot | Phân phối credit score hoặc monthly charges |
| Xem tỷ trọng | Stacked bar, 100% stacked bar | Share churn/not churn trong một nhóm |
| Xem quan hệ | Scatter, heatmap, faceted chart | Satisfaction vs complaints theo churn |
| Xem xu hướng | Line chart | Churn rate theo thời gian nếu có date |
| Xem bất định | Error bar, confidence band | Model score hoặc trend có uncertainty |

Nguyên tắc quan trọng: chart churn rate theo từng group không cần cộng lại
100%. Mỗi bar là:

```text
churn rate of group = churned customers in group / total customers in group
```

Vì vậy, phải so từng group với baseline churn rate, không cộng các bar lại.

## 5. Visual Encoding: Gán Dữ Liệu Vào Hình Ảnh

Encoding là ánh xạ dữ liệu sang mark và channel.

- Mark: point, line, area, bar, text.
- Channel: position, length, size, color, shape, orientation, value.

Độ chính xác nhận thức thường tốt theo thứ tự:

1. Position trên cùng một scale.
2. Length.
3. Angle hoặc slope.
4. Area.
5. Volume.
6. Color saturation/value.

Vì vậy:

- Dùng bar/position/length cho so sánh churn rate.
- Tránh pie/donut nếu cần so sánh chính xác nhiều nhóm.
- Không dùng 3D bar/pie cho dữ liệu bảng vì dễ bóp méo perception.
- Color nên dùng để phân biệt hoặc highlight, không nên là cách duy nhất để
  truyền thông tin quan trọng.

## 6. Graphical Perception

Người đọc không xử lý hình ảnh như máy tính. Họ bị ảnh hưởng bởi:

- Preattentive features: màu nổi bật, kích thước, orientation, position.
- Gestalt principles: proximity, similarity, connectedness, enclosure.
- Khả năng ước lượng magnitude: position/length dễ so hơn area/angle.

Áp dụng cho dashboard churn:

- Đặt các chart liên quan gần nhau: count chart cạnh churn-rate chart.
- Dùng cùng màu cho churn/not churn trên toàn bộ report.
- Dùng baseline line để mắt người xem thấy nhóm nào vượt mức chung.
- Highlight high-risk group nhất quán, nhưng vẫn cần label/text để tránh phụ
  thuộc hoàn toàn vào màu.

## 7. Figure Design Rules

Checklist thiết kế figure:

- Bar chart nên bắt đầu từ zero khi encode amount/rate.
- Không dùng 3D nếu data không phải 3D.
- Không dùng màu chỉ để trang trí.
- Tránh rainbow color scale cho dữ liệu có thứ tự.
- Dùng colorblind-friendly palette.
- Title phải nói rõ câu hỏi hoặc insight.
- Caption nên giải thích metric, denominator, source, và assumption.
- Direct label tốt hơn legend xa chart khi có thể.
- Multi-panel nên giữ scale, color mapping, và layout nhất quán.
- Nếu có overlap trong scatter plot, dùng transparency, binning, sampling, hoặc
  facet.
- Bảng nên tối giản line, căn chỉnh số và header rõ ràng.

## 8. Good, Bad, Weird Visualization

Một chart xấu thường mắc một trong các lỗi:

- Sai scale hoặc trục không bắt đầu hợp lý.
- Dùng area/volume để thể hiện số liệu khiến người đọc ước lượng sai.
- Màu sắc làm nhiễu hoặc tạo thứ tự giả.
- Thiếu denominator cho percentage/rate.
- Chart đẹp nhưng không phục vụ câu hỏi phân tích.
- Dùng chart lạ khiến người xem phải học cách đọc trước khi hiểu dữ liệu.
- Nhồi quá nhiều thông tin vào một view.

Một chart tốt không nhất thiết phức tạp. Nó giúp người đọc trả lời câu hỏi đúng
nhanh hơn.

## 9. Storytelling With Data

EDA là tìm hiểu dữ liệu. Storytelling là chọn insight quan trọng và dẫn người
đọc đến hành động.

Narrative tốt nên đi theo mạch:

1. Context: vì sao churn quan trọng?
2. Baseline: churn rate chung là bao nhiêu?
3. Evidence: nhóm nào lệch baseline?
4. Explanation: feature nào giải thích rủi ro?
5. Action: nên ưu tiên retention cho nhóm nào?

Chart title nên chuyển từ mô tả chung sang message title khi số liệu đã chốt.

Ví dụ:

- Yếu: `Churn Rate by Satisfaction`
- Tốt hơn: `Low-satisfaction customers churn above the baseline`

## 10. Phần Liên Quan Trực Tiếp Đến Report Churn

Các chapter nên dùng trong report:

- Chapter 1: giải thích vai trò visualization trong churn analysis.
- Chapter 2: phân loại feature và giải thích visual encoding.
- Chapter 3: giải thích perception, baseline line, highlight, layout.
- Chapter 4: giải thích chart types cho table data: bar, histogram, rate chart,
  distribution, relationship.
- Chapter 6: giải thích figure design: color, label, title, proportional ink,
  no 3D.
- Chapter 8: giải thích interaction: filter, selection, view update.
- Chapter 9: giải thích storytelling: baseline -> evidence -> action.

Các chapter thường không cần hoặc chỉ nêu N/A:

- Chapter 5 Graph visualization: không dùng nếu dataset không có node-edge.
- Chapter 7 Map visualization: không dùng nếu dataset không có location.

## 11. Template Viết Technique Application

Dùng format này cho từng chart/page trong report:

```text
Chart/Page:
  [Tên chart hoặc page]

Technique / principle applied:
  [Chapter + nguyên lý, ví dụ: visual encoding, common baseline, color highlight]

How applied:
  [Feature nào được encode bằng trục nào, màu nào, mark nào, vì sao]

Notes / adjustments:
  [Giới hạn, lý do không dùng chart khác, hoặc điều cần tránh]
```

Ví dụ cho churn:

```text
Chart/Page:
  Churn rate by customer satisfaction group

Technique / principle applied:
  Chapter 2 visual encoding and Chapter 3 graphical perception.

How applied:
  Satisfaction groups are placed on the x-axis in ordinal order. Churn rate is
  encoded by bar length on a common y-axis. A baseline line shows the overall
  churn rate so above-baseline groups are immediately visible.

Notes / adjustments:
  The bars are within-group churn rates, so they are not expected to sum to
  100%. Color is used only as a highlight and should be supported by labels.
```

## 12. Churn Dashboard Minimal Design

Một dashboard churn tối thiểu nên có:

- KPI row: total customers, churn, not churn, baseline churn rate.
- Segment distribution: count churn/not churn theo từng feature group.
- Risk view: churn rate theo feature group + baseline line.
- Filter: contract, tenure, satisfaction, complaints, service calls, late
  payments.
- Insight panel: top high-risk groups và recommended actions.
- Model panel nếu cần: AUC, precision, recall, F1, top risk drivers.

Ưu tiên phân tích:

1. `customer_satisfaction`
2. `num_complaints`
3. `num_service_calls`
4. `late_payments`
5. `avg_monthly_gb`
6. `days_since_last_interaction`
7. `credit_score`

Nhóm 1-4 là customer-experience/payment behavior, thường có ý nghĩa hành động
rõ hơn. Nhóm 5-7 nên dùng như supporting variables, không kết luận mạnh nếu chỉ
xem đơn biến.

## 13. Report-Ready English Sentences

These sentences can be reused or adapted in the English report.

- The visualization design separates customer distribution from churn risk:
  counts explain segment size, while churn-rate charts explain risk inside each
  segment.
- Churn-rate bars are interpreted independently because each bar uses the
  customers in that group as its denominator.
- Position and bar length are used for churn-rate comparison because they are
  easier to decode accurately than area, angle, or volume.
- Color is used as a supporting highlight for high-risk groups, not as the only
  carrier of meaning.
- The overall churn rate is kept as a baseline reference so users can identify
  above-baseline and below-baseline segments quickly.
- Graph and map visualizations are not central to the current dataset because
  the data does not contain explicit network edges or geographic fields.
- The narrative structure moves from business context to baseline churn,
  feature-level evidence, model support, and retention recommendations.

## 14. Final Checklist Trước Khi Chốt Chart

- Chart có trả lời đúng câu hỏi không?
- Người xem có hiểu denominator của rate/percentage không?
- Axis, scale, baseline có gây hiểu sai không?
- Có dùng chart 3D, pie quá nhiều lát, hoặc màu rainbow không?
- Color có đủ thân thiện với color-vision deficiency không?
- Title có nói insight thay vì chỉ nói tên biến không?
- Count và churn rate đã được tách riêng chưa?
- Các nhóm category có được sắp theo thứ tự có nghĩa không?
- Có giải thích vì sao graph/map không dùng nếu không phù hợp không?
- Chart có dẫn đến hành động retention cụ thể không?
