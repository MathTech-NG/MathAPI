from app.computation.finance.break_even import calculate_break_even


def test_break_even_units():
    result = calculate_break_even(fixed_costs=10000, price_per_unit=50, variable_cost_per_unit=30)
    assert result["units"] == 500.0
    assert result["revenue"] == 25000.0
    assert result["contribution_margin"] == 20.0


def test_break_even_high_margin():
    result = calculate_break_even(fixed_costs=5000, price_per_unit=100, variable_cost_per_unit=20)
    assert result["units"] == 62.5
    assert result["contribution_margin"] == 80.0
