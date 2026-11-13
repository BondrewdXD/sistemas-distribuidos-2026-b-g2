<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       15-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 15

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: Telemedicina
- SPRINT_GOAL: Deliver the final C3 milestone: full-stack local deployment verified end to end, both required videos produced (promotional and technical), the HCCDP-Solution Architectures certification completed with evidence, and the project documentation aligned with the deployed code.
<!-- CONFIG-END -->

## 1. User stories worked this week

| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| HU-018 | Worker: real appointment reminders and DLQ | done | https://github.com/code-corhuila/telemed-ia-worker/pull/7 |
| HU-019 | Transactional Outbox in Appointment and Consultation | done | https://github.com/code-corhuila/telemed-ia-medical-consultation-api/pull/17 |
| HU-020 | Full-stack deployment from `qa` with observability | done | https://github.com/code-corhuila/telemed-ia-infra-postgres/pull/29 |
| HU-021 | C3 promotional video (1 min) | done | Local artifact, see evidence links |
| HU-022 | C3 technical video (2-3 min) | done | Local artifact, see evidence links |
| HU-023 | C3 certification: HCCDP-Solution Architectures Course | done | https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/tree/main/certification |
| HU-024 | Project documentation aligned with deployed code | done | https://github.com/code-corhuila/telemed-ia-docs/pull/127 |

## 2. My individual contribution

- **Full-stack deployment:** Ran the complete local deployment from the `qa` branch of all 31 repositories (8 APIs, 8 portals, 1 shell, 1 gateway, 1 worker, PostgreSQL, MongoDB, RabbitMQ, Prometheus, Grafana, Jaeger, Mailpit). Verified that the shell at `localhost:4200` loads, the gateway routes correctly, and the observability stack (Prometheus targets, Grafana dashboards, RabbitMQ queues) is green.
- **End-to-end PDF flow verification:** With the platform running, completed the full asynchronous flow for a real consultation: patient schedules an appointment, patient uses the AI pre-consultation chat, the professional records the attention, the transactional outbox publishes `PostConsultationSummaryGenerated`, the worker consumes it, `document-generation-api` produces the PDF, and the patient receives it. This validated the `Transactional Outbox` + RabbitMQ + Worker chain that had failed multiple times during earlier sprints.
- **Promotional video (1 min):** Produced the `Video 1` requested by Juliana following her script beats: (a) the problem — arriving at a consultation and wasting it explaining symptoms, (b) the solution — TeleMed-IA lets the patient schedule in seconds and answer AI pre-consultation questions, (c) the outcome — the doctor arrives prepared and the patient receives a clear PDF summary. Edited with voice-over recorded separately, no background audio (per the professor's instruction "nada de fondo"), zoom keyframes on the important parts of the UI, and large subtitles.
- **Technical video (2-3 min):** Produced the `Video 2` as the technical owner. The video covers: cloning the 31 repositories from `qa`, the branching model (`develop` → `qa` → `main` by `cherry-pick -x`), the master script that generates JWT keys and env files, applying Flyway migrations, building the APIs (Java, Go, Python), bringing up RabbitMQ and the Worker, starting the API Gateway and the 8 portals, and finally the observability stack (Prometheus targets UP, Grafana dashboards, RabbitMQ queues, Mailpit). The video uses the "supreme script" `telemed-up-from-qa.sh` so the deployment is reproducible from a clean machine.
- **HCCDP-Solution Architectures Course (C3 certification):** Completed the 56-hour Huawei ICT Academy course. Finished chapters 1 to 14, the 4 online labs, and the final exam (score 77/100). Submitted the `certification/` folder in my fork with the `README.md`, the 21 evidence screenshots, the `design/architecture-design-note.md` (1,200-2,000 words, sections 1-6), the `target-architecture.png`, and the two required ADRs (`ADR-C3-01` and `ADR-C3-02`). Certificate in `certificate.pdf`.
- **Documentation:** Updated `telemed-ia-docs` to reflect the UUID migration and the deployment model. Added `DEC-XXX` entries to `06-appointment-service/decisions.md` and `07-consultation-service/decisions.md`, updated `_shared.yaml` alignment, added `GET /appointments/{id}` to `appointment-service.yaml`, recorded the two open technical debts (`startTime` vs `start` mismatch in the Appointment schema, and `attentionSummaryId` still `int64` in Go while the schema says `UUID`), and wrote the change-log entry for the UUID migration.
- **Forum C3:** Submitted the team + individual forum post comparing the two strongest team problems of the corte: (1) the asynchronous PDF flow failure cascade (6 distinct causes, resolved with a shared messaging contract, topic exchanges, DLQ, mandatory publish, and a fix to the transactional Outbox payload), and (2) the `int64` vs UUID inconsistency between the OpenAPI contract and the implementations. Also contributed the personal reflection on using AI assistants (DeepSeek) during the corte and the "inspect before acting / validate empirically" methodology it forced.

## 3. Blockers and risks

- **Remaining contract debt:** `_shared.yaml#/components/schemas/Appointment` uses `startTime`/`endTime` but the implementation uses `start`/`end`, and `PostSummary.attentionSummaryId` is still `int64` in Go while the schema says `UUID`. Both are recorded in `15-project-control/technical-backlog.md`. They do not block the deliverable but must be closed in a follow-up.
- **Service token contract:** `document-generation-api` and the `worker` still need a service token with a role or claim that the consultation API validates. Today `RequireJWT` only checks the signature and extracts `sub`/`role`; there is no per-endpoint role check, so any valid JWT can read any summary. This is recorded as a pre-existing security gap.
- **Event publication:** `PostConsultationSummaryGenerated` is defined but the event adapter in `medical-consultation-api` is `NoOpEventPublisher` until `ADR-011` is accepted. In this corte, the flow was validated with the Worker running against the outbox + RabbitMQ; if the broker is disabled in a future deployment, the flow reverts to a state where the PDF is not generated automatically.
- **Remaining tech debt (not blocking the delivery):** `InMemoryIdempotencyStore` in `appointment-scheduling-api` is not persistent nor thread-safe; the `GET /appointments/{id}` endpoint is not yet consumed by the portal (the reschedule page still resolves the appointment via `listByPatient` + `find`); and the `identity-and-access` service still needs the "create PROFESSIONAL user" admin flow finished to avoid manual DB inserts in `qa`.

## 4. Plan for next week

- Close the two contract debts in `telemed-ia-docs` (`startTime`/`endTime` vs `start`/`end` in `_shared.yaml`; `attentionSummaryId` typing) in a single dedicated PR, coordinated with `document-generation` and `medical-consultation-api`.
- Implement the service-token flow end to end: `identity-and-access` emits a short-lived token with `role: "SERVICE"` and a `service` claim; `medical-consultation-api` adds per-endpoint role checks (`SERVICE` for `GET /post-summaries/{id}` and `GET /consultations/{id}/attention`); `worker` and `document-generation-api` consume it. This closes the pre-existing security gap detected during the corte.
- Finish the `identity-and-access` admin flow to create PROFESSIONAL users (removes the manual SQL insert), and add a smoke test that covers it.
- Retire `InMemoryIdempotencyStore` in `appointment-scheduling-api` in favour of a persistent table (equivalent to `idempotency_key` in `patient-management-db`), with a `hash(body)` column to reject key reuse with different bodies (already the pattern in `patient-management-api`).
- Add the `btree_gist` extension verification in `infra-postgres` and, if the extension is missing, add the corresponding `EXCLUDE USING gist` constraints on `appointments` so that simultaneous booking requests cannot create overlapping slots (closes the race condition that is currently only handled in application code).
- Record the deployment recipe (`telemed-up-from-qa.sh`) in the `docs` runbook so any team member can reproduce the local environment without improvising.

## 5. Compliance self-check

- [X] Conventional Commits - `type(scope): summary`
- [X] Per-environment HU branch + PR to that environment (`hu-xxx-dev -> develop`, `cherry-pick -x` to `qa` and `main`)
- [X] Testable acceptance criteria
- [X] Tests added/updated (unit / integration)
- [X] DDD / hexagonal boundaries respected (domain has no I/O)
- [X] No secrets; config via environment variables
- [X] No secrets in `.env` files committed (all env files are generated locally from `.env.example` and are gitignored)
- [X] Both required videos produced, edited, and delivered without background audio

## 6. Evidence links

**Repositories (all `qa` branch, full-stack deployment verified):**
- Docs: https://github.com/code-corhuila/telemed-ia-docs
- Infra: https://github.com/code-corhuila/telemed-ia-infra-postgres
- Infra Mongo: https://github.com/code-corhuila/telemed-ia-infra-mongo
- API Gateway: https://github.com/code-corhuila/telemed-ia-api-gateway
- Worker: https://github.com/code-corhuila/telemed-ia-worker
- Patient Management: https://github.com/code-corhuila/telemed-ia-patient-management-db | https://github.com/code-corhuila/telemed-ia-patient-management-api | https://github.com/code-corhuila/telemed-ia-patient-management-portal
- Appointment Scheduling: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-db | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal
- Medical Consultation: https://github.com/code-corhuila/telemed-ia-medical-consultation-db | https://github.com/code-corhuila/telemed-ia-medical-consultation-api | https://github.com/code-corhuila/telemed-ia-medical-consultation-portal

**Deployment and verification PRs:**
- Prometheus + postgres-exporter + scrape config: https://github.com/code-corhuila/telemed-ia-infra-postgres/pull/29
- Worker: DLQ, retries, timeouts: https://github.com/code-corhuila/telemed-ia-worker/pull/7
- Medical Consultation: Outbox + RabbitMQ publisher: https://github.com/code-corhuila/telemed-ia-medical-consultation-api/pull/17
- Appointment Scheduling: idempotency hash: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-api/pull/24
- Docs: `GET /appointments/{id}` and UUID migration decisions: https://github.com/code-corhuila/telemed-ia-docs/pull/127

**C3 certification (HCCDP-Solution Architectures Course):**
- Certification folder: https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/tree/main/certification
- Course: HCCDP-Solution Architectures Course (56 hours, Huawei ICT Academy)
- Final exam score: 77/100
- Evidence screenshots: `certification/evidence/00-enrollment.png` through `19-final-exam.png`
- Design note: `certification/design/architecture-design-note.md`
- ADRs: `certification/design/ADR-C3-01.md`, `certification/design/ADR-C3-02.md`
- Certificate: `certification/evidence/certification`

**Videos (local artifacts, submitted through Moodle separately):**
- Video 1 - Promotional (1 minute)
- Video 2 - Technical deployment (2-3 minutes)

**Forum C3:**
- Team + individual forum post: `Forum_C3_TeleMed-IA.pdf` (submitted in Moodle) - covers the asynchronous PDF failure cascade and the UUID contract inconsistency, plus a personal reflection on AI-assisted development.