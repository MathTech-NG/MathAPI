# MathAPI

A multi-tenant mathematical computation API for developers.

MathAPI exposes financial and statistical computation as clean, authenticated, rate-limited HTTP endpoints. Developers create an account, get an API key, and start calling production-grade math endpoints immediately — no library setup, no numerical edge-case handling, no integration overhead.

Built as part of the **#ENg30DayChallenge** — Backend + DevOps Track.

---

## What It Does

Most startups that need math in their product either hardcode fragile formulas, pull in heavy scientific libraries and manage the integration themselves, or skip the feature entirely. MathAPI removes that friction. Pass in your data as JSON, get back a structured, validated result.

---

## Domains

### Financial Mathematics

| Endpoint                             | Description                                                 |
| ------------------------------------ | ----------------------------------------------------------- |
| `POST /v1/finance/compound-interest` | Final amount and interest earned over n periods             |
| `POST /v1/finance/amortization`      | Full payment schedule broken down by principal and interest |
| `POST /v1/finance/npv`               | Net present value of a future cash flow series              |
| `POST /v1/finance/irr`               | Internal rate of return for an investment                   |
| `POST /v1/finance/break-even`        | Break-even units and revenue at a given cost structure      |
| `POST /v1/finance/roi`               | Return on investment with annualized breakdown              |

### Statistics & Data Analysis

| Endpoint                           | Description                                        |
| ---------------------------------- | -------------------------------------------------- |
| `POST /v1/stats/summary`           | Mean, median, std dev, skewness, kurtosis, range   |
| `POST /v1/stats/regression/linear` | Slope, intercept, R², and predicted values         |
| `POST /v1/stats/correlation`       | Pearson correlation matrix for a dataset           |
| `POST /v1/stats/outliers`          | Flagged outliers using IQR and Z-score methods     |
| `POST /v1/stats/moving-average`    | SMA and EMA series for a given window size         |
| `POST /v1/stats/percentiles`       | Value at each percentile with distribution summary |

---

## Platform Features

- Account registration and login
- API key generation, listing, and revocation
- Per-key usage tracking (request count, last used, domain breakdown)
- Rate limiting per API key with sliding window enforcement
- Caching for deterministic computation results
- Structured JSON error responses with machine-readable error codes
- Per-request tracing via unique request IDs
- Health check endpoint at `/health`
- API documentation at `/docs`

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker and Docker Compose

### Run Locally

```bash
git clone https://github.com/your-username/mathapi.git
cd mathapi
cp .env.example .env
docker compose up --build
```

The API will be available at `http://localhost:8000`.
Documentation will be available at `http://localhost:8000/docs`.

### Run Without Docker

```bash
py -3.12 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Development

```bash
source venv/Scripts/activate
pip install -r requirements-dev.txt
ruff check .
ruff format .
pytest -q
```

---

## Environment Variables

| Variable         | Description                                        |
| ---------------- | -------------------------------------------------- |
| `DATABASE_URL`   | PostgreSQL connection string                       |
| `REDIS_URL`      | Redis connection string                            |
| `SECRET_KEY`     | Secret key for signing tokens                      |
| `API_RATE_LIMIT` | Max requests per minute per API key (default: 100) |
| `ENVIRONMENT`    | `development`, `staging`, or `production`          |

See `.env.example` for a full reference.

---

## Project Structure

```mk
mathapi/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── finance/
│   │   │   └── stats/
│   │   └── auth/
│   ├── core/
│   ├── computation/
│   │   ├── finance/
│   │   └── stats/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── docker/
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

---

## API Usage Example

### Register and get an API key

```bash
curl -X POST http://localhost:8000/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com", "password": "yourpassword"}'
```

### Call a computation endpoint

```bash
curl -X POST http://localhost:8000/v1/finance/compound-interest \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "principal": 10000,
    "rate": 0.05,
    "periods": 12,
    "frequency": "monthly"
  }'
```

---

## Commit Convention

This project follows conventional commits.

```mk
feat:     new feature or endpoint
fix:      bug fix
chore:    tooling, config, dependencies
test:     adding or updating tests
docs:     documentation only
refactor: code change with no feature or fix
ci:       CI/CD pipeline changes
```

---

## Challenge

Built during the **ENg 30-Day Build in Public Challenge** — Hard Mode.

Track: Backend + DevOps
Hashtags: `#ENg30DayChallenge` `#ENgShipIt`

---

## License

MIT
