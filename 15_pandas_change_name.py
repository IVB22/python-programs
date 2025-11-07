# Question 15: Pandas - Change the name 'James' to 'Suresh' in a column

import pandas as pd

def change_name_in_column(df, column_name, old_name, new_name):
    """Change a specific name in a DataFrame column"""
    df[column_name] = df[column_name].replace(old_name, new_name)
    return df

# Test the function
if __name__ == "__main__":
    # Create sample DataFrame
    data = {
        'Name': ['James', 'John', 'James', 'Emma', 'James'],
        'Age': [25, 30, 28, 32, 27],
        'City': ['NY', 'LA', 'Chicago', 'Boston', 'Miami']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    # Change 'James' to 'Suresh'
    df_updated = change_name_in_column(df.copy(), 'Name', 'James', 'Suresh')
    
    print("\nUpdated DataFrame:")
    print(df_updated)
