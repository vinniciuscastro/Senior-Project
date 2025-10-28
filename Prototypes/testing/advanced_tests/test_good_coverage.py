# file: testing/advanced_tests/test_good_coverage.py
"""
Test file with EXCELLENT coverage - comprehensive tests.
This will result in most mutants being KILLED.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import temperature


def test_celsius_to_fahrenheit():
    """Comprehensive test for celsius to fahrenheit conversion"""
    # Test multiple values
    assert temperature.celsius_to_fahrenheit(0) == 32
    assert temperature.celsius_to_fahrenheit(100) == 212
    assert temperature.celsius_to_fahrenheit(-40) == -40
    assert abs(temperature.celsius_to_fahrenheit(37) - 98.6) < 0.1

    # This will catch mutants that change * to /, + to -, etc.


def test_fahrenheit_to_celsius():
    """Comprehensive test for fahrenheit to celsius conversion"""
    # Test multiple values
    assert temperature.fahrenheit_to_celsius(32) == 0
    assert temperature.fahrenheit_to_celsius(212) == 100
    assert temperature.fahrenheit_to_celsius(-40) == -40
    assert abs(temperature.fahrenheit_to_celsius(98.6) - 37) < 0.1

    # This will catch mutants that change -, *, / operations


def test_is_freezing():
    """Test freezing temperature check - tests both sides of boundary"""
    # Test boundary conditions
    assert temperature.is_freezing(0) == True    # Exactly at freezing
    assert temperature.is_freezing(-1) == True   # Below freezing
    assert temperature.is_freezing(-10) == True  # Well below freezing
    assert temperature.is_freezing(1) == False   # Just above freezing
    assert temperature.is_freezing(10) == False  # Well above freezing

    # This will catch mutants that change <= to <, >, >=, etc.


def test_is_boiling():
    """Test boiling temperature check - tests both sides of boundary"""
    # Test boundary conditions
    assert temperature.is_boiling(100) == True   # Exactly at boiling
    assert temperature.is_boiling(101) == True   # Above boiling
    assert temperature.is_boiling(150) == True   # Well above boiling
    assert temperature.is_boiling(99) == False   # Just below boiling
    assert temperature.is_boiling(50) == False   # Well below boiling

    # This will catch mutants that change >= to >, <, <=, etc.


def test_temperature_category():
    """Test temperature categorization - comprehensive coverage"""
    # Test all categories and their boundaries
    assert temperature.temperature_category(-5) == "freezing"
    assert temperature.temperature_category(0) == "cold"       # Boundary
    assert temperature.temperature_category(5) == "cold"
    assert temperature.temperature_category(10) == "cool"      # Boundary
    assert temperature.temperature_category(15) == "cool"
    assert temperature.temperature_category(20) == "warm"      # Boundary
    assert temperature.temperature_category(25) == "warm"
    assert temperature.temperature_category(30) == "hot"       # Boundary
    assert temperature.temperature_category(35) == "hot"

    # This comprehensive testing will catch most comparison operator mutations
