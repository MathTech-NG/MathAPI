def calculate_moving_average(values: list[float], window: int) -> list[float]:
    return [sum(values[i : i + window]) / window for i in range(len(values) - window + 1)]
