<!-- HU-STATUS TEMPLATE - do NOT remove the <!-- ... --> markers or the table headers.
     Your weekly grade is read AUTOMATICALLY from this file:
       13-week/hu-status/README.md  (inside YOUR fork). English. -->

# Weekly Status - Week 13

<!-- CONFIG-START -->
- FULL_NAME: Jose Miguel Vera Garzón
- GITHUB_USER: BondrewdXD
- TEAM: telemed-ia
- DOCS_REPO: https://github.com/code-corhuila/telemed-ia-docs
- BOUNDARY: Backend to Database (Medical Records)
- CLAIM_ISSUE: https://github.com/code-corhuila/telemed-ia-docs/issues/140
- REFLECTION_DOC: https://docs.google.com/document/d/1wTtNLu71du6GacRwmZA9wM_knhsFT6JGNbNptCPunCU/edit?usp=sharing
- LIBRARY_BOOK: Tanenbaum, A. S., & Van Steen, M. (2008). Sistemas distribuidos: principios y paradigmas (2da ed.). Pearson Educación. 005.4476 T15D EJ: 2
- LIBRARY_RECORD_TIME: 08:05 AM
- STORIES: https://github.com/code-corhuila/telemed-ia-docs/issues/145 https://github.com/code-corhuila/telemed-ia-docs/issues/146 https://github.com/code-corhuila/telemed-ia-docs/issues/147
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| N/A | Threat Modeling Workshop | done | See links below |

## 2. My individual contribution
- Claimed and mapped trust boundary "Backend to Database (Medical Records)".
- Created the STRIDE analysis PR for the Medical DB.
- Created 3 security backlog issues for Spoofing, Tampering, and Info Disclosure.
- Proposed CI security gates and a negative authorization test.
- Reviewed a teammate's PR (Sofia) on the document-generation-api boundary.

## 3. Blockers and risks
- Need to integrate the CI workflow into the real microservice repository, as the current test is a proposal using a mock Express app.

## 4. Plan for next week
- Finish the implementation plan for the threat model.
- Refine acceptance criteria for the 3 security issues.

## 5. Compliance self-check
- [x] Conventional Commits - `type(scope): summary`
- [x] Testable acceptance criteria
- [x] Tests added/updated (unit / integration)
- [x] No secrets; config via environment variables

## 6. Evidence links
- PR STRIDE: [Threat model: Medical Service -> Medical DB](https://github.com/code-corhuila/telemed-ia-docs/pull/142)
- Issues: #145, #146, #147
- Review comment: [Comentario Sofia PR](https://github.com/code-corhuila/telemed-ia-docs/pull/144/changes#r4413160730)