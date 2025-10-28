"""
Very simple loop function designed to demonstrate timeout mutations.
"""

def count_to_five():
    """Count from 0 to 5 - very simple loop"""
    i = 0
    result = []
    while i < 5:  # If < mutated to >, <=, or >= this could loop forever
        result.append(i)
        i = i + 1  # If + mutated to -, this loops forever
    return result


def simple_sum(n):
    """Sum numbers from 1 to n"""
    total = 0
    i = 1
    while i < n:  # If < mutated, may not terminate correctly
        total = total + i  # If + mutated to -, wrong but won't timeout
        i = i + 1  # If + mutated to -, infinite loop
    return total
