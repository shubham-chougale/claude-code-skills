---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Tech Lead
sprint: 0
---

# Git Branching Strategy — {{PROJECT_NAME}}

> View Git Branching Diagram → [git-branching.html](../diagrams/git-branching.html)

## Branch Structure

```
main          ← Production-ready code only. Protected.
  └── staging ← Pre-release testing. Merges to main.
        └── develop ← Integration branch. All features merge here.
              └── feature/[name]  ← One branch per story/task
              └── fix/[name]      ← Bug fixes
              └── hotfix/[name]   ← Emergency production fixes
```

## Branch Naming

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature/[ticket]-[short-description]` | `feature/AUTH-12-google-login` |
| Bug fix | `fix/[ticket]-[short-description]` | `fix/AUTH-45-session-expiry` |
| Hotfix | `hotfix/[version]-[short-description]` | `hotfix/1.2.1-payment-null-error` |
| Release | `release/[version]` | `release/1.3.0` |

## Workflow

```
1. Branch from develop
   git checkout develop && git pull
   git checkout -b feature/TICKET-123-feature-name

2. Work on your branch
   Commit often. Push daily.

3. Open PR to develop
   All tests must pass.
   One approval required.

4. Merge to develop
   Squash and merge.
   Delete branch after merge.

5. Release cycle
   develop → staging (QA)
   staging → main (release)
```

## Commit Message Format

```
[type]: [short description]

Types:
  feat     New feature
  fix      Bug fix
  chore    Tooling, config, dependency update
  refactor Code change with no behavior change
  test     Adding or updating tests
  docs     Documentation only

Examples:
  feat: add Google OAuth login
  fix: resolve session timeout on mobile
  chore: update eslint to v9
```

## PR Rules

- PR title follows the same format as commit messages
- Description must explain WHY, not just WHAT
- Link the Jira/Linear ticket in the PR description
- All CI checks must pass before review
- One approval from a team member required
- No direct pushes to `main` or `develop`

## Hotfix Process

For critical production bugs only:

```
1. Branch from main: git checkout -b hotfix/1.2.1-description
2. Fix the bug
3. PR directly to main
4. After merge, immediately merge main back to develop
```

---
*Owner: Tech Lead — set once at project start. Update only when the branching strategy formally changes.*
