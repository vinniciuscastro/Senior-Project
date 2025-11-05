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
# UNIT TESTS (Test functions start with 'test_')
# ============================================================================

def test_add():
    """Test that add function works correctly"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_is_even():
    """Test even number detection"""
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(3) == False
    assert is_even(7) == False


def test_greet():
    """Test greeting message generation"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_calculate_discount():
    """Test discount calculation"""
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(50, 20) == 40.0
    assert calculate_discount(200, 0) == 200.0


# ============================================================================
# HOW TO RUN
# ============================================================================
# Run in terminal:
#   pytest example1_basic_tests.py -v
#
# The -v flag shows verbose output (more details)
