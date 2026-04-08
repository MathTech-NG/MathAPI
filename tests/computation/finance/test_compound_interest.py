from app.computation.finance.compound_interest import calculate_compound_interest


def test_calculate_compound_interest():
    final_amount, interest_earned = calculate_compound_interest(1000, 0.1, 2)
    assert round(final_amount, 2) == 1210.0
    assert round(interest_earned, 2) == 210.0
