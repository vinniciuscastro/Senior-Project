# file: testing/unit_test/test_validators_poor.py
"""
POOR mutation coverage for validators module.
Only tests happy paths, missing most edge cases and boundaries.
Should achieve low mutation score (< 50%).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from simple_functions import validators


def test_is_valid_email():
    """Minimal test for email validation - only happy path"""
    # Only test valid email
    assert validators.is_valid_email("test@example.com") == True

    # Missing: invalid emails, edge cases, boundary conditions
    # Missing: no @, multiple @, empty string, no domain, no local part
    # Missing: no dot in domain, etc.


def test_is_strong_password():
    """Minimal test for password strength - only one case"""
    # Only test one strong password
    assert validators.is_strong_password("Password123") == True

    # Missing: weak passwords, boundary cases
    # Missing: too short, no uppercase, no lowercase, no digits
    # Missing: exactly 8 characters, exactly 7 characters


def test_is_valid_age():
    """Minimal test for age validation - only middle values"""
    # Only test a normal age
    assert validators.is_valid_age(25) == True

    # Missing: boundary tests (0, 150, -1, 151)
    # Missing: very young, very old
    # Missing: negative ages


# Missing: test_is_weekend function entirely - this will allow all mutants to survive!
