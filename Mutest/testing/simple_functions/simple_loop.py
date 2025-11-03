"""
Very simple loop function designed to demonstrate timeout mutations.
"""


def count_to_five():
    """Count from 0 to 5 - very simple loop"""
    i = 0
    result = []
    while i < 5:
        result.append(i)
        i = i - 1
    return result


def simple_sum(n):
    """Sum numbers from 1 to n"""
    total = 0
    i = 1
    while i < n:
        total = total + i
        i = i + 1
    return total
