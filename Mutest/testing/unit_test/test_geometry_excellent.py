# file: testing/unit_test/test_geometry_excellent.py
"""
EXCELLENT mutation coverage for geometry module.
Tests all functions with comprehensive boundary and edge cases.
Should achieve 95%+ mutation score.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import geometry


def test_calculate_circle_area_comprehensive():
    """Comprehensive tests for calculate_circle_area - tests all boundaries"""
    # Test normal cases
    assert geometry.calculate_circle_area(1) == 3.14159
    assert geometry.calculate_circle_area(2) == 12.56636
    assert geometry.calculate_circle_area(5) == 78.53975

    # Test boundary values
    assert geometry.calculate_circle_area(0) == 0.0  # Zero radius

    # Test edge cases
    assert geometry.calculate_circle_area(10) == 314.159

    # Test invalid input
    with pytest.raises(ValueError):
        geometry.calculate_circle_area(-1)  # Negative radius

    with pytest.raises(ValueError):
        geometry.calculate_circle_area(-5)


def test_calculate_rectangle_perimeter_comprehensive():
    """Comprehensive tests for calculate_rectangle_perimeter"""
    # Test normal cases
    assert geometry.calculate_rectangle_perimeter(5, 3) == 16
    assert geometry.calculate_rectangle_perimeter(10, 10) == 40
    assert geometry.calculate_rectangle_perimeter(7, 4) == 22

    # Test boundary values
    assert geometry.calculate_rectangle_perimeter(1, 1) == 4

    # Test different dimensions
    assert geometry.calculate_rectangle_perimeter(100, 50) == 300

    # Test invalid inputs - both boundaries
    with pytest.raises(ValueError):
        geometry.calculate_rectangle_perimeter(0, 5)  # Zero length

    with pytest.raises(ValueError):
        geometry.calculate_rectangle_perimeter(5, 0)  # Zero width

    with pytest.raises(ValueError):
        geometry.calculate_rectangle_perimeter(-1, 5)  # Negative length

    with pytest.raises(ValueError):
        geometry.calculate_rectangle_perimeter(5, -1)  # Negative width


def test_is_valid_triangle_comprehensive():
    """Comprehensive tests for is_valid_triangle - tests both true and false cases"""
    # Valid triangles
    assert geometry.is_valid_triangle(3, 4, 5) == True  # Classic right triangle
    assert geometry.is_valid_triangle(5, 5, 5) == True  # Equilateral
    assert geometry.is_valid_triangle(5, 5, 8) == True  # Isosceles
    assert geometry.is_valid_triangle(10, 10, 15) == True

    # Invalid triangles - violate triangle inequality
    assert geometry.is_valid_triangle(1, 2, 5) == False  # sum of two sides < third
    assert geometry.is_valid_triangle(1, 1, 2) == False  # sum equals third (boundary)
    assert geometry.is_valid_triangle(10, 1, 1) == False

    # Invalid inputs - negative or zero sides
    assert geometry.is_valid_triangle(-1, 5, 5) == False
    assert geometry.is_valid_triangle(5, -1, 5) == False
    assert geometry.is_valid_triangle(5, 5, -1) == False
    assert geometry.is_valid_triangle(0, 5, 5) == False
    assert geometry.is_valid_triangle(5, 0, 5) == False
    assert geometry.is_valid_triangle(5, 5, 0) == False


def test_calculate_triangle_area_comprehensive():
    """Comprehensive tests for calculate_triangle_area"""
    # Test normal cases
    assert geometry.calculate_triangle_area(10, 5) == 25.0
    assert geometry.calculate_triangle_area(6, 4) == 12.0
    assert geometry.calculate_triangle_area(8, 3) == 12.0

    # Test boundary values
    assert geometry.calculate_triangle_area(1, 1) == 0.5

    # Test different values
    assert geometry.calculate_triangle_area(20, 10) == 100.0

    # Test invalid inputs
    with pytest.raises(ValueError):
        geometry.calculate_triangle_area(0, 5)  # Zero base

    with pytest.raises(ValueError):
        geometry.calculate_triangle_area(5, 0)  # Zero height

    with pytest.raises(ValueError):
        geometry.calculate_triangle_area(-1, 5)  # Negative base

    with pytest.raises(ValueError):
        geometry.calculate_triangle_area(5, -1)  # Negative height
