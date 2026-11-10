import pytest
from app import calculate_total


def test_calculate_total():
    assert calculate_total(25.00, 3) == 75.00


def test_zero_quantity():
    assert calculate_total(25.00, 0) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-10, 2)


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total(10, -2)
