"""
Calculator module with weak test coverage.
This will demonstrate surviving mutants due to incomplete tests.
"""

def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


def calculate_tax(amount, tax_rate):
    """Calculate total with tax"""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")

    tax_amount = amount * tax_rate
    total = amount + tax_amount
    return total


def is_even(number):
    """Check if number is even"""
    return number % 2 == 0
