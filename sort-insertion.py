# Insertion Sort
def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key
    return arr

# Get the list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

# Sort the list using insertion sort
sorted_numbers = insertion_sort(numbers)

# Display the sorted list
print(f"Sorted list using insertion sort: {sorted_numbers}")
