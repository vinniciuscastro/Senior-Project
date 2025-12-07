# file: testing/unit_test/test_string_excellent.py
"""
EXCELLENT mutation coverage for string_utils module.
Tests is_palindrome with comprehensive cases.
Should achieve 95%+ mutation score.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import string_utils


def test_is_palindrome_true_cases():
    """Test all cases where string IS a palindrome"""
    # Single character
    assert string_utils.is_palindrome("a") == True
    assert string_utils.is_palindrome("A") == True

    # Simple palindromes
    assert string_utils.is_palindrome("mom") == True
    assert string_utils.is_palindrome("dad") == True
    assert string_utils.is_palindrome("noon") == True
    assert string_utils.is_palindrome("racecar") == True
    assert string_utils.is_palindrome("level") == True

    # Mixed case palindromes
    assert string_utils.is_palindrome("Mom") == True
    assert string_utils.is_palindrome("Racecar") == True
    assert string_utils.is_palindrome("NOON") == True

    # Palindromes with spaces
    assert string_utils.is_palindrome("taco cat") == True
    assert string_utils.is_palindrome("race car") == True
    assert string_utils.is_palindrome("a man a plan a canal panama") == True

    # Even length palindromes
    assert string_utils.is_palindrome("abba") == True
    assert string_utils.is_palindrome("aa") == True


def test_is_palindrome_false_cases():
    """Test all cases where string is NOT a palindrome"""
    # Not palindromes
    assert string_utils.is_palindrome("hello") == False
    assert string_utils.is_palindrome("world") == False
    assert string_utils.is_palindrome("python") == False
    assert string_utils.is_palindrome("test") == False

    # Almost palindromes (off by one character)
    assert string_utils.is_palindrome("raceca") == False
    assert string_utils.is_palindrome("noob") == False
    assert string_utils.is_palindrome("mommy") == False

    # With spaces but not palindromes
    assert string_utils.is_palindrome("hello world") == False
    assert string_utils.is_palindrome("not a palindrome") == False
