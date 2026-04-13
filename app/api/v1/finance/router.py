from fastapi import APIRouter

from app.api.v1.finance.schemas import (
    BreakEvenRequest,
    BreakEvenResponse,
    CompoundInterestRequest,
    CompoundInterestResponse,
    ROIRequest,
    ROIResponse,
)
from app.computation.finance.break_even import calculate_break_even
from app.computation.finance.compound_interest import calculate_compound_interest
from app.computation.finance.roi import calculate_roi

router = APIRouter(prefix="/v1/finance", tags=["finance"])


@router.post("/compound-interest", response_model=CompoundInterestResponse)
def compound_interest(payload: CompoundInterestRequest) -> CompoundInterestResponse:
    final_amount, interest_earned = calculate_compound_interest(
        principal=payload.principal,
        rate=payload.rate,
        periods=payload.periods,
    )
    return CompoundInterestResponse(final_amount=final_amount, interest_earned=interest_earned)


@router.post("/roi", response_model=ROIResponse)
def roi(payload: ROIRequest) -> ROIResponse:
    net_profit, roi_percent = calculate_roi(gain=payload.gain, cost=payload.cost)
    return ROIResponse(net_profit=net_profit, roi_percent=roi_percent)


@router.post("/break-even", response_model=BreakEvenResponse)
def break_even(payload: BreakEvenRequest) -> BreakEvenResponse:
    result = calculate_break_even(
        fixed_costs=payload.fixed_costs,
        price_per_unit=payload.price_per_unit,
        variable_cost_per_unit=payload.variable_cost_per_unit,
    )
    return BreakEvenResponse(**result)
