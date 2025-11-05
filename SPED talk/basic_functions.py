"""
EXAMPLE 1: Basic Unit Tests with Pytest
========================================
This example shows the fundamentals of writing unit tests.
Each function does ONE thing, and each test verifies ONE behavior.
"""

# ============================================================================
# CODE TO TEST (The functions we're testing)
# ============================================================================

def add(a, b):
    """Add two numbers"""
    return a + b


def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


def greet(name):
    """Generate a greeting message"""
    return f"Hello, {name}!"


def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


























# ============================================================================
# HOW TO RUN
# ============================================================================
# Run in terminal:
#   pytest example1_basic_tests.py -v
#
# The -v flag shows verbose output (more details)
