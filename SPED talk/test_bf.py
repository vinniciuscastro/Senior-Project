"""
EXAMPLE 1: Basic Unit Tests with Pytest
========================================
This example shows the fundamentals of writing unit tests.
Each function does ONE thing, and each test verifies ONE behavior.
"""
from basic_functions import add, is_even, greet, calculate_discount



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
