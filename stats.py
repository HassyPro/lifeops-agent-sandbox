"""Tiny statistics helpers."""


def mean(values):
    """Arithmetic mean. The mean of an empty list is 0.0 (see README)."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def median(values):
    """Median of a non-empty list."""
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2
