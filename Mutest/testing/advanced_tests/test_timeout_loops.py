# file: testing/advanced_tests/test_timeout_loops.py
"""
Test file that will cause TIMEOUT mutants with loop-based functions.
When loop conditions or increment operations are mutated, infinite loops occur.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import loop_functions


def test_count_up_to():
    """
    Test count_up_to function.

    Mutations that cause TIMEOUT:
    - count < n  →  count <= n  (never terminates when count == n)
    - count < n  →  count > n   (infinite loop)
    - count + 1  →  count - 1   (infinite loop going backwards)
    """
    result = loop_functions.count_up_to(5)
    assert result == [0, 1, 2, 3, 4]
    assert len(result) == 5

    result = loop_functions.count_up_to(0)
    assert result == []

    result = loop_functions.count_up_to(1)
    assert result == [0]


def test_sum_while_positive():
    """
    Test sum_while_positive function.

    Mutations that cause TIMEOUT:
    - i < len(numbers)  →  i <= len(numbers)  (tries to access beyond array)
    - i + 1  →  i - 1   (infinite loop going backwards)
    - total + numbers[i]  →  total - numbers[i]  (wrong result but not timeout)
    """
    assert loop_functions.sum_while_positive([1, 2, 3, -1, 4]) == 6
    assert loop_functions.sum_while_positive([5, 10, 15]) == 30
    assert loop_functions.sum_while_positive([0, 1, 2]) == 0  # Stops at 0
    assert loop_functions.sum_while_positive([-1, 2, 3]) == 0  # First is negative


def test_find_first_negative():
    """
    Test find_first_negative function.

    Mutations that cause TIMEOUT:
    - i < len(numbers)  →  i <= len(numbers)  (access out of bounds)
    - i + 1  →  i - 1   (infinite loop)
    """
    assert loop_functions.find_first_negative([1, 2, -3, 4]) == 2
    assert loop_functions.find_first_negative([-1, 2, 3]) == 0
    assert loop_functions.find_first_negative([1, 2, 3]) == -1
    assert loop_functions.find_first_negative([5, 4, 3, 2, 1, -1]) == 5


def test_countdown():
    """
    Test countdown function.

    Mutations that cause TIMEOUT:
    - n > 0  →  n >= 0  (extra iteration, might not terminate)
    - n > 0  →  n < 0   (never enters loop when should)
    - n - 1  →  n + 1   (infinite loop, n keeps increasing)
    """
    result = loop_functions.countdown(5)
    assert result == [5, 4, 3, 2, 1]
    assert len(result) == 5

    result = loop_functions.countdown(1)
    assert result == [1]

    result = loop_functions.countdown(0)
    assert result == []

    result = loop_functions.countdown(3)
    assert result == [3, 2, 1]
