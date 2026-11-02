cat > 12-week/hu-status/README.md <<'EOF'
<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       12-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 12

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: telemed-ia
- SPRINT_GOAL: Migrate core domain IDs to UUID across all layers, fix security data leaks, implement slot conflict constraints, and integrate Prometheus observability.
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| HU-04 | Patient Management UUID migration and data leak fix | done | https://github.com/code-corhuila/telemed-ia-patient-management-api/pull/28 |
| HU-08 | Appointment Scheduling UUID migration and ownership | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api/pull/16 |
| HU-12 | Medical Consultation UUID migration and preconsultation view | done | https://github.com/code-corhuila/telemed-ia-medical-consultation-api/pull/10 |
| INFRA-001 | Prometheus Observability for Patient and Consultation | done | https://github.com/code-corhuila/telemed-ia-infra-postgres/pull/29 |

## 2. My individual contribution
- **UUID Migration:** Led the migration of primary keys from `INT`/`BIGINT` to `UUID` in the databases, APIs, and Angular Portals for Patient, Appointment, and Medical Consultation, aligning with `identity-and-access`.
- **Security Fixes:** Removed a critical data leak (`GET /api/patients`), implemented strict ownership validation (RBAC) for Appointment and Consultation, and fixed JWT `sub` parsing.
- **Slot Conflicts:** Implemented PostgreSQL `EXCLUDE USING gist` constraints in the Appointment DB to prevent race conditions and double-booking, mapping HTTP `409 Conflict` codes in the API and Portal.
- **Observability (W11 Workshop):** Added `MetricsMiddleware` and `/metrics` endpoints to the Go and Java APIs, integrating Prometheus and Grafana in `infra-postgres`.

## 3. Blockers and risks
- **Breaking changes:** The switch to UUID broke the old contracts. We had to synchronize the OpenAPI specs and TypeScript models across all portals.
- **Team Sync:** Required careful coordination of PR merging (DB first, then API, then Portal).

## 4. Plan for next week
- Implement the Transactional Outbox pattern in Appointment and Consultation.
- Scaffold and develop the asynchronous `Worker` repository in Java.
- Connect RabbitMQ for event-driven communication.

## 5. Compliance self-check
- [X] Conventional Commits - `type(scope): summary`
- [X] Per-environment HU branch + PR to that environment (hu-xxx-dev -> develop, ...)
- [X] Testable acceptance criteria
- [X] Tests added/updated (unit / integration)
- [X] DDD / hexagonal boundaries respected (domain has no I/O)
- [X] No secrets; config via environment variables

## 6. Evidence links
- Patient API UUID: https://github.com/code-corhuila/telemed-ia-patient-management-api
- Appointment DB Constraints: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db
- Consultation API RBAC: https://github.com/code-corhuila/telemed-ia-medical-consultation-api
- Prometheus Config: https://github.com/code-corhuila/telemed-ia-infra-postgres
EOF