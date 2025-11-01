"""
Functions with loops that can cause timeouts when mutated.
When comparison operators are mutated, loops can become infinite.
"""


def count_up_to(n):
    """Count from 0 to n"""
    count = 0
    result = []
    while count < n:
        result.append(count)
        count = count + 1
    return result


def sum_while_positive(numbers):
    """Sum numbers while they are positive"""
    total = 0
    i = 0
    while i < len(numbers):
        if numbers[i] <= 0:
            break
        total = total + numbers[i]
        i = i + 1
    return total


def find_first_negative(numbers):
    """Find index of first negative number"""
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            return i
        i = i + 1
    return -1


def countdown(n):
    """Countdown from n to 0"""
    result = []
    while n > 0:
        result.append(n)
        n = n - 1
    return result
