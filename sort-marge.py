def merge_sort(arr):
    # Base case: if the list is of length 1 or 0, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point and divide the array into left and right halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compare elements from left and right lists and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append any remaining elements from left and right lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Get the list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

# Sort the list using merge sort
sorted_numbers = merge_sort(numbers)

# Display the sorted list
print(f"Sorted list using merge sort: {sorted_numbers}")
