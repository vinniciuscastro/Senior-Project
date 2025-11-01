"""
Recursive functions that can cause timeouts.
This will demonstrate timeout mutants.
"""

def factorial(n):
    """Calculate factorial recursively"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate nth fibonacci number recursively"""
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_to_n(n):
    """Sum all numbers from 1 to n recursively"""
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)
