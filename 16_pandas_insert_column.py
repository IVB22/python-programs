# Question 16: Pandas - Insert a new column at specified location

import pandas as pd

def insert_column_at_position(df, position, column_name, column_data):
    """Insert a new column at a specified location in DataFrame"""
    df.insert(position, column_name, column_data)
    return df

# Test the function
if __name__ == "__main__":
    # Create sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'LA', 'Chicago']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    # Insert a new column 'Salary' at position 2
    df_updated = insert_column_at_position(df.copy(), 2, 'Salary', [50000, 60000, 70000])
    
    print("\nDataFrame after inserting 'Salary' column at position 2:")
    print(df_updated)
