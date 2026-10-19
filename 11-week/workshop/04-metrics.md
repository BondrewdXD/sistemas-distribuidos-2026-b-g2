# Metric Catalog (Medical Consultation API)

| Signal | Metric Name | Type | Labels | PromQL |
|---|---|---|---|---|
| Latency | `consultation_request_duration_seconds` | Histogram | `route`, `method` | `histogram_quantile(0.95, sum by (le) (rate(consultation_request_duration_seconds_bucket[5m])))` |
| Errors | `consultation_requests_total` | Counter | `outcome` | `sum(rate(consultation_requests_total{outcome="error"}[5m]))` |
| Traffic | `consultation_requests_total` | Counter | `route` | `sum(rate(consultation_requests_total[5m]))` |
| Saturation | `process_cpu_seconds_total` | Counter | (none) | `rate(process_cpu_seconds_total[5m])` |

**Cardinality:** We forbid `user_id` and `patient_id` as labels to avoid cardinality explosion. Replaced by `route` or `outcome`.
**Histogram Buckets:** `[0.1, 0.3, 0.5, 1.0, 2.0]` (Users expect medical records to load in under 1 second).