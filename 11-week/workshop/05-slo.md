# SLOs and Error Budget

## Service Level Objectives (SLOs)
| SLI | Formula | PromQL | Target | Window |
|---|---|---|---|---|
| **Availability** | Good Requests / Total Requests | `sum(rate(consultation_requests_total{outcome="success"}[5m])) / sum(rate(consultation_requests_total[5m]))` | 99.5% | 30 days |
| **Latency** | Requests < 300ms / Total Requests | `sum(rate(consultation_request_duration_seconds_bucket{le="0.3"}[5m])) / sum(rate(consultation_request_duration_seconds_count[5m]))` | 95% | 7 days |
| **Quality (Attendance Saved)** | Successful DB Inserts / Total Attempts | `sum(rate(consultation_requests_total{outcome="success"}[5m])) / sum(rate(consultation_requests_total[5m]))` | 99.9% | 30 days |

## Traffic Estimation
Based on the TeleMed IA scope, we estimate **10,000 requests per day** (medical consultations). 
For a 30-day window: 300,000 requests.

## Error Budget Calculation (Availability SLO: 99.5%)
- **Budget percentage:** 0.5%
- **Budget in requests:** 0.5% of 300,000 = **1,500 failed requests per month**.
- **Budget in minutes:** 30 days = 43,200 minutes. 0.5% of 43,200 = **216 minutes of total downtime**.

## Error Budget Policy
- **At 50% consumed:** We investigate the root cause but continue deploying new features.
- **At 75% consumed:** Feature freeze. We prioritize reliability tasks and bug fixes.
- **At 100% consumed:** Complete freeze. We only deploy hotfixes until the error budget is replenished.