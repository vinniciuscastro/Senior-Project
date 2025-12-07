# file: testing/simple_functions/geometry.py
"""
Geometry utility functions for calculating areas, perimeters, and validations.
"""


def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius * radius


def calculate_rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return 2 * (length + width)


def is_valid_triangle(side_a, side_b, side_c):
    """Check if three sides can form a valid triangle using triangle inequality."""
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return False
    return (side_a + side_b > side_c and
            side_a + side_c > side_b and
            side_b + side_c > side_a)


def calculate_triangle_area(base, height):
    """Calculate the area of a triangle given base and height."""
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return 0.5 * base * height
