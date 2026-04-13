def calculate_break_even(
    fixed_costs: float, price_per_unit: float, variable_cost_per_unit: float
) -> dict[str, float]:
    contribution_margin = price_per_unit - variable_cost_per_unit
    units = fixed_costs / contribution_margin
    revenue = units * price_per_unit
    return {"units": units, "revenue": revenue, "contribution_margin": contribution_margin}
