from pydantic import BaseModel, Field


class CompoundInterestRequest(BaseModel):
    principal: float = Field(gt=0)
    rate: float = Field(gt=0)
    periods: int = Field(gt=0)


class CompoundInterestResponse(BaseModel):
    final_amount: float
    interest_earned: float


class ROIRequest(BaseModel):
    gain: float = Field(gt=0, description="Total value received from the investment")
    cost: float = Field(gt=0, description="Total cost of the investment")


class ROIResponse(BaseModel):
    net_profit: float
    roi_percent: float
