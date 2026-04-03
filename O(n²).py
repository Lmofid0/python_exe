def bubble_sort(arr):
    """
    Bubble Sort - Classic O(n²) sorting algorithm
    Each pass "bubbles" the largest element to the end
    """
    n = len(arr)
    steps = 0
    
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            steps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr, steps

# Demonstration
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, steps = bubble_sort(numbers.copy())
print(f"Original: {numbers}")
print(f"Bubble Sort: {sorted_arr}")
print(f"Steps for n={len(numbers)}: {steps} (n²/2 = {len(numbers)**2//2})")

# -----------------------------------#
#            selection sort           #
def selection_sort(arr):
    """
    Selection Sort - Find minimum and place at beginning
    Always O(n²) even on sorted data!
    """
    n = len(arr)
    steps = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr, steps

# Demonstration
numbers = [64, 25, 12, 22, 11]
sorted_arr, steps = selection_sort(numbers.copy())
print(f"Original: {numbers}")
print(f"Selection Sort: {sorted_arr}")
print(f"Steps: {steps}") 