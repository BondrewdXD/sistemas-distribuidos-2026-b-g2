# Distributed Systems - 2026-B - Group 2

Class repository - Corporacion Universitaria del Huila (CORHUILA).

| | |
| --- | --- |
| **Course** | Distributed Systems (cod. 82739) |
| **Group** | 2 |
| **Room** | C4-409 [Sala Informatica] - Prado Alto |
| **Schedule** | Lunes 8:40-10:20 a.m. y Jueves 7:50-9:30 a.m. |
| **Term** | 2026-B |

## How this course works

This is a **project course**: your team builds one real distributed system all
semester and ships it as **releases (MVP)** each corte, working in **weekly sprints**.
There are **no written exams** - the product is the evaluation.

- **Session 1** each week = *weekly* (technical content + execution/status).
- **Session 2** each week = *planning* (plan the next sprint + real scenarios).
- **Releases:** MVP 1 (corte 1), MVP 2 (corte 2), MVP 3 + final (corte 3).

## Your weekly individual delivery (IMPORTANT - graded automatically)

Every week, in **your fork of this repository**, fill in:

```
NN-week/hu-status/README.md
```

Keep the exact structure of the template (it is parsed automatically).

### Profile repo (mandatory)

Create your profile repo **`username/username`** with a CONFIG block in its README:

```
<!-- CONFIG
FULL_NAME: Your Full Name
GITHUB_USER: your-github-user
-->
```

Without a correct CONFIG the automation cannot attribute your work - it will look
like you delivered nothing.

## Git workflow (per environment)

Long-lived environment branches: **develop -> qa -> main (prod)**. For each user
story you cut a branch **from that environment** and open a Pull Request **back to
the same environment**, then repeat for the next environment:

```
develop -> hu-xxx-dev  -> PR to develop
qa      -> hu-xxx-qa   -> PR to qa
main    -> hu-xxx-main -> PR to main
```

Commits use Conventional Commits: `type(scope): summary` (e.g. `feat(orders): ...`).

## How to deliver

```bash
# 1) Fork this repo on GitHub, then clone YOUR fork
git clone https://github.com/<your-user>/sistemas-distribuidos-2026-b-g2.git
cd sistemas-distribuidos-2026-b-g2
# 2) Fill your weekly report
#    edit NN-week/hu-status/README.md
git add NN-week/hu-status/README.md
git commit -m "docs(hu-status): week NN report"
git push
```

The learning material (interactive OVAs) lives at:
https://code-corhuila.github.io/ova-web/2026-B/distribuidos/
