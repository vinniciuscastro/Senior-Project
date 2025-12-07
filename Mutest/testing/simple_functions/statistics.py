# file: testing/simple_functions/statistics.py
"""
Statistical utility functions for calculating mean, median, and range.
"""


def calculate_mean(numbers):
    """Calculate the arithmetic mean (average) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # Even number of elements - average of two middle values
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # Odd number of elements - middle value
        return sorted_numbers[n // 2]


def calculate_range(numbers):
    """Calculate the range (max - min) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate range of empty list")
    return max(numbers) - min(numbers)


def is_passing_grade(score):
    """Check if a score is a passing grade (>= 60)."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    return score >= 60
