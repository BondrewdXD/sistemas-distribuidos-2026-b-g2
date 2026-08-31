<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       05-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 05

<!-- CONFIG-START - must match your profile repo (username/username) CONFIG -->
- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: Telemedicina
- SPRINT_GOAL: Develop the initial MVP frontend, validate connectivity with the backend using Postman, and implement the embedded PostgreSQL database from the backend
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) |
|---|---|---|
| MVP-004 | Development of the user interface (frontend) with ChatGPT assistance | done |
| MVP-005 | Connectivity and endpoint validation testing (frontend-backend) using Postman | done |
| MVP-006 | Configuration and integration of the embedded PostgreSQL database from the backend | done |

## 2. My individual contribution
- I used ChatGPT to generate the main frontend components (home screens, forms, and navigation), which significantly accelerated the UI development.
- I conducted thorough connectivity testing between the frontend and backend using Postman, verifying that the API endpoints correctly responded to GET, POST, and PUT requests.
- I configured PostgreSQL as an embedded database from the backend, adjusting the connection strings and migrations so that the database starts automatically when the application launches.
- I validated data persistence, ensuring that CRUD operations performed from the frontend were correctly reflected in the database.

## 3. Blockers and risks
- Initial CORS issues occurred when trying to connect the frontend (running on one port) with the backend (on another port); these were resolved by configuring the appropriate headers.
- The embedded database requires some manual configuration on Windows environments (environment variables and permissions); a step-by-step guide was documented for the team.
- Some endpoints are still not returning all expected fields; the DTO mapping in the backend needs to be adjusted.

## 4. Plan for next week
- Implement authentication logic (user login and registration) connecting the frontend with the backend security services.
- Begin connecting the frontend forms with the actual API endpoints (replacing mock data).
- Conduct end-to-end (E2E) integration tests between the frontend, backend, and database.
- Refine the UI design based on team feedback.

## 5. Compliance self-check
- [x] Conventional Commits - `type(scope): summary`
- [x] Per-environment HU branch + PR to that environment (hu-xxx-dev -> develop, ...)
- [ ] Testable acceptance criteria
- [x] Tests added/updated (unit / integration)
- [ ] DDD / hexagonal boundaries respected (domain has no I/O)
- [x] No secrets; config via environment variables

> Note: The PostgreSQL connection is now working, and the Postman tests successfully validated the data flow. The "acceptance criteria" and "hexagonal boundaries" checkboxes will continue to be reviewed as we progress with the functionalities.

## 6. Evidence links
- 
-