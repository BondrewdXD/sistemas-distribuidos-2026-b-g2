<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.

     Your weekly grade is read AUTOMATICALLY from this file:

       08-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 09

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->

- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: Telemedicina
- SPRINT_GOAL: Implement the appointment-scheduling bounded context end-to-end (database, API and CI), align the infrastructure repository with the new single-instance model of Anexo J, and freeze the medical-consultation domain in a consistent state after the change of priorities.

<!-- CONFIG-END -->

## 1. User stories worked this week

| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| HU-007 | Check General Practitioner Availability (database layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db |
| HU-008 | Schedule Appointment (database layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db |
| HU-009 | Manage My Appointments (database layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db |
| HU-011 | Update Appointment Status (database layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db |
| HU-007 | Check General Practitioner Availability (API layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api |
| HU-008 | Schedule Appointment (API layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api |
| HU-009 | Manage My Appointments (API layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api |
| HU-011 | Update Appointment Status (API layer) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api |
| HU-012 | Record Medical Care (domain and application, frozen) | doing | https://github.com/code-corhuila/telemed-ia-medical-consultation-api |
| HU-013 | Record Referral (domain and application, frozen) | doing | https://github.com/code-corhuila/telemed-ia-medical-consultation-api |
| HU-014 | Finalize Medical Consultation (domain and application, frozen) | doing | https://github.com/code-corhuila/telemed-ia-medical-consultation-api |
| INFRA | Anexo J alignment: single instance per engine | done | https://github.com/code-corhuila/telemed-ia-infra-postgres |

## 2. My individual contribution

### Appointment-scheduling domain (Python, FastAPI)

- Built the **database repository** from scratch: `01_ddl/`, `02_dml/`, `03_dcl/`, `04_tcl/`, `05_rollbacks/` families, `flyway.conf`, `deploy/compose.yml`, `db-ci.yml` with reconstruction verification.
- Designed the schema with two tables: `appointments` (root aggregate with a five-state lifecycle) and `professional_availability` (recurring weekly availability per professional). No cross-domain foreign keys, following Anexo J.3.4.
- Implemented the **service API in Python 3.12 with FastAPI** following the hexagonal architecture described in Anexo C: `domain/`, `application/` (ports, use cases, DTOs, events), `adapter/inbound/http/`, `adapter/outbound/{persistence,messaging}/`, and `config/`.
- Wrote the domain model with a strict state machine (`CONFIRMED`, `RESCHEDULED`, `COMPLETED`, `CANCELLED`, `NO_SHOW`) and typed domain exceptions, all covered by unit tests.
- Implemented six use cases (create, cancel, reschedule, update status, list by patient, list by professional) with in-memory fakes for testing.
- Implemented the HTTP adapter with:
  - RS256 JWT validation in the service itself (norm 5.3.7).
  - Common error envelope `{error, message, details?, traceId}` (norm 5.3.5).
  - `X-Correlation-Id` reuse or generation and echo (norm 5.3.9).
  - `Idempotency-Key` on creation, temporary in-memory store (norm 5.3.8).
  - Paginated listings `{data, meta}` (norm 5.3.6).
- Implemented the **Postgres adapter** with `asyncpg`, explicit connection limits and statement timeouts (norm 5.3.10). Wired the runtime composition root with a FastAPI lifespan.
- Wrote a `NoOpEventPublisher` behind the `EventPublisher` port, ready to be replaced by a RabbitMQ adapter when ADR-011 is accepted.
- Added CI workflow (ruff + pytest) and a PR template with the project-specific checklist.
- Ran the **end-to-end verification** against `-infra-postgres`: created an appointment via HTTP with a valid JWT and Idempotency-Key, retrieved it with a paginated envelope, and confirmed the row is persisted in PostgreSQL.

### Medical-consultation domain (Go, frozen)

- Built the **database repository**: schema `medical_consultation` with three tables (`consultations`, `attention_summaries`, `post_summaries`), Flyway migrations V001 to V010 with reversals U001 to U010, and a CI workflow that reconstructs and rolls back the schema on every pull request.
- Built the **service API in Go**: bootstrap with structured logging and explicit timeouts, pure domain model (`Consultation`, `AttentionSummary`, `PostSummary`, `MedicationInstruction`) with typed errors and 19 unit tests, application ports and DTOs (Pydantic-style with camelCase serialization), and an HTTP adapter with RS256 JWT, common error envelope, correlation middleware, `Idempotency-Key` on creation, and paginated listings.
- **Froze** the domain after the team changed priorities (the appointment-scheduling domain became the priority for the current period). The database and API are in a consistent state on the `develop` branch, waiting to be resumed.

### Infrastructure repository (Anexo J alignment)

- Aligned `telemed-ia-infra-postgres` with Anexo J:
  - The repo now owns the **single PostgreSQL instance** of the project: image, volume, healthcheck and the `pgcrypto` extension.
  - Added `postgres/init/01-instance.sh`, an idempotent bootstrap that creates one `<domain>_app` user and its `<domain>_reader` / `<domain>_writer` roles per domain.
  - `compose.yml` requires every password with `${VAR:?required}`, so a missing variable fails the start with a clear message.
  - Renamed env examples to the Anexo J convention (`env/dev.env.example`, `env/qa.env.example`, `env/main.env.example`).
  - Strengthened `scripts/up.sh` (fails on missing env file or unfilled `change-me` placeholders) and `scripts/down.sh` (requires an explicit `--volumes` flag and manual confirmation before wiping the volume).
  - Blocked `env/dev.env`, `env/qa.env`, `env/main.env`, `keys/` and `*.pem` in `.gitignore`.
  - Rewrote the README with a Rules section and a step-by-step guide to add a new domain.
  - Added a CI workflow that validates the compose file as YAML, the env examples as `KEY=value`, and the shell scripts with `sh -n` / `bash -n`.

### Documentation and governance

- Studied Anexo J in detail and adapted the infrastructure repo accordingly.
- Reviewed the existing architecture artifacts to prepare for the second evaluation period.

## 3. Blockers and risks

- The **medical-consultation domain is frozen** after the team changed priorities. It is not deleted; it stays on `develop` waiting to be resumed.
- The **React portal** originally planned for the medical-consultation domain was dropped after a proof of concept showed that Native Federation (the federation library used by the shell) cannot load a React remote without migrating the entire shell to Module Federation. This would break the three Angular portals already delivered. **A negotiation with the professor is pending.**
- The **appointment-scheduling portal** has not been started yet. It is the next block of work.
- The **`-infra-mongo` repository** is not used yet because MongoDB was reassigned to another teammate's domain. It will be wired when that domain reaches the implementation stage.
- The `patient-management` domain was **frozen** as well. It works end-to-end but its `-db` and `-api` still follow the pre-Anexo J model (own instance, `public` schema). Migrating them to the shared instance is registered as debt.
- Some architectural artifacts (diagrams, ADRs, API contracts) still need alignment with the actual implementation of the appointment-scheduling service.

## 4. Plan for next week

- Start the **Angular portal for the appointment-scheduling domain** (`telemed-ia-appointment-scheduling-portal`), following the same Native Federation pattern used for `patient-management-portal`.
- Implement the four view states per screen (loading, error with retry, empty, data) and the form validation rules defined in Anexo H.
- Register the new remote in `telemed-ia-front` (`federation.manifest.json` + `app.routes.ts` + `remotes/appointment.remote.ts`).
- Register the new route in `telemed-ia-api-gateway` (`nginx/routes/appointment.conf`) with the rewrite from `/api/v1/appointments/*` to `/api/appointments/*`.
- Add the portal `include:` to `telemed-ia-infra-postgres/compose.yml`.
- Run the end-to-end verification (shell + portal + gateway + API + database).
- If time permits, start the migration of `patient-management-db` and `patient-management-api` to the Anexo J shared-instance model.
- Continue reviewing and approving the Pull Requests generated by team members.

## 5. Compliance self-check

- [X] Conventional Commits - `type(scope): summary`
- [X] Per-environment HU branch + PR to that environment (feat/* branches to develop, chore/* for tooling)
- [X] Testable acceptance criteria
- [X] Tests added/updated (unit + HTTP; integration against PostgreSQL verified manually)
- [X] DDD / hexagonal boundaries respected (domain has no I/O; domain imports nothing outside the standard library)
- [X] No secrets; config via environment variables (`env/dev.env` gitignored)

## 6. Evidence links

### Appointment-scheduling database
- Repository: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db
- Schema `appointment_scheduling` with `appointments` and `professional_availability`.
- Migrations V001 to V008 with reversals U001 to U008.
- CI workflow `db-ci.yml` reconstructs, reverts and reapplies on every PR.

### Appointment-scheduling API (Python, FastAPI)
- Repository: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api
- Bootstrap FastAPI + `/health`.
- Domain (Appointment aggregate, Availability value object, typed errors).
- Ports and DTOs (camelCase, pagination envelope).
- Use cases with in-memory fakes.
- HTTP adapter (JWT RS256, envelope, correlation, idempotency).
- Postgres adapter (`asyncpg` with explicit limits) and runtime composition root.
- CI workflow (`ruff check` + `pytest`).
- PR template and README documenting the contract deviations and known limitations.

### Medical-consultation database
- Repository: https://github.com/code-corhuila/telemed-ia-medical-consultation-db
- Schema `medical_consultation` with `consultations`, `attention_summaries` and `post_summaries`.
- Migrations V001 to V010 with reversals U001 to U010.
- CI workflow verified green.

### Medical-consultation API (Go, frozen)
- Repository: https://github.com/code-corhuila/telemed-ia-medical-consultation-api
- Bootstrap Go with health endpoint and explicit timeouts.
- Domain model with typed errors and unit tests.
- Application ports and DTOs.
- HTTP adapter with JWT RS256, envelope and correlation.
- Postgres adapter and composition root.
- Frozen after the priority change of the team.

### Infrastructure
- Repository: https://github.com/code-corhuila/telemed-ia-infra-postgres
- Single PostgreSQL instance, idempotent init script with per-domain roles, secret protection, hardened scripts, validation CI.

### Documentation
- https://github.com/code-corhuila/telemed-ia-docs