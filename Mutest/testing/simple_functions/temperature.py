# file: testing/simple_functions/temperature.py
"""
Temperature conversion and utility functions.
Provides functions for converting between Celsius and Fahrenheit,
and checking temperature conditions.
"""


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit

    Formula: F = C * 9/5 + 32
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit

    Returns:
        Temperature in Celsius

    Formula: C = (F - 32) * 5/9
    """
    return (fahrenheit - 32) * 5 / 9


def is_freezing(celsius):
    """
    Check if temperature is at or below freezing point (0°C).

    Args:
        celsius: Temperature in Celsius

    Returns:
        True if temperature is freezing (≤ 0°C), False otherwise
    """
    return celsius <= 0


def is_boiling(celsius):
    """
    Check if temperature is at or above boiling point (100°C).

    Args:
        celsius: Temperature in Celsius

    Returns:
        True if temperature is boiling (≥ 100°C), False otherwise
    """
    return celsius >= 100


def temperature_category(celsius):
    """
    Categorize temperature into descriptive categories.

    Args:
        celsius: Temperature in Celsius

    Returns:
        String category: "freezing", "cold", "cool", "warm", or "hot"

    Categories:
        - Below 0°C: freezing
        - 0-9°C: cold
        - 10-19°C: cool
        - 20-29°C: warm
        - 30°C and above: hot
    """
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
