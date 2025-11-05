"""
EXAMPLE 3: Parametrized Tests
==============================
Parametrized tests let you run the same test with different inputs.
Instead of writing 10 similar tests, write ONE test with 10 inputs!

WHY USE PARAMETRIZED TESTS?
- Test multiple cases without duplicating code
- Easy to add new test cases
- Cleaner, more maintainable tests
"""

import pytest
from parametrized import is_valid_password, calculate_grade, fahrenheit_to_celsius



@pytest.mark.parametrize("password,expected", [
    ("Abc12345", True),      # Valid: has uppercase, digit, and 8+ chars
    ("HelloWorld1", True),   # Valid
    ("Test123", False),      # Invalid: only 7 characters
    ("abcdefgh", False),     # Invalid: no digit or uppercase
    ("ABCDEFGH", False),     # Invalid: no digit
    ("abcd1234", False),     # Invalid: no uppercase
    ("Short1", False),       # Invalid: too short
    ("ValidPass123", True),  # Valid
])
def test_password_validation(password, expected):
    """Test password validation with multiple cases"""
    assert is_valid_password(password) == expected


@pytest.mark.parametrize("score,expected_grade", [
    (95, 'A'),
    (90, 'A'),
    (85, 'B'),
    (80, 'B'),
    (75, 'C'),
    (70, 'C'),
    (65, 'D'),
    (60, 'D'),
    (55, 'F'),
    (0, 'F'),
    (100, 'A'),
])
def test_grade_calculation(score, expected_grade):
    """Test grade calculation for various scores"""
    assert calculate_grade(score) == expected_grade


@pytest.mark.parametrize("fahrenheit,celsius", [
    (32, 0),        # Freezing point
    (212, 100),     # Boiling point
    (98.6, 37),     # Body temperature
    (0, -17.78),    # Cold day
    (100, 37.78),   # Hot day
])
def test_temperature_conversion(fahrenheit, celsius):
    """Test temperature conversion"""
    result = fahrenheit_to_celsius(fahrenheit)
    assert abs(result - celsius) < 0.1  # Allow small floating point difference


# ============================================================================
# COMPARISON: Without Parametrization (DON'T DO THIS!)
# ============================================================================

def test_password_old_way():
    """This is how you'd test without parametrization - TOO MUCH CODE!"""
    assert is_valid_password("Abc12345") == True
    assert is_valid_password("HelloWorld1") == True
    assert is_valid_password("Test123") == False
    assert is_valid_password("abcdefgh") == False
    # ... and so on (gets repetitive and hard to read!)


# ============================================================================
# HOW TO RUN
# ============================================================================
# Run in terminal:
#   pytest example3_parametrized.py -v
#
# Notice: Each parameter combination runs as a separate test!
# You'll see test_password_validation[Abc12345-True], etc.
