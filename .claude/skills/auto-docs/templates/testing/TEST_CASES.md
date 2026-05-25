---
last_updated: {{DATE}}
changed: Initial document created
updated_by: QA Team
sprint: 1
---

# Test Cases — {{PROJECT_NAME}}

## How to Read This Document

| Column | Meaning |
|--------|---------|
| ID | Unique test identifier — never reused |
| Precondition | What must be true before the test starts |
| Steps | Exact actions to perform |
| Expected Result | What should happen |
| Status | Pass / Fail / Blocked / Not Run |

---

## Authentication

### TC-AUTH-001 — Register with valid credentials

**Story:** 1.1
**Priority:** Critical

| Field | Value |
|-------|-------|
| Precondition | User is not registered. App is on the registration page. |
| Steps | 1. Enter valid email. 2. Enter password meeting requirements. 3. Enter name. 4. Click Register. |
| Expected Result | Account created. Verification email sent within 60 seconds. User sees confirmation message. |
| Status | Not Run |

---

### TC-AUTH-002 — Register with existing email

**Story:** 1.1
**Priority:** Critical

| Field | Value |
|-------|-------|
| Precondition | Email already registered in the system. |
| Steps | 1. Enter registered email. 2. Enter any password. 3. Click Register. |
| Expected Result | Error message: "An account with this email already exists." No email sent. |
| Status | Not Run |

---

### TC-AUTH-003 — Login with valid credentials

**Story:** 1.2
**Priority:** Critical

| Field | Value |
|-------|-------|
| Precondition | User is registered and email is verified. |
| Steps | 1. Enter correct email. 2. Enter correct password. 3. Click Login. |
| Expected Result | User redirected to dashboard. Auth token stored. |
| Status | Not Run |

---

### TC-AUTH-004 — Login with wrong password

**Story:** 1.2
**Priority:** Critical

| Field | Value |
|-------|-------|
| Precondition | User is registered. |
| Steps | 1. Enter correct email. 2. Enter wrong password. 3. Click Login. |
| Expected Result | Error: "Invalid email or password." Failed attempt count incremented. |
| Status | Not Run |

---

### TC-AUTH-005 — Account locks after 3 failed attempts

**Story:** 1.2
**Priority:** High

| Field | Value |
|-------|-------|
| Precondition | User is registered. |
| Steps | 1. Fail login 3 times with wrong password. |
| Expected Result | Account locked. Message shows: "Account locked. Try again after 15 minutes." |
| Status | Not Run |

---

## [Feature Area 2]

### TC-[AREA]-001 — [Test name]

**Story:** [X.X]
**Priority:** [Critical / High / Medium]

| Field | Value |
|-------|-------|
| Precondition | [What must be true] |
| Steps | 1. [Step 1] 2. [Step 2] |
| Expected Result | [What should happen] |
| Status | Not Run |

---

## Test Execution Summary

| Sprint | Total Cases | Passed | Failed | Blocked | Not Run |
|--------|------------|--------|--------|---------|---------|
| Sprint 1 | 5 | 0 | 0 | 0 | 5 |

---
*Owner: QA Team — add new test cases when user stories move to In Development.*
