from fastapi import FastAPI

from app.api.auth.router import router as auth_router
from app.api.v1.finance.router import router as finance_router
from app.api.v1.stats.router import router as stats_router
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.request_id import RequestIDMiddleware

app = FastAPI(title="MathAPI", version="0.1.0")

app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)

app.include_router(auth_router)
app.include_router(finance_router)
app.include_router(stats_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
