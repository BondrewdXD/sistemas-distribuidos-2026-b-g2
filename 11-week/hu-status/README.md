<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       11-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 11

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Jose Miguel Vera Garzon
- GITHUB_USER: BondrewdXD
- TEAM: Telemedicina
- SPRINT_GOAL: Initialize the asynchronous infrastructure (Worker and Workflow repositories), align database schemas with UUIDs as requested by the team, and complete the observability workshop (W11).
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| INFRA-001 | Create Worker and Workflow infrastructure repositories | doing | https://github.com/code-corhuila/telemed-ia-docs |
| INFRA-002 | Migrate database schemas from INT to UUID | doing | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db |
| INFRA-003 | Observability, SLOs, and Incident Response Workshop (W11) | done | https://github.com/BondrewdXD/telemed-ia-docs/tree/main/11-week/workshop |
| HU-014 | Implement local mock mode for Appointment and Consultation portals | done | https://github.com/code-corhuila/telemed-ia-front/pull/17 |

## 2. My individual contribution
- **Asynchronous Infrastructure:** Started the scaffolding for the `telemed-ia-worker` and `telemed-ia-workflow` repositories. Configured the initial Docker setup and the base integration for Camunda 7 to handle the BPMN core flow.
- **Database Adjustments:** Reviewed the Flyway migrations in the `-db` repositories (Appointment and Medical Consultation) to replace auto-incremental `INT` primary keys with `UUID` generation (`uuid_generate_v4()`), ensuring distributed data consistency and preventing ID collisions.
- **Observability (Week 11 Workshop):** Completed Delivery 1 and Delivery 2 (CP0 through CP10). Traced a critical user journey (recording a medical attention), defined a structured JSON log contract, implemented a trace-context middleware in Python/FastAPI, and exposed Prometheus metrics. Documented SLOs, error budgets, burn-rate alerts, a runbook, and a blameless postmortem for a simulated database degradation.
- **Frontend Integration:** Finalized the mock strategies for both the Appointment and Consultation portals (using HTTP interceptors and `tsconfig` path aliases respectively) so the UI can be tested independently of the backend. Registered the consultation remote in the shell.

## 3. Blockers and risks
- **UUID Migration Breaking Changes:** Changing primary keys from `INT` to `UUID` in the databases requires synchronizing the data models in the APIs and the TypeScript interfaces in the portals. We must ensure mocks and fixtures are updated accordingly to avoid type errors.
- **Local Port Collision:** Since the `appointment-scheduling-api` and `medical-consultation-api` both try to run on port 8080 locally, full E2E testing without Docker requires manual API switching.
- **OpenTelemetry Integration:** Implementing real tracing in the Go and Java APIs might take longer than expected due to the learning curve.

## 4. Plan for next week
- Implement the W11 implementation plan: Add OpenTelemetry to the `appointment-scheduling-api` and `medical-consultation-api`.
- Finish the initial setup of the `worker` and `workflow` repositories.
- Apply the UUID changes to the API DTOs and Angular models, updating the mock fixtures.
- Coordinate with Juliana and Sofia to test the complete E2E flow (Shell -> Gateway -> API -> DB -> Worker).

## 5. Compliance self-check
- [X] Conventional Commits - `type(scope): summary`
- [X] Per-environment HU branch + PR to that environment (hu-xxx-dev -> develop, ...)
- [X] Testable acceptance criteria
- [X] Tests added/updated (unit / integration)
- [X] DDD / hexagonal boundaries respected (domain has no I/O)
- [X] No secrets; config via environment variables

## 6. Evidence links
- **Week 11 Workshop:** https://github.com/BondrewdXD/telemed-ia-docs/tree/main/11-week/workshop
- **Patient Management Portal:** https://github.com/code-corhuila/telemed-ia-patient-management-portal
- **Appointment Scheduling Portal:** https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal
- **Medical Consultation Portal:** https://github.com/code-corhuila/telemed-ia-medical-consultation-portal