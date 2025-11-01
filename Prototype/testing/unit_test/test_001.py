# file: tests/test_math_utils.py
import sys, pathlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import math_utils, grade_utils, string_utils


def test_add():
    assert math_utils.add(2, 3) == 5

def test_subtract():
    assert math_utils.subtract(5, 3) == 2

def test_multiply():
    assert math_utils.multiply(4, 2) == 8

def test_divide():
    assert math_utils.divide(10, 2) == 5
    with pytest.raises(ValueError):
        math_utils.divide(10, 0)

def test_get_grade():
    assert grade_utils.get_grade(95) == "A"
    assert grade_utils.get_grade(75) == "C"
    assert grade_utils.get_grade(50) == "F"

def test_is_palindrome():
    assert string_utils.is_palindrome("racecar")
    assert string_utils.is_palindrome("Never odd or even")
    assert not string_utils.is_palindrome("hello")
