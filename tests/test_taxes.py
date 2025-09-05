import pytest

from main import calculate_taxes

@pytest.fixture
def valid_prices():
    return [100, 200, 300]


@pytest.mark.parametrize("tax_rate, expected", [
    (10, [110, 220, 330]),
    (20, [120, 240, 360]),
    (50, [150, 300, 450])
])
def test_calculate_taxes_valid_values(valid_prices, tax_rate, expected):
    assert calculate_taxes(valid_prices, tax_rate) == expected


def test_calculate_taxes_invalid_taxes(valid_prices):
    with pytest.raises(ValueError) as negative_msg:
        calculate_taxes(valid_prices, -10)
    assert str(negative_msg.value) == 'Неверный налоговый процент'


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError) as zero_price_msg:
        calculate_taxes([0.0, -1], 10.0)
    assert str(zero_price_msg.value) == 'Неверная цена'
