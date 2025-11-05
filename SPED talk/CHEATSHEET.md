# Pytest Cheat Sheet - Quick Reference

## Basic Test Structure

```python
def test_something():
    # Arrange - Set up test data
    x = 5

    # Act - Call the function
    result = my_function(x)

    # Assert - Check the result
    assert result == expected_value
```

## Common Assertions

```python
# Equality
assert a == b
assert a != b

# Comparison
assert a > b
assert a >= b
assert a < b
assert a <= b

# Boolean
assert condition is True
assert condition is False

# Membership
assert item in collection
assert item not in collection

# Type checking
assert isinstance(obj, MyClass)

# Approximate equality (for floats)
assert abs(a - b) < 0.001
```

## Fixtures

```python
@pytest.fixture
def my_fixture():
    # Setup code
    data = setup_data()
    return data
    # Teardown happens automatically

# Use fixture in test
def test_with_fixture(my_fixture):
    assert my_fixture.some_property == expected
```

## Parametrized Tests

```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert double(input) == expected
```

## Testing Exceptions

```python
# Simple exception test
def test_error():
    with pytest.raises(ValueError):
        some_function()

# Check error message
def test_error_message():
    with pytest.raises(ValueError, match="specific message"):
        some_function()

# Capture exception details
def test_error_details():
    with pytest.raises(ValueError) as exc_info:
        some_function()
    assert "important text" in str(exc_info.value)
```

## Running Tests

```bash
pytest                    # Run all tests
pytest -v                 # Verbose output
pytest -vv                # Extra verbose
pytest file.py            # Run specific file
pytest file.py::test_foo  # Run specific test
pytest -k "name"          # Run tests matching name
pytest -x                 # Stop at first failure
pytest --tb=short         # Shorter traceback
pytest -l                 # Show local variables in errors
```

## Test Organization

```
project/
├── src/
│   └── mymodule.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # Shared fixtures
│   ├── test_feature1.py
│   └── test_feature2.py
└── pytest.ini           # Configuration
```

## Common Patterns

### Setup and Teardown

```python
def setup_function():
    # Runs before each test function
    pass

def teardown_function():
    # Runs after each test function
    pass
```

### Skipping Tests

```python
@pytest.mark.skip(reason="Not ready yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_new_feature():
    pass
```

### Expected Failures

```python
@pytest.mark.xfail(reason="Known bug #123")
def test_known_issue():
    pass
```

## Pro Tips

1. **One assertion per test** (when possible)
2. **Use descriptive test names** - `test_user_cannot_delete_other_users_posts`
3. **Test edge cases** - empty, zero, negative, very large
4. **Keep tests simple** - If test is complex, code might be too complex
5. **Tests should be fast** - Slow tests won't get run

## Common Mistakes to Avoid

```python
# ❌ Don't do this - tests depend on each other
def test_a():
    global value
    value = 5

def test_b():
    assert value == 5  # Breaks if test_a doesn't run first!

# ✅ Do this - tests are independent
def test_a():
    value = 5
    assert value == 5

def test_b():
    value = 5
    assert value == 5
```

```python
# ❌ Don't do this - testing multiple things
def test_user():
    assert user.name == "Alice"
    assert user.age == 30
    assert user.email == "alice@example.com"

# ✅ Do this - separate tests
def test_user_name():
    assert user.name == "Alice"

def test_user_age():
    assert user.age == 30

def test_user_email():
    assert user.email == "alice@example.com"
```

## When to Write Tests

- **Before coding** (Test-Driven Development)
- **During coding** (Test as you go)
- **After coding** (Better late than never!)

The best time? **Whichever gets you to actually write them!**
