def calculate_roi(gain: float, cost: float) -> tuple[float, float]:
    net_profit = gain - cost
    roi_percent = (net_profit / cost) * 100
    return net_profit, roi_percent
