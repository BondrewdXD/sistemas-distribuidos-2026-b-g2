# Incident Drill: Database Degradation

## Scenario
The PostgreSQL database (`medical_consultation` schema) responds in 3 seconds for 25% of the requests during 40 minutes.

## Trace of a slow request (Span Tree)
- [Root] POST /api/v1/consultations/attention (Gateway) - 3.2s
  - [Child] POST /api/consultations/attention (Consultation API) - 3.1s
    - [Child] INSERT attention_summaries (PostgreSQL) - 3.0s  <-- Bottleneck

## Log Lines
```json
{"timestamp":"2026-10-20T10:00:01Z","level":"INFO","service":"medical-consultation-api","trace_id":"abc","event":"request.received","message":"Processing attention"}
{"timestamp":"2026-10-20T10:00:02Z","level":"WARN","service":"medical-consultation-api","trace_id":"abc","event":"db.slow","message":"Query taking > 1s","duration_ms":2500}
{"timestamp":"2026-10-20T10:00:04Z","level":"ERROR","service":"medical-consultation-api","trace_id":"abc","event":"db.timeout","message":"Query timeout","duration_ms":3000}
{"timestamp":"2026-10-20T10:00:04Z","level":"ERROR","service":"api-gateway","trace_id":"abc","event":"request.failed","message":"504 Gateway Timeout"}
```