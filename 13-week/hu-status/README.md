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
- STORIES: https://github.com/code-corhuila/telemed-ia-docs/issues/145 https://github.com/code-corhuila/telemed-ia-docs/issues/146 https://github.com/code-corhuila/telemed-ia-docs/issues/147 https://github.com/code-corhuila/telemed-ia-docs/pull/156
<!-- CONFIG-END -->

## 1. User stories worked this week
| HU ID | Title | Status (todo/doing/done) | Evidence (PR or commit URL) |
|---|---|---|---|
| N/A | Threat Modeling Workshop | done | See links below |

## 2. My individual contribution
- Threat model and STRIDE analysis for Medical DB (PR #142, review addressed in PR #156).
- Created 3 security backlog issues (#145, #146, #147).
- Proposed CI security gates and a negative authorization test.
- Reviewed a teammate's PR (Sofia).
- Completed the implementation plan in the reflection document.

## 3. Blockers and risks
- None. The CI pipeline proposal is ready for the team lead to integrate.

## 4. Plan for next week
- Implement the security backlog issues (mTLS, checksums, encryption).

## 5. Compliance self-check
- [x] Conventional Commits - `type(scope): summary`
- [x] Testable acceptance criteria
- [x] Tests added/updated (unit / integration)
- [x] No secrets; config via environment variables

## 6. Evidence links
- PR STRIDE (Original): https://github.com/code-corhuila/telemed-ia-docs/pull/142
- PR STRIDE (Review Addressed): https://github.com/code-corhuila/telemed-ia-docs/pull/156
- Issues: https://github.com/code-corhuila/telemed-ia-docs/issues/145, https://github.com/code-corhuila/telemed-ia-docs/issues/146, https://github.com/code-corhuila/telemed-ia-docs/issues/147
- Review comment: https://github.com/code-corhuila/telemed-ia-docs/pull/144/changes#r4413160730
