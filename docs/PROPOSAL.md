# MathAPI — Project Proposal

**Challenge:** ENg 30-Day Build in Public Challenge (Hard Mode)
**Track:** Backend + DevOps
**Hashtags:** #ENg30DayChallenge #ENgShipIt

---

## 1. The Problem

Startups that need mathematical computation in their product face a frustrating choice. They can hardcode formulas, which breaks the moment requirements change. They can pull in heavy scientific libraries, which means setting up a runtime environment, managing dependencies, and writing the integration layer themselves. Or they skip the feature entirely and ship a worse product.

There is no clean, developer-friendly API they can call in five minutes and have a working amortization schedule or outlier detection result by end of day. Financial and statistical computation is genuinely needed by fintech products, analytics tools, SaaS dashboards, and logistics platforms, but the infrastructure to consume it as a service does not exist at the developer level.

MathAPI closes that gap.

---

## 2. What Is Being Built

MathAPI is a multi-tenant REST API platform. A developer creates an account, receives an API key, and can immediately start calling mathematical computation endpoints, passing in their data as JSON and receiving structured, validated results.

The platform handles everything the developer should not have to think about: authentication, key management, rate limiting, caching of deterministic results, and structured error responses. The developer's only job is to call the endpoint and use the result.

Under the hood, the computation layer wraps battle-tested open-source mathematical libraries behind clean, versioned HTTP endpoints. The mathematical correctness is delegated to those libraries. The product is the infrastructure, the developer experience, and the reliability layer built around them.

---

## 3. Scope

MathAPI covers two computation domains, chosen for their direct relevance to startup products and for having the clearest, most immediate use cases for early-stage founders.

### 3.1 Domain 1: Financial Mathematics

Six endpoints covering the core financial calculations that fintech products, SaaS pricing tools, and investor dashboards need to ship real features.

| Endpoint | What It Returns | Who Needs This |
|---|---|---|
| `POST /v1/finance/compound-interest` | Final amount and interest earned over n periods | Savings tools, lending apps |
| `POST /v1/finance/amortization` | Full payment schedule broken down by principal and interest per period | Loan calculators, fintech products |
| `POST /v1/finance/npv` | Net present value of a future cash flow series | Startup financial modeling |
| `POST /v1/finance/irr` | Internal rate of return for an investment | Investor dashboards, cap table tools |
| `POST /v1/finance/break-even` | Break-even units and revenue at a given cost structure | Early-stage SaaS pricing tools |
| `POST /v1/finance/roi` | Return on investment with annualized breakdown | Marketing, ops, product analytics |

### 3.2 Domain 2: Statistics & Data Analysis

Six endpoints covering the statistical operations that analytics products, data dashboards, and any startup working with user metrics will need.

| Endpoint | What It Returns | Who Needs This |
|---|---|---|
| `POST /v1/stats/summary` | Mean, median, std dev, skewness, kurtosis, range | Any analytics dashboard |
| `POST /v1/stats/regression/linear` | Slope, intercept, R², and predicted values | Growth forecasting, trend analysis |
| `POST /v1/stats/correlation` | Pearson correlation matrix for a dataset | Feature analysis, business metrics |
| `POST /v1/stats/outliers` | Flagged outliers using IQR and Z-score methods | Fraud detection, data quality checks |
| `POST /v1/stats/moving-average` | SMA and EMA series for a given window size | Time-series dashboards, stock tools |
| `POST /v1/stats/percentiles` | Value at each percentile with distribution summary | User cohorts, performance benchmarks |

### 3.3 Platform Features

Beyond the computation endpoints, the following platform features are in scope and are required for the API to be considered production-ready:

- Account registration and login
- API key generation, listing, and revocation
- Per-key usage tracking (request count, last used, domain breakdown)
- Rate limiting per API key, sliding window, enforced at the request layer
- Caching for deterministic computation results
- Structured JSON error responses with machine-readable error codes
- Request logging with unique request IDs for traceability
- Health check endpoint
- API documentation hosted at `/docs`

---

## 4. Must-Haves

### 4.1 Backend Track Requirements

| Track Requirement | Implementation in MathAPI | Status |
|---|---|---|
| Production-ready API | Versioned endpoints (/v1/), structured error responses, input validation, API documentation | Must Have |
| Authentication + Authorization | Account registration, API key issuance, key-based request auth, per-key permission scopes | Must Have |
| Real database | Relational database storing accounts, API keys, request logs, and usage metrics | Must Have |
| 5+ meaningful tests | Unit tests per computation module plus integration tests for auth and rate limiting flows | Must Have |
| Rate limiting (Bonus) | Sliding window rate limiter per API key enforced at the request layer | Must Have |
| Caching (Bonus) | In-memory cache for deterministic results. Same inputs return a cached response with measurable latency improvement. | Must Have |
| Logging (Bonus) | Structured JSON logs with per-request tracing via unique request ID | Must Have |

### 4.2 DevOps Track Requirements

| DevOps Requirement | Implementation in MathAPI |
|---|---|
| Containerization | The full application stack is containerized and runs as isolated services. Any reviewer can clone the repository and bring up a working instance from scratch with a single command. |
| CI/CD Pipeline | A fully automated pipeline runs on every push: code is linted, tests are executed, the build is verified, and a passing build on the main branch triggers an automatic deployment. |
| Cloud Deployment | The API is deployed to a live, publicly accessible URL by Day 30. The deployment is not local and not a demo environment. |
| Environment Configuration | All environment-specific values are managed through environment variables. No secrets are hardcoded. The configuration is reproducible across local, staging, and production environments. |
| Health and Uptime Monitoring | A dedicated health check endpoint exposes the live status of the API and its dependent services. Uptime is monitored externally and verifiable. |
| Observability | Structured logs are emitted on every request with a unique request ID, status, latency, and endpoint. |
| Zero-Downtime Deployment | The CI/CD pipeline is configured such that deploying a new version does not drop live traffic. Deployments are atomic and rollback-capable. |
| Security Hardening | The API runs as a non-root process inside its container. Sensitive headers are stripped from responses. Rate limiting is enforced at the infrastructure layer, not just application code. |

---

## 5. Measurable Output

Every deliverable below is observable, testable, or demonstrable. Nothing exists only as documentation or theory.

| Deliverable | How It Is Verified |
|---|---|
| 12 live computation endpoints across 2 domains | Publicly accessible API returning valid responses on Day 30 |
| Account and API key system | New user can register, receive a key, and hit an endpoint end-to-end |
| Rate limiting enforced per key | 429 response returned when limit is exceeded, demonstrable live |
| Caching active on computation endpoints | Response headers expose cache hit/miss status with measurable latency difference |
| Test suite passing in CI | CI pipeline badge is green and test run is visible in the public repository |
| Containerized and reproducible | Any reviewer can clone the repository and bring up a working instance with a single command |
| Live cloud deployment | Public base URL accessible from any network with external uptime monitoring active |
| API documentation | All endpoints documented and browsable at /docs with request and response schemas |
| Structured logging and observability | Every request produces a structured log entry with request ID, status, and latency |
| Consistent commit history | 30 days of commits visible on the public repository with no bulk uploads |

On Day 30, a reviewer should be able to: register an account via the API, receive an API key, call any of the 12 computation endpoints and receive a valid result, exceed the rate limit and receive a 429, observe cache hit headers on a repeated call, and view the full API documentation at /docs, all against a live public URL.
