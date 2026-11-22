from random import Random

import pytest

from algopack.errors import ArgTypeError
from algopack.selection_sort import selection_sort


def test_empty():
    assert selection_sort([]) == []


def test_single_element():
    assert selection_sort([5]) == [5]


def test_sorted_and_reversed():
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates_and_negative():
    assert selection_sort([3, -2, 3, 0, -5]) == [-5, -2, 0, 3, 3]


def test_original_list():
    numbers = [5, 3, 1, 4]
    result = selection_sort(numbers)

    assert result == [1, 3, 4, 5]
    assert numbers == [5, 3, 1, 4]
    assert result is not numbers


def test_tuple():
    assert selection_sort((4, 1, 3)) == [1, 3, 4]


def test_random_arrays():
    rng = Random(42)

    for i in range(20):
        numbers = [rng.randint(-100, 100) for i in range(50)]
        assert selection_sort(numbers) == sorted(numbers)


def test_invalid_type():
    with pytest.raises(ArgTypeError):
        selection_sort("123")
