---
last_updated: {{DATE}}
changed: Initial document created
updated_by: Tech Lead / Architect
sprint: 0
---

# High Level Design — {{PROJECT_NAME}}

> View System Architecture Diagram → [system-architecture.html](../diagrams/system-architecture.html)
> View Sequence Diagram → [sequence-diagram.html](../diagrams/sequence-diagram.html)
> View Data Flow Diagram → [data-flow.html](../diagrams/data-flow.html)

## System Overview

{{PROJECT_NAME}} is a {{PROJECT_TYPE}} application built on {{STACK}}. It follows a [monolith / microservices / serverless] architecture.

[One paragraph describing the system's core purpose and how its components work together. Written for someone who needs a quick mental model.]

## Architecture Diagram

> [View interactive diagram](../diagrams/system-architecture.html)

```
[Paste a simple ASCII representation here as a fallback]

Client → API Gateway → [Service A] → Database
                    → [Service B] → Cache
                    → [Service C] → External API
```

## Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Frontend | {{FRONTEND_STACK}} | User interface |
| API Layer | {{BACKEND_STACK}} | Business logic + data access |
| Database | {{DB_STACK}} | Persistent data storage |
| Cache | [Redis / Memcached / N/A] | Session + hot data caching |
| Auth | [JWT / OAuth2 / Session] | Authentication + authorization |
| File Storage | [S3 / GCS / Local] | Media + document storage |

## Data Flow

> [View interactive data flow diagram](../diagrams/data-flow.html)

1. User sends request via [browser / mobile app]
2. Request hits [API Gateway / Load Balancer / Direct]
3. [Describe the main request path through the system]
4. Response returns to client

## Key Design Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| [e.g. Database type] | [PostgreSQL] | [Why — ACID compliance, relational data] |
| [e.g. Auth strategy] | [JWT] | [Why — stateless, scales horizontally] |
| [e.g. Caching layer] | [Redis] | [Why — session management + rate limiting] |

## External Dependencies

| Service | Purpose | Critical? |
|---------|---------|-----------|
| [e.g. Stripe] | Payment processing | Yes |
| [e.g. SendGrid] | Transactional email | Yes |
| [e.g. Cloudinary] | Image processing | No |

## Security Considerations

- Authentication: [How users authenticate]
- Authorization: [How permissions are enforced]
- Data encryption: [At rest and in transit]
- Secrets management: [How API keys and credentials are stored]

## Scalability

- Expected load: [X requests/second at peak]
- Scaling strategy: [Horizontal / Vertical / Auto-scaling]
- Bottlenecks identified: [Known constraints]

---
*Owner: Tech Lead / Architect — update when a new service, major module, or architectural decision changes.*
