# file: testing/advanced_tests/test_simple_loop.py
"""
Very simple test to demonstrate timeout mutations.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from simple_functions import simple_loop


def test_count_to_five():
    """
    Test count_to_five function.

    When i + 1 is mutated to i - 1, the loop goes backward infinitely.
    When i < 5 is mutated to i > 5, the loop never enters (not a timeout).
    """
    result = simple_loop.count_to_five()
    assert result == [0, 1, 2, 3, 4]
    assert len(result) == 5


def test_simple_sum():
    """
    Test simple_sum function.

    When the increment i + 1 is mutated to i - 1, infinite loop occurs.
    """
    assert simple_loop.simple_sum(5) == 10  # 1+2+3+4 = 10
    assert simple_loop.simple_sum(1) == 0
    assert simple_loop.simple_sum(10) == 45
