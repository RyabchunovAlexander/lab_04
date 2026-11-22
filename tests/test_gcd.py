import pytest

from algopack.errors import ArgTypeError, GCDError
from algopack.gcd import gcd_iterative, gcd_recursive


def test_iterative():
    assert gcd_iterative(48, 18) == 6
    assert gcd_iterative(1071, 462) == 21
    assert gcd_iterative(13, 17) == 1
    assert gcd_iterative(7, 7) == 7


def test_recursive():
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(1071, 462) == 21
    assert gcd_recursive(13, 17) == 1
    assert gcd_recursive(7, 7) == 7


def test_negative_numbers():
    assert gcd_iterative(-48, 18) == 6
    assert gcd_iterative(-48, -18) == 6
    assert gcd_recursive(48, -18) == 6
    assert gcd_recursive(-48, -18) == 6


def test_zero():
    assert gcd_iterative(0, 7) == 7
    assert gcd_iterative(7, 0) == 7
    assert gcd_recursive(0, 7) == 7
    assert gcd_recursive(7, 0) == 7


def test_invalid_types():
    with pytest.raises(ArgTypeError):
        gcd_iterative(5.5, 2)

    with pytest.raises(ArgTypeError):
        gcd_recursive("12", 4)

    with pytest.raises(ArgTypeError):
        gcd_iterative(True, 5)


def test_zero_zero():
    with pytest.raises(GCDError):
        gcd_iterative(0, 0)

    with pytest.raises(GCDError):
        gcd_recursive(0, 0)
