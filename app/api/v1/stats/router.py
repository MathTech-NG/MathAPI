from fastapi import APIRouter

from app.api.v1.stats.schemas import SummaryRequest, SummaryResponse
from app.computation.stats.summary import summary_stats

router = APIRouter(prefix="/v1/stats", tags=["stats"])


@router.post("/summary", response_model=SummaryResponse)
def summary(payload: SummaryRequest) -> SummaryResponse:
    result = summary_stats(payload.values)
    return SummaryResponse(**result)
