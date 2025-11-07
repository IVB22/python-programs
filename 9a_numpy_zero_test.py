# Question 9a: NumPy - Test whether any of the elements is zero

import numpy as np

def test_for_zeros(arr):
    """Test if any element in the array is zero"""
    return np.any(arr == 0)

# Test the function
if __name__ == "__main__":
    # Test case 1: Array with zeros
    arr1 = np.array([1, 2, 0, 4, 5])
    print(f"Array 1: {arr1}")
    print(f"Contains zero: {test_for_zeros(arr1)}")
    
    # Test case 2: Array without zeros
    arr2 = np.array([1, 2, 3, 4, 5])
    print(f"\nArray 2: {arr2}")
    print(f"Contains zero: {test_for_zeros(arr2)}")
    
    # Test case 3: 2D array with zeros
    arr3 = np.array([[1, 2, 3], [0, 5, 6], [7, 8, 9]])
    print(f"\nArray 3:\n{arr3}")
    print(f"Contains zero: {test_for_zeros(arr3)}")
    
    # Test case 4: Array with all zeros
    arr4 = np.zeros(5)
    print(f"\nArray 4: {arr4}")
    print(f"Contains zero: {test_for_zeros(arr4)}")
