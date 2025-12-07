# file: testing/simple_functions/validators.py
"""
Validation utility functions for checking various inputs.
"""


def is_valid_email(email):
    """Basic email validation."""
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True


def is_strong_password(password):
    """Check if password meets strength requirements."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit


def is_valid_age(age):
    """Check if age is valid (between 0 and 150)."""
    return 0 <= age <= 150


def is_weekend(day):
    """Check if day is weekend (Saturday or Sunday)."""
    return day in ["Saturday", "Sunday"]
