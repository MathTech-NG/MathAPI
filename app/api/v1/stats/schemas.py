from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    values: list[float] = Field(min_length=1)


class SummaryResponse(BaseModel):
    count: int
    mean: float
    minimum: float
    maximum: float


class PercentilesRequest(BaseModel):
    values: list[float] = Field(min_length=2)


class PercentilesResponse(BaseModel):
    p25: float
    p50: float
    p75: float
    p90: float
    p95: float
