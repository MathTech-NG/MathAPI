from app.computation.stats.summary import summary_stats


def test_summary_stats():
    result = summary_stats([1, 2, 3, 4])
    assert result["count"] == 4
    assert result["mean"] == 2.5
