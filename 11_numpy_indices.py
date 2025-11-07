# Question 11: NumPy - Find the indices of elements equal to zero

import numpy as np

def find_zero_indices(arr):
    """Find indices of elements equal to zero in an array"""
    return np.where(arr == 0)[0]

# Test the function
if __name__ == "__main__":
    # Test case 1: 1D array with zeros
    arr1 = np.array([1, 0, 3, 0, 5, 0, 7])
    print(f"Array: {arr1}")
    print(f"Indices of zeros: {find_zero_indices(arr1)}")
    
    # Test case 2: Array with no zeros
    arr2 = np.array([1, 2, 3, 4, 5])
    print(f"\nArray: {arr2}")
    print(f"Indices of zeros: {find_zero_indices(arr2)}")
    
    # Test case 3: Array with multiple zeros
    arr3 = np.array([0, 0, 1, 2, 0, 3, 0, 0])
    print(f"\nArray: {arr3}")
    print(f"Indices of zeros: {find_zero_indices(arr3)}")
