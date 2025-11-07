# Question 10: NumPy - Extract all numbers from a given array which are divisible by 5

import numpy as np

def extract_divisible_by_5(arr):
    """Extract all numbers from array that are divisible by 5"""
    return arr[arr % 5 == 0]

# Test the function
if __name__ == "__main__":
    # Test case 1: 1D array
    arr1 = np.array([5, 10, 15, 20, 23, 25, 30, 33, 35, 40])
    print(f"Original array: {arr1}")
    print(f"Numbers divisible by 5: {extract_divisible_by_5(arr1)}")
    
    # Test case 2: Array with mixed numbers
    arr2 = np.array([1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 22, 25])
    print(f"\nOriginal array: {arr2}")
    print(f"Numbers divisible by 5: {extract_divisible_by_5(arr2)}")
    
    # Test case 3: Random array
    arr3 = np.arange(1, 51)
    print(f"\nOriginal array: {arr3}")
    print(f"Numbers divisible by 5: {extract_divisible_by_5(arr3)}")
