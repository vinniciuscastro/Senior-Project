# file: testing/advanced_tests/test_timeout.py
"""
Test file that will cause TIMEOUT mutants.
When base case conditions are mutated, recursion becomes infinite.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import recursive_functions


def test_factorial():
    """Test factorial - mutations to base case will cause infinite recursion"""
    assert recursive_functions.factorial(0) == 1
    assert recursive_functions.factorial(1) == 1
    assert recursive_functions.factorial(5) == 120

    # When mutant changes == to != in base case (n == 0 or n == 1),
    # it will cause infinite recursion and TIMEOUT

    with pytest.raises(ValueError):
        recursive_functions.factorial(-1)


def test_fibonacci():
    """Test fibonacci - mutations to base case will cause infinite recursion"""
    assert recursive_functions.fibonacci(0) == 0
    assert recursive_functions.fibonacci(1) == 1
    assert recursive_functions.fibonacci(5) == 5
    assert recursive_functions.fibonacci(10) == 55

    # When mutant changes == to != in base cases,
    # it will cause infinite recursion and TIMEOUT

    with pytest.raises(ValueError):
        recursive_functions.fibonacci(-1)


def test_sum_to_n():
    """Test sum_to_n - mutations to base case will cause infinite recursion"""
    assert recursive_functions.sum_to_n(0) == 0
    assert recursive_functions.sum_to_n(1) == 1
    assert recursive_functions.sum_to_n(5) == 15  # 1+2+3+4+5
    assert recursive_functions.sum_to_n(10) == 55

    # When mutant changes <= to < in base case (n <= 0),
    # it will cause infinite recursion and TIMEOUT
