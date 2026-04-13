def calculate_percentiles(values: list[float]) -> dict[str, float]:
    sorted_vals = sorted(values)
    n = len(sorted_vals)

    def percentile(p: float) -> float:
        idx = (p / 100) * (n - 1)
        lower, upper = int(idx), min(int(idx) + 1, n - 1)
        return sorted_vals[lower] + (idx - lower) * (sorted_vals[upper] - sorted_vals[lower])

    return {
        "p25": percentile(25),
        "p50": percentile(50),
        "p75": percentile(75),
        "p90": percentile(90),
        "p95": percentile(95),
    }
