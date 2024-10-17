# Prog 5 Binary Search 

def binary_search(arr, target):
    # Initial left and right pointers
    left, right = 0, len(arr) - 1

    while left <= right:
        # Find the middle element
        mid = left + (right - left) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1  # Ignore the left half
        else:
            right = mid - 1  # Ignore the right half

    return -1  # Return -1 if the target is not found

# Get the list of numbers from the user
numbers = input("Enter a sorted list of numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

# Get the target from the user
target = int(input("Enter the number you want to search for: "))

# Call the function with the target
result = binary_search(numbers, target)

# Display the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
