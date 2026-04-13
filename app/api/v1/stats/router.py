from fastapi import APIRouter

from app.api.v1.stats.schemas import (
    CorrelationRequest,
    CorrelationResponse,
    MovingAverageRequest,
    MovingAverageResponse,
    PercentilesRequest,
    PercentilesResponse,
    SummaryRequest,
    SummaryResponse,
)
from app.computation.stats.correlation import calculate_correlation
from app.computation.stats.moving_average import calculate_moving_average
from app.computation.stats.percentiles import calculate_percentiles
from app.computation.stats.summary import summary_stats

router = APIRouter(prefix="/v1/stats", tags=["stats"])


@router.post("/summary", response_model=SummaryResponse)
def summary(payload: SummaryRequest) -> SummaryResponse:
    result = summary_stats(payload.values)
    return SummaryResponse(**result)


@router.post("/percentiles", response_model=PercentilesResponse)
def percentiles(payload: PercentilesRequest) -> PercentilesResponse:
    result = calculate_percentiles(payload.values)
    return PercentilesResponse(**result)


@router.post("/moving-average", response_model=MovingAverageResponse)
def moving_average(payload: MovingAverageRequest) -> MovingAverageResponse:
    result = calculate_moving_average(values=payload.values, window=payload.window)
    return MovingAverageResponse(result=result)


@router.post("/correlation", response_model=CorrelationResponse)
def correlation(payload: CorrelationRequest) -> CorrelationResponse:
    coefficient = calculate_correlation(x=payload.x, y=payload.y)
    return CorrelationResponse(coefficient=coefficient)
