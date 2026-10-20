# Runbook: Fast Burn Rate Alert (Consultation API)

## Symptoms
The `HighErrorBurnRate_Fast` alert triggers, indicating a high rate of 5xx errors or timeouts in the `medical-consultation-api`.

## Confirmation
1. Check the PromQL dashboard: `sum(rate(consultation_requests_total{outcome="error"}[5m]))`
2. Search logs for the failing traces: `trace_id: "..." AND level: "ERROR"`

## Mitigations (Ordered by risk)
1. **Rollback:** If a recent deployment caused the issue, revert to the previous stable version (`git revert`).
2. **Circuit Breaker:** Enable the circuit breaker to stop sending requests to the failing database, returning a graceful 503 error.
3. **Scale Out:** If the database is overloaded, increase the connection pool limit or scale the Postgres instance.

## Escalation
- L1: On-call Developer (check logs and apply rollback).
- L2: Jose Miguel Vera (Database expert).
- L3: Jesus Gonzalez (Architecture / Infrastructure).

## Recovery Verification
Confirm that the error rate drops below 0.5% and the burn rate alert resolves automatically in Prometheus.