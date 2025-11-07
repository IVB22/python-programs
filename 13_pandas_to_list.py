# Question 13: Pandas - Convert Pandas Series to Python list

import pandas as pd

def series_to_list(series):
    """Convert Pandas Series to Python list"""
    return series.tolist()

# Test the function
if __name__ == "__main__":
    # Create a Pandas Series
    series1 = pd.Series([10, 20, 30, 40, 50])
    print("Original Series:")
    print(series1)
    print(f"Type: {type(series1)}")
    
    # Convert to list
    list1 = series_to_list(series1)
    print("\nConverted to list:")
    print(list1)
    print(f"Type: {type(list1)}")
    
    # Test with strings
    series2 = pd.Series(['apple', 'banana', 'cherry'])
    list2 = series_to_list(series2)
    print("\nString series to list:")
    print(f"Series: {series2.tolist()}")
    print(f"List: {list2}")
