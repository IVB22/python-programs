# Program to get the largest number from a list

numbers = [45, 23, 78, 12, 89, 34, 67, 56, 91, 24]

# Method 1: Using max() function
largest = max(numbers)

print("List of numbers:", numbers)
print("Largest number:", largest)

# Method 2: Manual approach
largest_manual = numbers[0]
for num in numbers:
    if num > largest_manual:
        largest_manual = num
print("Largest (manual method):", largest_manual)
