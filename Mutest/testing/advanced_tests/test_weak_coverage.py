# file: testing/advanced_tests/test_weak_coverage.py
"""
Test file with WEAK coverage - intentionally incomplete tests.
This will result in SURVIVING MUTANTS because we don't test all edge cases.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import calculator


def test_calculate_discount_basic():
    """Only tests basic case - doesn't test boundary conditions"""
    # This only tests one scenario
    result = calculator.calculate_discount(100, 20)
    assert result == 80

    # We're NOT testing:
    # - discount_percent = 0 (mutant could change < to <= and survive)
    # - discount_percent = 100 (mutant could change > to >= and survive)
    # - The subtraction operation (mutant could change - to + and survive)
    # - The division operation (mutant could change / to * and survive)


def test_calculate_tax_basic():
    """Only tests basic case - doesn't verify the calculation"""
    # Only checks that it returns something positive
    result = calculator.calculate_tax(100, 0.08)
    assert result > 0

    # We're NOT testing:
    # - The exact calculation (mutant could change * to / and survive)
    # - The addition operation (mutant could change + to - and survive)
    # - Edge case with 0 tax rate


def test_is_even_partial():
    """Only tests even numbers - doesn't test odd numbers"""
    assert calculator.is_even(2) == True
    assert calculator.is_even(4) == True

    # We're NOT testing:
    # - Odd numbers (mutant could change == to != and survive)
    # - The modulo operation (mutant could survive)
