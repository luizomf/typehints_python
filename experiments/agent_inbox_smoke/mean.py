"""Small standalone arithmetic exercise for an agent-inbox integration test."""


def arithmetic_mean(values: tuple[float, ...]) -> float:
    """Return the arithmetic mean of a nonempty tuple."""
    if not values:
        message = "values must not be empty"
        raise ValueError(message)
    return sum(values) / len(values)
