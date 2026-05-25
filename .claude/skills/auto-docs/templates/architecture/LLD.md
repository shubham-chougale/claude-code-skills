---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Senior Developer
sprint: 1
---

# Low Level Design — {{PROJECT_NAME}}

> View System Architecture → [HLD.md](HLD.md)

## Overview

This document covers module-level detail for {{PROJECT_NAME}}. Each section documents a module's public interface, internal structure, and dependencies. Audience: developers working directly on the codebase.

---

## Module: [Module Name, e.g. AuthService]

**Location:** `src/services/auth/`
**Purpose:** Handles user authentication — login, logout, token refresh, and session management.

### Public Interface

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `login(email, password)` | email: string, password: string | `Promise<AuthToken>` | Validates credentials, returns JWT |
| `logout(userId)` | userId: string | `Promise<void>` | Invalidates session token |
| `refreshToken(token)` | token: string | `Promise<AuthToken>` | Issues new token from valid refresh token |
| `validateToken(token)` | token: string | `Promise<User>` | Validates JWT, returns user object |

### Internal Structure

```
AuthService
├── login()
│   ├── hashPassword(password)
│   ├── findUserByEmail(email)
│   └── generateToken(userId)
├── logout()
│   └── invalidateToken(userId)
└── refreshToken()
    ├── validateRefreshToken(token)
    └── generateToken(userId)
```

### Dependencies

| Dependency | Version | Why |
|-----------|---------|-----|
| bcrypt | 5.x | Password hashing |
| jsonwebtoken | 9.x | JWT generation + validation |
| UserRepository | internal | User lookup |

### Error Handling

| Error | When | Response |
|-------|------|----------|
| `InvalidCredentialsError` | Wrong email or password | 401 Unauthorized |
| `TokenExpiredError` | JWT past expiry | 401 + refresh hint |
| `AccountLockedError` | Too many failed attempts | 403 + unlock time |

---

## Module: [Module Name 2]

**Location:** `src/[path]/`
**Purpose:** [What this module does]

### Public Interface

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| [method] | [params] | [return type] | [what it does] |

---

## Change Log

| Date | Module | Change | Sprint |
|------|--------|--------|--------|
| {{DATE}} | — | Initial document created | 1 |

---
*Owner: Senior Developer — update when module interfaces or internal logic changes significantly.*
