"""
Temperature conversion module with good test coverage.
This will demonstrate well-tested code with killed mutants.
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9


def is_freezing(celsius):
    """Check if temperature is at or below freezing (0°C)"""
    return celsius <= 0


def is_boiling(celsius):
    """Check if temperature is at or above boiling (100°C)"""
    return celsius >= 100


def temperature_category(celsius):
    """Categorize temperature"""
    if celsius < 0:
        return "freezing"
    elif celsius < 10:
        return "cold"
    elif celsius < 20:
        return "cool"
    elif celsius < 30:
        return "warm"
    else:
        return "hot"
