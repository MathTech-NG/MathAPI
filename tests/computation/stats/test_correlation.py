from app.computation.stats.correlation import calculate_correlation


def test_perfect_positive_correlation():
    result = calculate_correlation([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    assert round(result, 6) == 1.0


def test_perfect_negative_correlation():
    result = calculate_correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    assert round(result, 6) == -1.0


def test_no_correlation():
    result = calculate_correlation([1, 2, 3, 4, 5], [3, 3, 3, 3, 3])
    assert result == 0.0
