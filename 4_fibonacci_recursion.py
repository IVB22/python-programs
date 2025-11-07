# Program to calculate nth Fibonacci number using recursion

def fibonacci(n):
    """Calculate nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Get input from user
n = int(input("Enter n to find the nth Fibonacci number: "))

if n < 0:
    print("Please enter a positive number")
else:
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
    
    # Print first n Fibonacci numbers
    print(f"\nFirst {n+1} Fibonacci numbers:")
    for i in range(n+1):
        print(fibonacci(i), end=" ")
    print()
