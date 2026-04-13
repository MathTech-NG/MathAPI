from app.computation.stats.percentiles import calculate_percentiles


def test_percentiles_basic():
    result = calculate_percentiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result["p50"] == 5.5
    assert result["p25"] == 2.75
    assert result["p75"] == 7.75


def test_percentiles_uniform():
    result = calculate_percentiles([10.0] * 10)
    assert result["p25"] == 10.0
    assert result["p50"] == 10.0
    assert result["p95"] == 10.0
