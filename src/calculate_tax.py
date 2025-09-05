def calculate_tax(price: float, tax_rate: float) -> float:
    """"""
    if price <= 0:
        raise ValueError("Invalid price")
    if tax_rate <0 or tax_rate >= 100:
        raise ValueError("Invalid tax rate")
    return price + price * (tax_rate / 100)