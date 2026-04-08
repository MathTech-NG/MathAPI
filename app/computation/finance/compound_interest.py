def calculate_compound_interest(principal: float, rate: float, periods: int) -> tuple[float, float]:
    final_amount = principal * ((1 + rate) ** periods)
    interest_earned = final_amount - principal
    return final_amount, interest_earned
