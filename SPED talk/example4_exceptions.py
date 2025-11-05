"""
EXAMPLE 4: Testing Exceptions and Error Handling
=================================================
Good code doesn't just handle valid input - it also handles errors gracefully.
We need to test that our functions raise the RIGHT errors at the RIGHT times.

WHY TEST EXCEPTIONS?
- Ensure your code fails gracefully with bad input
- Verify error messages are helpful
- Catch bugs before users do!
"""

import pytest

# ============================================================================
# CODE TO TEST
# ============================================================================

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def get_user_age(age):
    """Validate and return user age"""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age


class BankAccount:
    """A simple bank account"""

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance

    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        return self.balance


# ============================================================================
# TESTING EXCEPTIONS - Method 1: pytest.raises()
# ============================================================================

def test_divide_by_zero():
    """Test that dividing by zero raises ValueError"""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_with_message():
    """Test the exact error message"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_negative_age():
    """Test that negative age raises error"""
    with pytest.raises(ValueError):
        get_user_age(-5)


def test_unrealistic_age():
    """Test that unrealistic age raises error"""
    with pytest.raises(ValueError, match="unrealistic"):
        get_user_age(200)


# ============================================================================
# TESTING EXCEPTIONS - Method 2: Capturing exception details
# ============================================================================

def test_negative_age_detailed():
    """Capture exception and check its details"""
    with pytest.raises(ValueError) as exc_info:
        get_user_age(-10)

    # Check the exact error message
    assert str(exc_info.value) == "Age cannot be negative"


def test_bank_account_insufficient_funds():
    """Test withdrawing more than balance"""
    account = BankAccount(balance=100)

    with pytest.raises(ValueError) as exc_info:
        account.withdraw(150)

    assert "Insufficient funds" in str(exc_info.value)


def test_negative_initial_balance():
    """Test creating account with negative balance"""
    with pytest.raises(ValueError):
        BankAccount(balance=-50)


def test_negative_withdrawal():
    """Test withdrawing negative amount"""
    account = BankAccount(balance=100)

    with pytest.raises(ValueError, match="must be positive"):
        account.withdraw(-10)


def test_negative_deposit():
    """Test depositing negative amount"""
    account = BankAccount(balance=100)

    with pytest.raises(ValueError, match="must be positive"):
        account.deposit(-20)


# ============================================================================
# TESTING BOTH SUCCESS AND FAILURE
# ============================================================================

def test_divide_success():
    """Test that division works with valid input"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_valid_age():
    """Test that valid ages work correctly"""
    assert get_user_age(25) == 25
    assert get_user_age(0) == 0
    assert get_user_age(150) == 150  # Edge case: exactly 150 is valid


def test_bank_account_success():
    """Test that bank account works correctly with valid operations"""
    account = BankAccount(balance=100)

    # Test successful deposit
    new_balance = account.deposit(50)
    assert new_balance == 150

    # Test successful withdrawal
    new_balance = account.withdraw(30)
    assert new_balance == 120


# ============================================================================
# PARAMETRIZED EXCEPTION TESTS
# ============================================================================

@pytest.mark.parametrize("age", [-1, -100, -5])
def test_multiple_negative_ages(age):
    """Test that various negative ages all raise errors"""
    with pytest.raises(ValueError):
        get_user_age(age)


@pytest.mark.parametrize("amount", [-10, -50, 0])
def test_invalid_withdrawal_amounts(amount):
    """Test that invalid withdrawal amounts raise errors"""
    account = BankAccount(balance=100)
    with pytest.raises(ValueError):
        account.withdraw(amount)


# ============================================================================
# HOW TO RUN
# ============================================================================
# Run in terminal:
#   pytest example4_exceptions.py -v
#
# Key takeaway: Testing errors is just as important as testing success!
