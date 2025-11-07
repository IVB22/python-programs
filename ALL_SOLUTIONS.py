"""Python Programming Solutions - All Questions

This file contains solutions to all 21 Python programming questions.
For better organization, each solution is in a separate function.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ================ Q1a: Kilogram to Pounds ================
def q1a_kg_to_pounds():
    weight_kg = float(input("Enter weight in kilograms: "))
    weight_pounds = weight_kg * 2.2
    print(f"{weight_kg} kg = {weight_pounds} pounds")

# ================ Q1b: For Loop Sequence ================
def q1b_for_loop_sequence():
    for i in range(8, 90, 3):
        print(i, end=" ")
    print()

# ================ Q2: Split String to Array ================
def q2_split_string():
    string = input("Enter a string: ")
    char_array = list(string)
    print("Character array:", char_array)

# ================ Q3: Largest Number from List ================
def q3_largest_number():
    numbers = [45, 23, 78, 12, 89, 34, 67]
    largest = max(numbers)
    print(f"Largest number: {largest}")

# ================ Q4: Fibonacci with Recursion ================
def q4_fibonacci(n):
    if n <= 1:
        return n
    return q4_fibonacci(n-1) + q4_fibonacci(n-2)

def run_q4():
    n = int(input("Enter n for Fibonacci: "))
    print(f"Fibonacci({n}) = {q4_fibonacci(n)}")

# ================ Q5: Car Class ================
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print(f"{self.make} {self.model} is now running")
    
    def stop(self):
        self.is_running = False
        print(f"{self.make} {self.model} is now stopped")

def run_q5():
    car = Car("Toyota", "Camry", 2023)
    car.start()
    car.stop()

# ================ Q6: Inheritance - Animal Classes ================
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

def run_q6():
    dog = Dog("Buddy")
    dog.eat()
    dog.bark()
    
    cat = Cat("Whiskers")
    cat.eat()
    cat.meow()

# ================ Q7: Polymorphism - Animal Sounds ================
class AnimalBase:
    def make_sound(self):
        pass

class DogSound(AnimalBase):
    def make_sound(self):
        return "Woof! Woof!"

class CatSound(AnimalBase):
    def make_sound(self):
        return "Meow! Meow!"

class Bird(AnimalBase):
    def make_sound(self):
        return "Tweet! Tweet!"

def run_q7():
    animals = [DogSound(), CatSound(), Bird()]
    for animal in animals:
        print(animal.make_sound())

# ================ Q8: Error Handling - Division by Zero ================
def q8_error_handling():
    try:
        num = float(input("Enter numerator: "))
        den = float(input("Enter denominator: "))
        result = num / den
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")

# ================ Q9a: NumPy - Test for Zero ================
def q9a_numpy_zero_test():
    arr = np.array([1, 2, 3, 4, 5])
    has_no_zero = np.all(arr != 0)
    print(f"Array has no zeros: {has_no_zero}")

# ================ Q9b: NumPy - Element-wise Comparison ================
def q9b_numpy_comparison():
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([2, 2, 3, 3, 6])
    
    print("Greater:", np.greater(arr1, arr2))
    print("Greater or Equal:", np.greater_equal(arr1, arr2))
    print("Less:", np.less(arr1, arr2))
    print("Less or Equal:", np.less_equal(arr1, arr2))
    print("Equal:", np.equal(arr1, arr2))
    print("All Close:", np.allclose(arr1, arr2))

# ================ Q10: NumPy - Extract Numbers ================
def q10_numpy_extract():
    arr = np.array([1, 5, 10, 15, 20, 25, 30])
    threshold = 15
    less_than = arr[arr < threshold]
    greater_than = arr[arr > threshold]
    print(f"Less than {threshold}:", less_than)
    print(f"Greater than {threshold}:", greater_than)

# ================ Q11: NumPy - Find Indices ================
def q11_numpy_indices():
    arr = np.array([[1, 5, 3], [4, 2, 6]])
    max_indices = np.argmax(arr, axis=1)
    min_indices = np.argmin(arr, axis=1)
    print("Max indices along axis 1:", max_indices)
    print("Min indices along axis 1:", min_indices)

# ================ Q12: Pandas - Create Series ================
def q12_pandas_series():
    data = [10, 20, 30, 40, 50]
    series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
    print("Pandas Series:")
    print(series)

# ================ Q13: Pandas - Series to List ================
def q13_pandas_to_list():
    series = pd.Series([1, 2, 3, 4, 5])
    py_list = series.tolist()
    print("Python list:", py_list)
    print("Type:", type(py_list))

# ================ Q14-17: Pandas DataFrames ================
def create_exam_dataframe():
    exam_data = {
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    return pd.DataFrame(exam_data, index=labels)

def q14_create_dataframe():
    df = create_exam_dataframe()
    print("DataFrame with index labels:")
    print(df)

def q15_change_name():
    df = create_exam_dataframe()
    df.loc[df['name'] == 'James', 'name'] = 'Suresh'
    print("DataFrame after changing name:")
    print(df)

def q16_insert_column():
    df = create_exam_dataframe()
    df['grade'] = ['A', 'C', 'A', 'F', 'C', 'A', 'A', 'F', 'C', 'A']
    print("DataFrame with new column:")
    print(df)

def q17_column_headers():
    df = create_exam_dataframe()
    headers = df.columns.tolist()
    print("Column headers:", headers)

# ================ Q18-21: Data Visualization ================
def q18_plots_analysis():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('Sine Wave Analysis')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def q19_subplot_layout():
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
    
    ax1.scatter(x, y)
    ax1.set_title('Scatter Plot')
    
    ax2.plot(x, y)
    ax2.set_title('Line Plot')
    
    ax3.bar(range(10), range(10))
    ax3.set_title('Bar Plot')
    
    plt.tight_layout()
    plt.show()

def q20_time_series():
    dates = pd.date_range('2024-01-01', periods=100)
    values = np.random.randn(100).cumsum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(dates, values)
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def q21_3d_scatter():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.random.randn(100)
    y = np.random.randn(100)
    z = np.random.randn(100)
    
    ax.scatter(x, y, z, c='blue', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Scatter Plot')
    plt.show()

# ================ Main Menu ================
def main():
    print("\n===== Python Programming Solutions =====")
    print("All solution functions are defined.")
    print("Call any function to run its solution.")
    print("Example: q1a_kg_to_pounds()")
    print("========================================\n")

if __name__ == "__main__":
    main()
