# file: testing/unit_test/test_shopping_fair.py
"""
FAIR mutation coverage for shopping module.
Tests some functions but misses several boundary cases.
Should achieve 60-75% mutation score.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import shopping


def test_calculate_total():
    """Basic test for calculate_total - missing edge cases"""
    # Test normal case
    assert shopping.calculate_total([10, 20, 30]) == 60
    assert shopping.calculate_total([5, 5]) == 10

    # Missing: empty list test, single item, negative numbers


def test_apply_bulk_discount():
    """Test bulk discount - missing some boundaries"""
    # Test 10+ items (20% off)
    assert shopping.apply_bulk_discount(100, 10) == 80.0

    # Test 5-9 items (10% off)
    assert shopping.apply_bulk_discount(100, 5) == 90.0

    # Missing: test for exactly 9 items, test for 4 items, test for 0 items
    # Missing: boundary tests for exactly at discount thresholds


def test_calculate_shipping():
    """Test shipping calculation - incomplete"""
    # Test free shipping
    assert shopping.calculate_shipping(100) == 0.0

    # Test mid-range shipping
    assert shopping.calculate_shipping(75) == 5.0

    # Missing: test for exactly $50, test for $49, test for exactly $99
    # Missing: test for very low amounts


def test_is_eligible_for_coupon():
    """Test coupon eligibility - missing branches"""
    # Test premium customer
    assert shopping.is_eligible_for_coupon(30, "premium") == True

    # Test regular customer
    assert shopping.is_eligible_for_coupon(60, "regular") == True

    # Missing: test for exactly at thresholds ($25 for premium, $50 for regular)
    # Missing: test for below thresholds
    # Missing: test for unknown customer type
    # Missing: test for empty string customer type
