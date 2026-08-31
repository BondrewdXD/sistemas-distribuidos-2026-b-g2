<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       04-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 04

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: Telemedicina
- SPRINT_GOAL: Develop the initial MVP of the system, defining the project structure with AI support (ChatGPT) and implementing the first backend tests
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| MVP-001 | Setup of the base backend structure (hexagonal / layered architecture) | done | [Initial structure commit](https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/tree/main/04-week/01-session/backend-structure) |
| MVP-002 | Implementation of test endpoints (health-check / status) and database connection | done | [PR to develop](https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/pull/1) |
| MVP-003 | Configuration of the unit testing environment and first tests for the backend services | doing | [Initial tests commit](https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/commit/abc123) |

## 2. My individual contribution
- I used ChatGPT to generate the initial project scaffolding (controllers, services, repositories, and DTOs), which allowed us to speed up the development environment setup.
- I defined the folder structure following DDD/Hexagonal principles, clearly separating the domain, application, and infrastructure layers.
- I set up the testing environment with the appropriate tools (Jest / PyTest) and wrote the first test cases to validate the basic business logic and health endpoints.
- I performed the initial database integration (connection configuration and base migrations).

## 3. Blockers and risks
- Environment variable configuration for different environments (dev, test, prod) is not yet fully standardized.
- Dependency on external services (authentication, storage) that are not yet available; mocks are required for testing.
- The team needs to agree on the API response standard (error codes, JSON format) to maintain consistency.

## 4. Plan for next week
- Implement the CRUD services for the main domain entities (Patient, Appointment, Doctor).
- Increase unit test coverage and begin integration testing.
- Set up the CI/CD pipeline (GitHub Actions) to automatically run tests on every PR.
- Document the API with OpenAPI/Swagger as endpoints are developed.

## 5. Compliance self-check
- [x] Conventional Commits - `type(scope): summary`
- [x] Per-environment HU branch + PR to that environment (hu-xxx-dev -> develop, ...)
- [ ] Testable acceptance criteria
- [x] Tests added/updated (unit / integration)
- [ ] DDD / hexagonal boundaries respected (domain has no I/O)
- [x] No secrets; config via environment variables

> Note: Although we have already started testing, some items such as "acceptance criteria" or "hexagonal boundaries" will be refined as we develop more complex functionality.

## 6. Evidence links
- Backend structure generated with ChatGPT: [https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/tree/main/04-week/01-session/backend-structure](https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/tree/main/04-week/01-session/backend-structure)
- First PR with base endpoints and tests: [https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/pull/1](https://github.com/BondrewdXD/sistemas-distribuidos-2026-b-g2/pull/1)
- Test configuration and examples: [Link to commit or test folder]