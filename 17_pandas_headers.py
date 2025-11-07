# Question 17: Pandas - Get column headers from DataFrame

import pandas as pd

def get_column_headers(df):
    """Get column headers (column names) from a DataFrame"""
    return df.columns.tolist()

# Test the function
if __name__ == "__main__":
    # Create sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'LA', 'Chicago'],
        'Salary': [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame:")
    print(df)
    
    # Get column headers
    headers = get_column_headers(df)
    print("\nColumn headers:")
    print(headers)
    print(f"Number of columns: {len(headers)}")
