# File: even_sum.py
import numpy as np

def sum_even_numbers(numbers):
    """
    returns sum of all even numbers in a list/array
    Inputs:
    Outputs:
    """
    sum = np.sum(num for num in numbers if num % 2 ==0)
    return sum
