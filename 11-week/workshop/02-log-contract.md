# Structured Log Contract

## Fields Table
| Name | Type | Required | Example | Why |
|---|---|---|---|---|
| timestamp | string | Yes | 2026-10-19T14:02:11.482Z | ISO-8601 UTC |
| level | string | Yes | ERROR | Severity |
| service | string | Yes | medical-consultation-api | Origin |
| version | string | Yes | 1.0.0 | Deployment tracking |
| environment | string | Yes | dev | Context |
| trace_id | string | Yes | 4bf92f3577b34da6a3ce929d0e0e4736 | Trace correlation |
| span_id | string | Yes | 00f067aa0ba902b7 | Span correlation |
| correlation_id | string | Yes | req-88121 | Business correlation |
| event | string | Yes | attention.created | Action name |
| message | string | Yes | Attention registered | Human readable |
| duration_ms | number | Yes | 45 | Performance |
| patient_id | number | No | 1001 | Domain field |
| appointment_id | number | No | 5 | Domain field |
| professional_id | number | No | 2 | Domain field |
| diagnosis_code | string | No | J11 | Domain field |

## Never Log (Masking)
- Passwords: NEVER.
- JWT Tokens: NEVER.
- Patient Health Data (Symptoms, Diagnosis details): MASK as `[REDACTED_HEALTH_DATA]`.

## Log Levels
- ERROR: Database connection failed.
- WARN: High latency (duration_ms > 1000).
- INFO: Attention created successfully (id=202).
- DEBUG: Incoming payload (masked).

## 7 Example Logs (Same trace_id)
```json
{"timestamp":"2026-10-19T14:00:01.000Z","level":"INFO","service":"api-gateway","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"1a2b3c","correlation_id":"req-1","event":"request.received","message":"POST /attention","duration_ms":0}
{"timestamp":"2026-10-19T14:00:01.050Z","level":"INFO","service":"medical-consultation-api","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"4d5e6f","correlation_id":"req-1","event":"request.received","message":"Processing attention","duration_ms":0}
{"timestamp":"2026-10-19T14:00:01.080Z","level":"DEBUG","service":"medical-consultation-api","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"4d5e6f","correlation_id":"req-1","event":"db.query","message":"INSERT attention","duration_ms":30}
{"timestamp":"2026-10-19T14:00:01.090Z","level":"WARN","service":"medical-consultation-api","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"4d5e6f","correlation_id":"req-1","event":"db.slow","message":"Query took too long","duration_ms":450,"appointment_id":5}
{"timestamp":"2026-10-19T14:00:03.100Z","level":"ERROR","service":"medical-consultation-api","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"4d5e6f","correlation_id":"req-1","event":"db.timeout","message":"Connection timeout","duration_ms":3000,"appointment_id":5}
{"timestamp":"2026-10-19T14:00:03.200Z","level":"ERROR","service":"api-gateway","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"1a2b3c","correlation_id":"req-1","event":"request.failed","message":"Downstream timeout","duration_ms":3200}
{"timestamp":"2026-10-19T14:00:03.300Z","level":"INFO","service":"api-gateway","version":"2.0.0","environment":"dev","trace_id":"4bf92f35","span_id":"1a2b3c","correlation_id":"req-1","event":"request.returned","message":"500 Internal Server Error","duration_ms":3300}
```