# file: testing/unit_test/test_statistics_excellent.py
"""
EXCELLENT mutation coverage for statistics module.
Tests all functions with comprehensive boundary and edge cases.
Should achieve 95%+ mutation score.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import statistics


def test_calculate_mean_comprehensive():
    """Comprehensive tests for calculate_mean - tests all boundaries"""
    # Test normal cases
    assert statistics.calculate_mean([1, 2, 3, 4, 5]) == 3.0
    assert statistics.calculate_mean([10, 20, 30]) == 20.0
    assert statistics.calculate_mean([5, 5, 5, 5]) == 5.0

    # Test single element
    assert statistics.calculate_mean([10]) == 10.0

    # Test negative numbers
    assert statistics.calculate_mean([-5, -10, -15]) == -10.0

    # Test mixed positive and negative
    assert statistics.calculate_mean([-10, 10]) == 0.0
    assert statistics.calculate_mean([1, 2, 3, -6]) == 0.0

    # Test decimals
    assert statistics.calculate_mean([1.5, 2.5, 3.5]) == 2.5

    # Test invalid input
    with pytest.raises(ValueError):
        statistics.calculate_mean([])  # Empty list


def test_calculate_median_comprehensive():
    """Comprehensive tests for calculate_median - tests odd and even cases"""
    # Test odd number of elements
    assert statistics.calculate_median([1, 2, 3]) == 2
    assert statistics.calculate_median([5, 1, 3, 2, 4]) == 3
    assert statistics.calculate_median([10]) == 10

    # Test even number of elements
    assert statistics.calculate_median([1, 2, 3, 4]) == 2.5
    assert statistics.calculate_median([10, 20]) == 15.0
    assert statistics.calculate_median([1, 2, 3, 4, 5, 6]) == 3.5

    # Test negative numbers
    assert statistics.calculate_median([-5, -10, -15]) == -10

    # Test mixed positive and negative
    assert statistics.calculate_median([-10, 0, 10]) == 0

    # Test unsorted input
    assert statistics.calculate_median([5, 2, 8, 1, 9]) == 5

    # Test invalid input
    with pytest.raises(ValueError):
        statistics.calculate_median([])  # Empty list


def test_calculate_range_comprehensive():
    """Comprehensive tests for calculate_range"""
    # Test normal cases
    assert statistics.calculate_range([1, 2, 3, 4, 5]) == 4
    assert statistics.calculate_range([10, 20, 30]) == 20
    assert statistics.calculate_range([100, 200]) == 100

    # Test single element
    assert statistics.calculate_range([10]) == 0

    # Test negative numbers
    assert statistics.calculate_range([-5, -10, -15]) == 10

    # Test mixed positive and negative
    assert statistics.calculate_range([-10, 10]) == 20
    assert statistics.calculate_range([-5, 0, 5]) == 10

    # Test same values
    assert statistics.calculate_range([5, 5, 5, 5]) == 0

    # Test invalid input
    with pytest.raises(ValueError):
        statistics.calculate_range([])  # Empty list


def test_is_passing_grade_comprehensive():
    """Comprehensive tests for is_passing_grade - tests boundary"""
    # Test passing grades
    assert statistics.is_passing_grade(60) == True  # Exactly at boundary
    assert statistics.is_passing_grade(61) == True
    assert statistics.is_passing_grade(75) == True
    assert statistics.is_passing_grade(90) == True
    assert statistics.is_passing_grade(100) == True

    # Test failing grades
    assert statistics.is_passing_grade(59) == False  # Just below boundary
    assert statistics.is_passing_grade(50) == False
    assert statistics.is_passing_grade(30) == False
    assert statistics.is_passing_grade(0) == False

    # Test invalid inputs
    with pytest.raises(ValueError):
        statistics.is_passing_grade(-1)  # Below 0

    with pytest.raises(ValueError):
        statistics.is_passing_grade(101)  # Above 100
