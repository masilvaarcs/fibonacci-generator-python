import pytest
from fibonacci import fibonacci_generator, fibonacci_list


def test_first_ten():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_list(10) == expected


def test_single():
    assert fibonacci_list(1) == [0]


def test_empty():
    assert fibonacci_list(0) == []


def test_generator_is_infinite():
    gen = fibonacci_generator()
    for _ in range(1000):
        next(gen)
    val = next(gen)
    assert isinstance(val, int)
    assert val > 0
