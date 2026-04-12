from app.computation.finance.roi import calculate_roi


def test_calculate_roi_profit():
    net_profit, roi_percent = calculate_roi(gain=1500, cost=1000)
    assert net_profit == 500.0
    assert roi_percent == 50.0


def test_calculate_roi_loss():
    net_profit, roi_percent = calculate_roi(gain=800, cost=1000)
    assert net_profit == -200.0
    assert roi_percent == -20.0


def test_calculate_roi_breakeven():
    net_profit, roi_percent = calculate_roi(gain=1000, cost=1000)
    assert net_profit == 0.0
    assert roi_percent == 0.0
