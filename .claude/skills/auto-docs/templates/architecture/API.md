---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Backend Lead
sprint: 1
---

# API Design Document — {{PROJECT_NAME}}

> View API Lifecycle Diagram → [api-lifecycle.html](../diagrams/api-lifecycle.html)
> View Sequence Diagram → [sequence-diagram.html](../diagrams/sequence-diagram.html)

## Base URL

```
Production:  https://api.{{PROJECT_NAME}}.com/v1
Staging:     https://api-staging.{{PROJECT_NAME}}.com/v1
Local:       http://localhost:8000/v1
```

## Authentication

All protected endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

Tokens expire after 24 hours. Use `POST /auth/refresh` to get a new token.

## Response Format

All responses follow this structure:

```json
{
  "success": true,
  "data": {},
  "error": null,
  "meta": {
    "timestamp": "2026-05-21T10:00:00Z",
    "version": "v1"
  }
}
```

## Error Codes

| Code | Meaning |
|------|---------|
| 400 | Bad request — invalid parameters |
| 401 | Unauthorized — missing or invalid token |
| 403 | Forbidden — valid token but insufficient permissions |
| 404 | Resource not found |
| 409 | Conflict — resource already exists |
| 422 | Unprocessable — validation failed |
| 429 | Rate limited — too many requests |
| 500 | Internal server error |

---

## Endpoints

### Authentication

#### POST /auth/register

Creates a new user account.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123",
  "name": "Jane Smith"
}
```

**Response 201:**
```json
{
  "success": true,
  "data": {
    "userId": "usr_abc123",
    "email": "user@example.com",
    "message": "Verification email sent"
  }
}
```

**Errors:** 409 (email already registered), 422 (validation failed)

---

#### POST /auth/login

Authenticates a user and returns a JWT token.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123"
}
```

**Response 200:**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "rt_xyz789",
    "expiresAt": "2026-05-22T10:00:00Z"
  }
}
```

**Errors:** 401 (invalid credentials), 403 (account locked)

---

#### POST /auth/refresh

Issues a new access token using a valid refresh token.

**Request:**
```json
{
  "refreshToken": "rt_xyz789"
}
```

**Response 200:**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresAt": "2026-05-22T10:00:00Z"
  }
}
```

---

### [Resource Name, e.g. Users]

#### GET /users/:id

Returns a single user by ID. Requires authentication.

**Path Parameters:**
- `id` — User ID (string)

**Response 200:**
```json
{
  "success": true,
  "data": {
    "id": "usr_abc123",
    "email": "user@example.com",
    "name": "Jane Smith",
    "createdAt": "2026-05-01T00:00:00Z"
  }
}
```

**Errors:** 401, 403 (own profile only unless admin), 404

---

#### PATCH /users/:id

Updates user profile fields. Requires authentication. Users can only update their own profile.

**Request:**
```json
{
  "name": "Jane Doe"
}
```

**Response 200:** Returns updated user object.

**Errors:** 401, 403, 404, 422

---

## Rate Limits

| Endpoint Group | Limit |
|---------------|-------|
| Auth endpoints | 10 requests / minute |
| Read endpoints | 100 requests / minute |
| Write endpoints | 30 requests / minute |

## Endpoint Change Log

| Date | Endpoint | Change | Sprint |
|------|----------|--------|--------|
| {{DATE}} | — | Initial document created | 1 |

---
*Owner: Backend Lead — auto-updated when API files change. Review and verify accuracy after each auto-update.*
