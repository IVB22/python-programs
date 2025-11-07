# Question 9b: NumPy - Element-wise comparison of two arrays

import numpy as np

def compare_arrays(arr1, arr2):
    """Compare two arrays element-wise and return boolean array"""
    return arr1 > arr2

# Test the function
if __name__ == "__main__":
    # Test case 1: 1D arrays
    arr1 = np.array([1, 5, 3, 8, 2])
    arr2 = np.array([2, 3, 4, 7, 5])
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"arr1 > arr2: {compare_arrays(arr1, arr2)}")
    
    # Test case 2: 2D arrays
    print("\n2D Array Comparison:")
    arr3 = np.array([[1, 5, 3], [8, 2, 6]])
    arr4 = np.array([[2, 3, 4], [7, 5, 5]])
    print(f"Array 3:\n{arr3}")
    print(f"Array 4:\n{arr4}")
    print(f"arr3 > arr4:\n{compare_arrays(arr3, arr4)}")
    
    # Additional comparison operations
    print("\nOther Comparisons:")
    print(f"arr1 < arr2: {arr1 < arr2}")
    print(f"arr1 == arr2: {arr1 == arr2}")
    print(f"arr1 >= arr2: {arr1 >= arr2}")
