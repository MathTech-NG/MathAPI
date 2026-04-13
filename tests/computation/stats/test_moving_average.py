from app.computation.stats.moving_average import calculate_moving_average


def test_moving_average_window_3():
    result = calculate_moving_average([1, 2, 3, 4, 5], window=3)
    assert result == [2.0, 3.0, 4.0]


def test_moving_average_window_2():
    result = calculate_moving_average([10, 20, 30, 40], window=2)
    assert result == [15.0, 25.0, 35.0]


def test_moving_average_full_window():
    result = calculate_moving_average([4, 8], window=2)
    assert result == [6.0]
