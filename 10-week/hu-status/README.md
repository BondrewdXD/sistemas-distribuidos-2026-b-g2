<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.

     Your weekly grade is read AUTOMATICALLY from this file:

       08-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 10

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->

- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: Telemedicina
- SPRINT_GOAL: Deliver the medical-consultation and appointment-scheduling portals with a local mock mode for backend-less development, wire the medical-consultation domain end-to-end across the three transversal repositories (shell, gateway, infrastructure), and promote the appointment-scheduling and medical-consultation portals through the QA cycle.

<!-- CONFIG-END -->

## 1. User stories worked this week

| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| HU-012 | Record Medical Care (portal UI, mock-enabled) | done | https://github.com/code-corhuila/telemed-ia-medical-consultation-portal/pull/1 |
| HU-013 | Record Referral (portal UI, mock-enabled) | done | https://github.com/code-corhuila/telemed-ia-medical-consultation-portal/pull/1 |
| HU-014 | Finalize Medical Consultation (portal UI, blocked on API HU-14) | doing | https://github.com/code-corhuila/telemed-ia-medical-consultation-portal/pull/1 |
| HU-007 | Check General Practitioner Availability (portal UI, mock-enabled) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal/pull/14 |
| HU-008 | Schedule Appointment (portal UI, mock-enabled) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal/pull/14 |
| HU-009 | Manage My Appointments (portal UI, mock-enabled) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal/pull/14 |
| HU-011 | Update Appointment Status (portal UI, mock-enabled) | done | https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal/pull/14 |
| INFRA | Include medical-consultation-db in shared Postgres instance | done | https://github.com/code-corhuila/telemed-ia-infra-postgres/pull/13 |
| INFRA | Add medical-consultation route to the API Gateway | done | https://github.com/code-corhuila/telemed-ia-api-gateway (PR pending review) |
| INFRA | Register medical-consultation remote in the shell | done | https://github.com/code-corhuila/telemed-ia-front (PR pending review) |
| PROMO | Promote medical-consultation portal from develop to qa | done | https://github.com/code-corhuila/telemed-ia-medical-consultation-portal/pull/2 |

## 2. My individual contribution

### Medical-consultation portal (Angular 21 + Native Federation)

- Delivered the **four screens** of the consultation portal end-to-end:
  - `/consultation` — patient consultation history (filtered by `COMPLETED`).
  - `/consultation/detail/:appointmentId` — consultation detail with preconsultation and post-consultation summary.
  - `/consultation/professional` — professional queue with preconsultation availability indicators.
  - `/consultation/professional/:appointmentId/attention` — clinical attention form (observations, diagnosis, recommendations, medications, referral).
- Implemented a **local mock mode** (`npm run start:mock`) so the portal can be developed, demoed and reviewed **without the shell, gateway, API or database**:
  - `src/mocks/mock-api-client.service.ts` — in-memory implementation of the shell's `ApiClientService` resolving the six consultation endpoints with ~350 ms simulated latency.
  - `src/mocks/mock-session.service.ts` — replacement for `shell/session` reading `mockRole`, `mockId` and `mockName` from query params.
  - `src/mocks/fixtures/consultation.fixtures.ts` — coherent fixtures: 7 appointments, 6 preconsultations, 3 attentions, 3 post-summaries, and one `COMPLETED` appointment intentionally without `postSummaryId` to exercise the "summary pending" state.
  - `tsconfig.mock.json` — path aliases `shell/*` → `src/mocks/*` for the mock build only.
  - `angular.json` — new `mock` configuration on `esbuild` and a `serve-mock` target on port 4205.
  - `package.json` — `npm run start:mock` script.
- Kept **`npm start` (Native Federation mode) untouched**, so the shell integration remains identical.
- Documented the Local mock mode in `README.md` and kept `BACKEND_INTEGRATION_GAPS.md` up to date.

### Appointment-scheduling portal (Angular 21 + Native Federation)

- Delivered a **local mock mode** on top of the existing portal (`npm run start:mock`) following a slightly different strategy because this portal uses `HttpClient` directly instead of the shell's `ApiClientService`:
  - `src/mocks/mock-appointment.interceptor.ts` — functional `HttpInterceptorFn` resolving every `/api/v1/appointments/*` request from fixtures (list by patient, list by professional, create, cancel, reschedule, status).
  - `src/mocks/mock-session-seed.ts` — seeds a fake decodable JWT into `sessionStorage` before bootstrap, driven by `mockRole` / `mockId` / `mockName` query params (the portal decodes the JWT itself, it does not use `shell/session`).
  - `src/mocks/mock-main.ts` — mock entry point bypassing `initFederation`.
  - `src/mocks/fixtures/appointment.fixtures.ts` — coherent fixtures aligned with the portal's `PROFESSIONAL_DIRECTORY` and `PATIENT_DIRECTORY`.
  - `tsconfig.mock.json`, `angular.json` mock config + `serve-mock` target on port 4203, and `npm run start:mock` script.
- Documented the standalone-only nature of the mock in `README.md`.

### Infrastructure repository - medical-consultation inclusion

- Included `telemed-ia-medical-consultation-db/deploy/compose.yml` in the `include:` list of `telemed-ia-infra-postgres/compose.yml`, so its Flyway migrations run against the shared `telemed-ia-postgres` instance (Anexo J model).
- Added the `medical-consultation-db-migrate` hint to `scripts/up.sh`.
- Verified that the `medical_consultation_app` / `_reader` / `_writer` roles were already provisioned idempotently by `postgres/init/01-instance.sh`.

### API Gateway - medical-consultation route

- Created `nginx/routes/consultation.conf` mapping `/api/v1/consultations/*` to the consultation service at `host.docker.internal:8080`, following the same pattern as `appointment.conf` and `patient.conf` (rate limit, auth guard, path rewrite, correlation headers, shared headers snippet).
- Documented the port 8080 collision between appointment-scheduling-api and medical-consultation-api in the route file, aligned with the project rule that only one API can run at a time.

### Shell - consultation remote registration

- Added `consultation` to `public/federation.manifest.json` pointing to `http://localhost:4205/remoteEntry.json`.
- Created `src/app/remotes/consultation.remote.ts` with `CONSULTATION_REMOTE_ROUTES`, mirroring the pattern of the other remotes and falling back to `RemoteUnavailableComponent` when the remote is down.
- Added the `/consultation` route under the authenticated `ShellLayoutComponent`.
- Added navigation entries in `shell-layout.component.html` for both roles: **Mis consultas** for patients and **Consultas asignadas** for professionals.

### Promotion and governance

- Promoted the medical-consultation portal from `develop` to `qa` using `git cherry-pick -x` on the original feature commit, following the project's promotion convention.
- Started the equivalent promotion flow for `infra-postgres`, `api-gateway` and `front`.

## 3. Blockers and risks

- **HU-14 (Finalize Medical Consultation) remains blocked on the backend.** The consultation API only registers attention summaries; it does not finalize the appointment nor generate the post-summary automatically. The portal correctly does not fake this behaviour. It will be completed when the finalization operation is added to the OpenAPI contract and the Go HTTP handlers.
- **The medical-consultation Go API is still not end-to-end functional.** Only `GET /health` is registered; the HTTP handlers and use cases are not exposed yet. The mock mode unblocks the UI work but the real integration is pending.
- **Identity mapping needs validation.** The MVP assumes the numeric JWT `sub` corresponds to the numeric patient / professional IDs used by Appointment Scheduling. This must be confirmed with the Identity/Access owner before production.
- **`env/dev.env` requires three passwords that were not present locally** (`IDENTITY_APP_PASSWORD`, `DOCUMENT_GENERATION_APP_PASSWORD`, `PROFESSIONAL_MANAGEMENT_APP_PASSWORD`). Documented in the PR description and covered by the `:?required` guard in `compose.yml`.
- **Login is not functional yet**, so tokens are still pasted manually into `sessionStorage`. This is a known limitation and not a regression.

## 4. Plan for next week

- Finish the promotion flow of `infra-postgres` (qa to main with tag `v2.0.1`).
- Complete the same promotion flow for `api-gateway` and `front` once their PRs to `develop` are approved.
- Promote the appointment-scheduling portal from `develop` to `qa` and later to `main` with tag `v2.0.1`.
- Promote the medical-consultation portal from `qa` to `main` with tag `v2.0.0`.
- Run the full end-to-end verification against the real backend for `medical-consultation` once the Go HTTP handlers are implemented.
- Continue reviewing and approving Pull Requests generated by team members.
- If time permits, start the migration of `patient-management-db` and `patient-management-api` to the Anexo J shared-instance model.

## 5. Compliance self-check

- [X] Conventional Commits - `type(scope): summary`
- [X] Per-environment HU branch + PR to that environment (`feat/*` to `develop`, `promote/*` to `qa`, `release/*` to `main`)
- [X] Testable acceptance criteria (mock mode validated manually in both portals)
- [X] Tests added/updated (existing tests kept green; no new tests needed for the mock layer)
- [X] DDD / hexagonal boundaries respected
- [X] No secrets; config via environment variables (`env/dev.env` gitignored)

## 6. Evidence links

### Medical-consultation portal
- Repository: https://github.com/code-corhuila/telemed-ia-medical-consultation-portal
- Local mock mode documented in `README.md`
- Fixtures and mock services under `src/mocks/`

### Appointment-scheduling portal
- Repository: https://github.com/code-corhuila/telemed-ia-appointment-scheduling-portal
- Local mock mode documented in `README.md`
- Functional HTTP interceptor and fixtures under `src/mocks/`

### Infrastructure
- Repository: https://github.com/code-corhuila/telemed-ia-infra-postgres
- `compose.yml` now includes `telemed-ia-medical-consultation-db/deploy/compose.yml`

### API Gateway
- Repository: https://github.com/code-corhuila/telemed-ia-api-gateway
- New route file: `nginx/routes/consultation.conf`
- Public path `/api/v1/consultations/*` routed to the consultation service

### Shell
- Repository: https://github.com/code-corhuila/telemed-ia-front
- `public/federation.manifest.json` now registers the `consultation` remote
- `src/app/remotes/consultation.remote.ts` loads the remote lazily with graceful fallback
- Navigation updated in `shell-layout.component.html`