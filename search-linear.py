# Prog5-A Linear Search
#  
def linear_search(arr, target):
    # Iterate through the list
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Get the list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

# Get the target from the user
target = int(input("Enter the number you want to search for: "))

# Call the function with the target
result = linear_search(numbers, target)

# Display the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
