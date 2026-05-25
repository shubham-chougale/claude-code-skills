---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Tech Lead
sprint: 0
---

# Coding Standards — {{PROJECT_NAME}}

These are the rules for writing code in this project. They exist to keep the codebase consistent and readable by anyone on the team. Enforce them via linter where possible — manual review for the rest.

## General Rules

- Write code for the next developer who reads it, not just for the machine
- Name things clearly. A longer name that explains itself beats a short cryptic one
- One function does one thing
- If you need a comment to explain what the code does, rename the variable or function instead
- Comments explain WHY, not WHAT

## File Organization

```
src/
├── api/          ← Route handlers only — no business logic
├── services/     ← Business logic
├── models/       ← Data models and database access
├── middleware/   ← Express/FastAPI middleware
├── utils/        ← Pure utility functions
├── types/        ← TypeScript interfaces and types (if applicable)
└── tests/        ← Test files mirror src/ structure
```

## Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| Variables | camelCase | `userId`, `authToken` |
| Functions | camelCase, verb-first | `getUser()`, `sendEmail()` |
| Classes | PascalCase | `UserService`, `AuthMiddleware` |
| Constants | SCREAMING_SNAKE | `MAX_LOGIN_ATTEMPTS` |
| Files | kebab-case | `user-service.ts`, `auth-middleware.ts` |
| DB columns | snake_case | `user_id`, `created_at` |

## Functions

- Maximum 30 lines per function. Extract if longer.
- Maximum 3 parameters. Use an object for more.
- Return early from validation checks — avoid deep nesting

```javascript
// Bad
function processUser(user) {
  if (user) {
    if (user.isActive) {
      // 20 lines of logic
    }
  }
}

// Good
function processUser(user) {
  if (!user) return null;
  if (!user.isActive) return null;
  // 20 lines of logic
}
```

## Error Handling

- Never swallow errors silently (`catch {}` is banned)
- Always log the original error before throwing a new one
- Use specific error types, not generic `Error`
- HTTP errors must include a user-readable message and an internal code

```javascript
// Bad
try { ... } catch (e) {}

// Good
try { ... } catch (e) {
  logger.error('Failed to fetch user', { userId, error: e });
  throw new DatabaseError('User lookup failed', { cause: e });
}
```

## Testing

- Every public function must have at least one test
- Test the behavior, not the implementation
- Test names follow: `[method] [scenario] [expected result]`
  - `login_withInvalidPassword_returns401`
- Use real data shapes, not `foo`, `bar`, `test123`

## {{STACK}}-Specific Rules

[Add language or framework-specific rules here]

---
*Owner: Tech Lead — update when standards are formally agreed upon by the team.*
