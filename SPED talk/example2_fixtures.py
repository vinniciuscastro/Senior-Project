"""
EXAMPLE 2: Test Fixtures
=========================
Fixtures are reusable setup code that runs before tests.
They help you avoid repeating the same setup in every test.

WHY USE FIXTURES?
- Avoid code duplication
- Set up test data once, use it many times
- Clean setup/teardown
"""

import pytest

# ============================================================================
# CODE TO TEST (A simple shopping cart)
# ============================================================================

class ShoppingCart:
    """A simple shopping cart"""

    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        """Add an item to the cart"""
        self.items.append({'item': item, 'price': price})

    def get_total(self):
        """Calculate total price of all items"""
        return sum(item['price'] for item in self.items)

    def get_item_count(self):
        """Get number of items in cart"""
        return len(self.items)

    def clear(self):
        """Remove all items from cart"""
        self.items = []


# ============================================================================
# FIXTURES (Reusable test setup)
# ============================================================================

@pytest.fixture
def empty_cart():
    """Provides a fresh empty shopping cart for each test"""
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    """Provides a cart pre-loaded with some items"""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)
    return cart


# ============================================================================
# TESTS USING FIXTURES
# ============================================================================

def test_empty_cart_has_zero_items(empty_cart):
    """Test that new cart starts empty"""
    assert empty_cart.get_item_count() == 0
    assert empty_cart.get_total() == 0


def test_add_item_to_cart(empty_cart):
    """Test adding items to cart"""
    empty_cart.add_item("Milk", 3.50)
    assert empty_cart.get_item_count() == 1
    assert empty_cart.get_total() == 3.50


def test_cart_total_calculation(cart_with_items):
    """Test total price calculation with pre-loaded cart"""
    # Cart already has: Apple (1.50) + Banana (0.75) + Orange (2.00) = 4.25
    assert cart_with_items.get_total() == 4.25


def test_add_to_existing_cart(cart_with_items):
    """Test adding to a cart that already has items"""
    cart_with_items.add_item("Grapes", 3.00)
    assert cart_with_items.get_item_count() == 4
    assert cart_with_items.get_total() == 7.25


def test_clear_cart(cart_with_items):
    """Test clearing all items from cart"""
    cart_with_items.clear()
    assert cart_with_items.get_item_count() == 0
    assert cart_with_items.get_total() == 0


# ============================================================================
# HOW TO RUN
# ============================================================================
# Run in terminal:
#   pytest example2_fixtures.py -v
#
# Notice: Each test gets its own fresh fixture instance!
# Tests don't interfere with each other.
