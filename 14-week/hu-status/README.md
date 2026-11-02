<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       14-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 14

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: telemed-ia
- SPRINT_GOAL: Finalize the HU-18 real reminders, simplify the Appointment API contract (auto-calculate end time), and fix Docker/Gateway routing for the E2E demo.
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| HU-018 | Worker: Fetch real upcoming appointments | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api/pull/21 |
| HU-020 | Simplify Appointment Booking (Remove End Time) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api/pull/23 |
| INFRA-002 | Fix Gateway upstreams and Docker compose variables | done | https://github.com/code-corhuila/telemed-ia-api-gateway/pull/8 |

## 2. My individual contribution
- **HU-18 Completion:** Added the `/api/appointments/internal/reminders` endpoint to the Python API and updated the Java Worker to consume real appointments, generating deterministic `eventId`s and `correlationId`s to ensure idempotency.
- **API Contract Simplification:** Refactored the Appointment API and Angular Portal to remove the `endDateTime` from the public forms. The API now calculates `end = start + 30 minutes` internally, preserving database exclusion constraints while simplifying the patient UX.
- **Infrastructure & Docker:** Fixed the Gateway NGINX configuration to route to `appointment-scheduling-api` and `medical-consultation-api`. Added missing `RABBITMQ_URL` variables to the compose files and removed default `guest/guest` credentials from the Worker.
- **Testing:** Ensured all unit tests pass (`pytest` and `mvn clean package`) after the Outbox and UUID migrations.

## 3. Blockers and risks
- **None remaining.** The asynchronous flow from consultation completion to PDF generation and appointment reminders is fully implemented and tested in Docker.

## 4. Plan for next week
- Final presentation preparation.
- Monitor Grafana dashboards for any runtime anomalies during the demo.

## 5. Compliance self-check
- [X] Conventional Commits - `type(scope): summary`
- [X] Per-environment HU branch + PR to that environment (hu-xxx-dev -> develop, ...)
- [X] Testable acceptance criteria
- [X] Tests added/updated (unit / integration)
- [X] DDD / hexagonal boundaries respected (domain has no I/O)
- [X] No secrets; config via environment variables

## 6. Evidence links
- Internal Reminders Endpoint: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api
- Remove End Time PR: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal
- Gateway Fix: https://github.com/code-corhuila/telemed-ia-api-gateway
