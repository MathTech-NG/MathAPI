from pydantic import BaseModel, Field


class CompoundInterestRequest(BaseModel):
    principal: float = Field(gt=0)
    rate: float = Field(gt=0)
    periods: int = Field(gt=0)


class CompoundInterestResponse(BaseModel):
    final_amount: float
    interest_earned: float
