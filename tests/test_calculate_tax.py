from src.calculate_tax import calculate_tax
import pytest

# @pytest.fixture
# def prices():
#     return [100, 200, 300]

@pytest.mark.parametrize("price, tax_rate, expected", [(100, 10, 110), (100, 20, 120), (100, 30, 130)])
def test_calculate_test_valid_values(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(price=-100, tax_rate=10)


def test_calculate_tax_invalid_tax():
    with pytest.raises(ValueError):
        calculate_tax(price=100, tax_rate=-10)
    with pytest.raises(ValueError):
        calculate_tax(price=100, tax_rate=100)
    with pytest.raises(ValueError):
        calculate_tax(price=100, tax_rate=110)

