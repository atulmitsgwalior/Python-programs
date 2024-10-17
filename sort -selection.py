#Selection Sort
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Get the list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

# Sort the list using selection sort
sorted_numbers = selection_sort(numbers)

# Display the sorted list
print(f"Sorted list using selection sort: {sorted_numbers}")
