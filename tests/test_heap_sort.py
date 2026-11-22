from random import Random

import pytest

from algopack.errors import ArgTypeError
from algopack.heap_sort import heap_sort


def test_empty():
    assert heap_sort([]) == []


def test_single_element():
    assert heap_sort([5]) == [5]


def test_sorted_and_reversed():
    assert heap_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert heap_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates_and_negative():
    assert heap_sort([3, -2, 3, 0, -5]) == [-5, -2, 0, 3, 3]


def test_original_list():
    numbers = [5, 3, 1, 4]
    result = heap_sort(numbers)

    assert result == [1, 3, 4, 5]
    assert numbers == [5, 3, 1, 4]
    assert result is not numbers


def test_tuple():
    assert heap_sort((4, 1, 3)) == [1, 3, 4]


def test_random_arrays():
    rng = Random(42)

    for _ in range(20):
        numbers = [rng.randint(-100, 100) for _ in range(100)]
        assert heap_sort(numbers) == sorted(numbers)


def test_large_reversed_array():
    numbers = list(range(2000, 0, -1))
    assert heap_sort(numbers) == sorted(numbers)


def test_invalid_type():
    with pytest.raises(ArgTypeError):
        heap_sort("123")
