# file: testing/unit_test/test_calculator_excellent.py
"""
EXCELLENT mutation coverage for calculator module.
Tests all functions with comprehensive boundary and edge cases.
Should achieve 95%+ mutation score.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import calculator


def test_calculate_discount_comprehensive():
    """Comprehensive tests for calculate_discount - tests all boundaries"""
    # Test normal cases
    assert calculator.calculate_discount(100, 10) == 90.0
    assert calculator.calculate_discount(100, 50) == 50.0
    assert calculator.calculate_discount(200, 25) == 150.0

    # Test boundary values
    assert calculator.calculate_discount(100, 0) == 100.0  # No discount
    assert calculator.calculate_discount(100, 100) == 0.0  # Full discount

    # Test edge cases
    assert calculator.calculate_discount(0, 10) == 0.0  # Zero price
    assert calculator.calculate_discount(50, 20) == 40.0

    # Test invalid inputs - both boundaries
    with pytest.raises(ValueError):
        calculator.calculate_discount(100, -1)  # Below 0

    with pytest.raises(ValueError):
        calculator.calculate_discount(100, 101)  # Above 100


def test_calculate_tax_comprehensive():
    """Comprehensive tests for calculate_tax - tests all boundaries"""
    # Test normal cases
    assert calculator.calculate_tax(100, 0.1) == 110.0
    assert calculator.calculate_tax(100, 0.2) == 120.0
    assert calculator.calculate_tax(50, 0.05) == 52.5

    # Test boundary values
    assert calculator.calculate_tax(100, 0) == 100.0  # No tax
    assert calculator.calculate_tax(0, 0.1) == 0.0    # Zero amount

    # Test different tax rates
    assert calculator.calculate_tax(200, 0.15) == 230.0
    assert calculator.calculate_tax(75, 0.08) == 81.0

    # Test invalid input
    with pytest.raises(ValueError):
        calculator.calculate_tax(100, -0.1)  # Negative tax rate


def test_is_even_comprehensive():
    """Comprehensive tests for is_even - tests both true and false cases"""
    # Test even numbers
    assert calculator.is_even(0) == True   # Zero is even
    assert calculator.is_even(2) == True
    assert calculator.is_even(4) == True
    assert calculator.is_even(100) == True
    assert calculator.is_even(-2) == True  # Negative even
    assert calculator.is_even(-100) == True

    # Test odd numbers
    assert calculator.is_even(1) == False
    assert calculator.is_even(3) == False
    assert calculator.is_even(99) == False
    assert calculator.is_even(-1) == False  # Negative odd
    assert calculator.is_even(-99) == False
