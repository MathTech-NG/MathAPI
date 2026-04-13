def calculate_correlation(x: list[float], y: list[float]) -> float:
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom_x = sum((v - mean_x) ** 2 for v in x) ** 0.5
    denom_y = sum((v - mean_y) ** 2 for v in y) ** 0.5
    if denom_x == 0 or denom_y == 0:
        return 0.0
    return numerator / (denom_x * denom_y)
