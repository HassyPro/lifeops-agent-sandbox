from stats import mean, median


def test_mean():
    assert mean([1, 2, 3]) == 2


def test_median_odd_and_even():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5


def test_mean_empty_returns_zero():
    assert mean([]) == 0.0
