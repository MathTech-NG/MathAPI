from fastapi import APIRouter

from app.api.v1.finance.schemas import CompoundInterestRequest, CompoundInterestResponse
from app.computation.finance.compound_interest import calculate_compound_interest

router = APIRouter(prefix="/v1/finance", tags=["finance"])


@router.post("/compound-interest", response_model=CompoundInterestResponse)
def compound_interest(payload: CompoundInterestRequest) -> CompoundInterestResponse:
    final_amount, interest_earned = calculate_compound_interest(
        principal=payload.principal,
        rate=payload.rate,
        periods=payload.periods,
    )
    return CompoundInterestResponse(final_amount=final_amount, interest_earned=interest_earned)
