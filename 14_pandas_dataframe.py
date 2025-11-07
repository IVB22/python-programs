# Question 14: Pandas - Create a DataFrame from a dictionary

import pandas as pd

def create_dataframe_from_dict(data_dict):
    """Create a Pandas DataFrame from a dictionary"""
    return pd.DataFrame(data_dict)

# Test the function
if __name__ == "__main__":
    # Test case 1: Simple dictionary
    data1 = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']
    }
    df1 = create_dataframe_from_dict(data1)
    print("DataFrame from dictionary:")
    print(df1)
    
    # Test case 2: Students data
    data2 = {
        'Student': ['John', 'Emma', 'Michael'],
        'Math': [85, 92, 78],
        'Science': [88, 95, 82],
        'English': [90, 88, 85]
    }
    df2 = create_dataframe_from_dict(data2)
    print("\nStudent grades DataFrame:")
    print(df2)
