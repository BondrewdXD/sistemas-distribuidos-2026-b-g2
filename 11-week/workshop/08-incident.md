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

## Impact and Alert
* **SLI:** Latency SLI drops to 75% (below the 95% threshold).

* **Alert:** HighErrorBurnRate_Fast fires at minute 5.

* **Runbook step:** Mitigation #2 (Circuit Breaker) stops the bleeding while the DBA investigates.

## Blameless Postmortem
* **Timeline:** 10:00 Degradation starts. 10:05 Alert fires. 10:10 Circuit breaker activated. 10:40 DB lock resolved.

* **Impact:** 2,000 requests affected. 10% of the monthly error budget consumed.

* **Root Cause:** A missing index on the appointment_id column caused full table scans when the table grew past 100k rows.

* **Action Items:**

1. Add index on appointment_id (Acceptance: Query time < 50ms).
2. Implement query timeout of 1s in the Python adapter (Acceptance: Requests fail fast, no 3s hangs).