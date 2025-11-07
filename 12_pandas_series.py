# Question 12: Pandas - Create a Series from a list

import pandas as pd

def create_series_from_list(data_list):
    """Create a Pandas Series from a list"""
    return pd.Series(data_list)

# Test the function
if __name__ == "__main__":
    # Test case 1: List of numbers
    numbers = [10, 20, 30, 40, 50]
    series1 = create_series_from_list(numbers)
    print("Series from numbers:")
    print(series1)
    
    # Test case 2: List of strings
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    series2 = create_series_from_list(fruits)
    print("\nSeries from strings:")
    print(series2)
    
    # Test case 3: List with custom index
    data = [100, 200, 300]
    series3 = pd.Series(data, index=['a', 'b', 'c'])
    print("\nSeries with custom index:")
    print(series3)
