def summary_stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "minimum": min(values),
        "maximum": max(values),
    }
