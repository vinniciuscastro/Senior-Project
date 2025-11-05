# Pytest & Unit Testing - SPED Talk Examples

This folder contains 4 complete code examples for teaching pytest and unit testing concepts.

## Quick Start

```bash
# Install pytest if you haven't already
pip install pytest

# Run all examples
pytest -v

# Run a specific example
pytest example1_basic_tests.py -v
```

---

## 📚 Example 1: Basic Unit Tests
**File:** `example1_basic_tests.py`

**What it teaches:**
- How to write simple unit tests
- The `assert` statement
- Naming conventions (functions start with `test_`)
- Testing different scenarios

**Key functions tested:**
- `add()` - Basic arithmetic
- `is_even()` - Boolean returns
- `greet()` - String manipulation
- `calculate_discount()` - Business logic

**Talking points:**
- Each test should test ONE thing
- Tests should be independent
- Good test names describe what they're testing

---

## 🔧 Example 2: Test Fixtures
**File:** `example2_fixtures.py`

**What it teaches:**
- What fixtures are and why they're useful
- The `@pytest.fixture` decorator
- How fixtures eliminate code duplication
- Test isolation (each test gets fresh fixture)

**Key concepts:**
- `empty_cart` fixture - provides fresh shopping cart
- `cart_with_items` fixture - provides pre-loaded cart
- Tests automatically get fixtures as parameters

**Talking points:**
- Fixtures = reusable setup code
- Like "before each" in other testing frameworks
- Keeps tests DRY (Don't Repeat Yourself)

---

## 🔄 Example 3: Parametrized Tests
**File:** `example3_parametrized.py`

**What it teaches:**
- The `@pytest.mark.parametrize` decorator
- Testing multiple inputs without code duplication
- How to write one test that runs many times

**Key functions tested:**
- `is_valid_password()` - Multiple password scenarios
- `calculate_grade()` - All grade boundaries
- `fahrenheit_to_celsius()` - Temperature edge cases

**Talking points:**
- Test 10 cases with 1 test function instead of 10
- Easy to add new test cases (just add to list)
- Makes thorough testing practical

---

## ⚠️ Example 4: Testing Exceptions
**File:** `example4_exceptions.py`

**What it teaches:**
- How to test that code raises errors correctly
- Using `pytest.raises()` context manager
- Testing error messages with `match` parameter
- Capturing exception details with `exc_info`

**Key concepts:**
- `BankAccount` class with validation
- Testing both success and failure cases
- Ensuring helpful error messages

**Talking points:**
- Good code handles errors gracefully
- Test the "unhappy path" not just the "happy path"
- Users should see helpful error messages

---

## 🎤 Presentation Tips

### Order to Present:
1. **Example 1** - Start here, covers fundamentals
2. **Example 2** - Build on basics with fixtures
3. **Example 3** - Show how to be more efficient
4. **Example 4** - Complete picture with error handling

### Live Demo Ideas:

**1. Show a test passing:**
```bash
pytest example1_basic_tests.py::test_add -v
```

**2. Show a test failing (break something on purpose):**
- Change `assert add(2, 3) == 5` to `assert add(2, 3) == 6`
- Run the test and show the detailed error message

**3. Show verbose vs normal output:**
```bash
# Normal output
pytest example1_basic_tests.py

# Verbose output (shows each test)
pytest example1_basic_tests.py -v

# Even more verbose (shows print statements)
pytest example1_basic_tests.py -vv
```

**4. Run parametrized tests to show one function = many tests:**
```bash
pytest example3_parametrized.py::test_password_validation -v
```

### Discussion Questions:
1. Why is testing important?
2. When should you write tests? (Before code? After? During?)
3. What makes a good test?
4. How much testing is enough?

---

## 📊 Testing Best Practices

### The 3 A's of Testing:
1. **Arrange** - Set up test data
2. **Act** - Call the function being tested
3. **Assert** - Check the result

### Good Test Characteristics:
- **Fast** - Tests should run quickly
- **Independent** - Tests shouldn't depend on each other
- **Repeatable** - Same result every time
- **Self-checking** - Pass or fail automatically
- **Timely** - Written close to the code

### Test Naming Convention:
```python
def test_<function_name>_<scenario>_<expected_result>():
    # Example: test_divide_by_zero_raises_error
    pass
```

---

## 🚀 Advanced Topics (If Time Permits)

### Mocking and Patching:
```python
# For testing code that calls external services, databases, APIs
from unittest.mock import Mock, patch
```

### Test Coverage:
```bash
# Install coverage tool
pip install pytest-cov

# Run tests with coverage report
pytest --cov=. --cov-report=html
```

### Continuous Integration:
- Run tests automatically on every commit
- GitHub Actions, GitLab CI, Jenkins, etc.

---

## 🎯 Key Takeaways

1. **Testing saves time** - Catch bugs early, before users do
2. **Tests are documentation** - Show how code is supposed to work
3. **Pytest makes testing easy** - Minimal boilerplate, powerful features
4. **Test early, test often** - Make it part of your workflow

---

## 📝 Quick Command Reference

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific file
pytest example1_basic_tests.py

# Run a specific test
pytest example1_basic_tests.py::test_add

# Stop after first failure
pytest -x

# Show local variables in failures
pytest -l

# Run tests matching a pattern
pytest -k "password"
```

---

## 🔗 Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Real Python - Pytest Tutorial](https://realpython.com/pytest-python-testing/)
- [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)

---

Good luck with your talk! 🎉
