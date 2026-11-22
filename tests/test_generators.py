import pytest

from algopack.errors import ArgTypeError, ArgValueError
from algopack.generators import (
    generate_almost_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
    generate_with_duplicates,
)


def test_empty_and_length():
    generators = [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates
    ]

    for generator in generators:
        assert generator(0, seed=42) == []

        numbers = generator(
            30, seed=42, low_bound=-5, high_bound=5
        )

        assert len(numbers) == 30
        assert all(-5 <= x <= 5 for x in numbers)


def test_sorted_and_reversed():
    numbers = generate_sorted(100, seed=42)
    assert numbers == sorted(numbers)

    numbers = generate_reversed(100, seed=42)
    assert numbers == sorted(numbers, reverse=True)


def test_almost_sorted():
    numbers = generate_almost_sorted(100, seed=42)
    original = generate_sorted(100, seed=42)

    assert sorted(numbers) == original

    differences = sum(
        a != b for a, b in zip(numbers, original)
    )
    assert differences <= 10


def test_duplicates():
    numbers = generate_with_duplicates(
        100, seed=42, unique_count=3
    )

    assert len(numbers) == 100
    assert len(set(numbers)) <= 3


def test_seed():
    generators = [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates
    ]

    for generator in generators:
        assert generator(100, seed=42) == generator(100, seed=42)

    assert generate_random(100, seed=1) != generate_random(100, seed=2)


def test_invalid_arguments():
    with pytest.raises(ArgTypeError):
        generate_random("10")

    with pytest.raises(ArgValueError):
        generate_sorted(-1)

    with pytest.raises(ArgValueError):
        generate_reversed(5, low_bound=10, high_bound=2)

    with pytest.raises(ArgValueError):
        generate_with_duplicates(10, unique_count=0)

    with pytest.raises(ArgTypeError):
        generate_almost_sorted(10, seed="x")
