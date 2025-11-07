# Question 8: Demonstrate error handling with try-except
# Handle division by zero error

def divide_numbers(a, b):
    """Divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numeric values!"

# Test the function
if __name__ == "__main__":
    # Test cases
    print("Test 1: 10 / 2 =", divide_numbers(10, 2))
    print("Test 2: 15 / 3 =", divide_numbers(15, 3))
    print("Test 3: 20 / 0 =", divide_numbers(20, 0))  # Division by zero
    print("Test 4: 10 / 'a' =", divide_numbers(10, 'a'))  # Type error
    
    # Interactive example
    print("\nInteractive Division:")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = divide_numbers(num1, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
