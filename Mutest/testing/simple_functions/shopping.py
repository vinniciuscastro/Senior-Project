# file: testing/simple_functions/shopping.py
"""
Shopping utility functions for calculating totals and applying discounts.
"""


def calculate_total(prices):
    """Calculate the total of a list of prices."""
    if not prices:
        return 0.0
    return sum(prices)


def apply_bulk_discount(total, item_count):
    """Apply bulk discount based on item count."""
    if item_count >= 10:
        return total * 0.8  # 20% off for 10+ items
    elif item_count >= 5:
        return total * 0.9  # 10% off for 5-9 items
    else:
        return total


def calculate_shipping(total):
    """Calculate shipping cost based on order total."""
    if total >= 100:
        return 0.0  # Free shipping over $100
    elif total >= 50:
        return 5.0  # $5 shipping for $50-$99
    else:
        return 10.0  # $10 shipping for under $50


def is_eligible_for_coupon(total, customer_type):
    """Check if customer is eligible for a coupon."""
    if customer_type == "premium":
        return total >= 25
    elif customer_type == "regular":
        return total >= 50
    else:
        return False
