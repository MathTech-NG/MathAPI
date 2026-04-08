from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    values: list[float] = Field(min_length=1)


class SummaryResponse(BaseModel):
    count: int
    mean: float
    minimum: float
    maximum: float
