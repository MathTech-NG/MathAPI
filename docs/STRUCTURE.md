# MathAPI — Project Structure

```
mathapi/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── finance/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── router.py          # Route definitions for all /v1/finance/* endpoints
│   │   │   │   └── schemas.py         # Request and response models for finance endpoints
│   │   │   ├── stats/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── router.py          # Route definitions for all /v1/stats/* endpoints
│   │   │   │   └── schemas.py         # Request and response models for stats endpoints
│   │   │   └── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── router.py              # Register, login, key management endpoints
│   │   │   └── schemas.py             # Auth request and response models
│   │   └── __init__.py
│   │
│   ├── computation/
│   │   ├── finance/
│   │   │   ├── __init__.py
│   │   │   ├── compound_interest.py   # Pure computation logic — no HTTP concerns
│   │   │   ├── amortization.py
│   │   │   ├── npv.py
│   │   │   ├── irr.py
│   │   │   ├── break_even.py
│   │   │   └── roi.py
│   │   ├── stats/
│   │   │   ├── __init__.py
│   │   │   ├── summary.py
│   │   │   ├── linear_regression.py
│   │   │   ├── correlation.py
│   │   │   ├── outliers.py
│   │   │   ├── moving_average.py
│   │   │   └── percentiles.py
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                  # Environment variable loading and validation
│   │   ├── security.py                # API key hashing, validation logic
│   │   ├── rate_limiter.py            # Sliding window rate limiting implementation
│   │   ├── cache.py                   # Cache read/write abstraction
│   │   ├── logging.py                 # Structured JSON logger setup
│   │   └── dependencies.py            # FastAPI shared dependencies (auth, db session, etc.)
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py                 # Database session factory
│   │   └── base.py                    # Base model class
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                    # User account table
│   │   ├── api_key.py                 # API key table
│   │   └── request_log.py             # Per-request log table for usage tracking
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py            # Account creation, login, key issuance logic
│   │   └── usage_service.py           # Usage tracking and quota checking
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── request_id.py              # Attach unique request ID to every request
│   │   └── logging_middleware.py      # Log every request with status and latency
│   │
│   └── main.py                        # App entrypoint — register routers, middleware, startup
│
├── alembic/
│   ├── versions/                      # Auto-generated migration files
│   ├── env.py
│   └── alembic.ini
│
├── tests/
│   ├── computation/
│   │   ├── finance/
│   │   │   └── test_compound_interest.py
│   │   └── stats/
│   │       └── test_summary.py
│   ├── api/
│   │   ├── test_auth.py
│   │   └── test_rate_limiting.py
│   └── conftest.py                    # Shared fixtures (test client, test DB, etc.)
│
├── docker/
│   ├── api.Dockerfile                 # Production image for the API
│   └── worker.Dockerfile              # If background workers are added later
│
├── .github/
│   └── workflows/
│       └── ci.yml                     # Lint, test, build, deploy pipeline
│
├── .env.example                       # All required env vars with placeholder values
├── .gitignore
├── docker-compose.yml                 # Local dev: API + database + cache
├── docker-compose.prod.yml            # Production overrides
├── Dockerfile                         # Defaults to api.Dockerfile
├── requirements.txt                   # Production dependencies
├── requirements-dev.txt               # Dev and test dependencies
├── PROPOSAL.md
└── README.md
```

---

## Key Design Decisions

**`app/computation/` is completely isolated from HTTP.**
Every computation module is a pure function: takes validated inputs, returns a result. No FastAPI imports, no database calls, no request objects. This makes them trivially testable and replaceable.

**`app/api/` only handles HTTP concerns.**
Routers validate input via schemas, call the appropriate computation function or service, and return a response. No business logic lives here.

**`app/core/` owns cross-cutting infrastructure.**
Rate limiting, caching, logging, security, and config all live here. They are shared across the entire app but belong to no single domain.

**`app/services/` owns business logic that crosses models.**
Auth and usage tracking involve multiple models and side effects. They belong in services, not in routers and not in models.

**Migrations are first-class.**
Alembic is set up from Day 1. No `create_all()` in production.
