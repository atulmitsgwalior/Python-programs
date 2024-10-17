# Find the maximum of the list of numbers
# Method 1
# Define a list of numbers
numbers = [3, 5, 2, 8, 1, 9, 4]

# Find the maximum value
maximum_value = max(numbers)
print(f"The maximum value in the list is: {maximum_value}")


# Method 2
# Define a list of numbers
numbers = [3, 5, 2, 8, 1, 9, 4]

# Initialize the maximum value as the first element
maximum_value = numbers[0]

# Iterate through the list to find the maximum
for num in numbers:
    if num > maximum_value:
        maximum_value = num

print(f"The maximum value in the list is: {maximum_value}")
