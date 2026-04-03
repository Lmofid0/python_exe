# Merge Sort
def merge_sort(arr):
    # Helper to merge two sorted lists
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)
unsorted_arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(unsorted_arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]

# Quick Sort
def quicksort(arr):
    """
    Quick sort implementation
    Average: O(n log n)
    Worst: O(n²) but rarely happens with good pivot selection
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (middle element for better performance)
    pivot = arr[len(arr) // 2]
    
    # Partition
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quicksort(left) + middle + quicksort(right)

# In-place quicksort (more memory efficient)
def quicksort_inplace(arr, low=0, high=None):
    """
    In-place quicksort - O(log n) space
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    """Partition function for in-place quicksort"""
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test both versions
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numbers}")
print(f"QuickSort: {quicksort(numbers.copy())}")
print(f"In-place:  {quicksort_inplace(numbers.copy())}")


# ---------------------------------------------------------------------#
#                                Heap Sort
def heap_sort(arr):
    """
    Heap sort implementation
    Time: O(n log n)
    Space: O(1) - in-place
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is larger
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is larger
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Test
numbers = [12, 11, 13, 5, 6, 7]
print(f"Original: {numbers}")
print(f"HeapSort: {heap_sort(numbers.copy())}")




# import tracemalloc
# import random
# def memory_comparison():
#     """Compare memory usage of each sort"""
#     print("=" * 60)
#     print("MEMORY USAGE COMPARISON")
#     print("=" * 60)
    
#     size = 10000
#     arr = [random.randint(1, size) for _ in range(size)]
    
#     # Merge Sort memory
#     tracemalloc.start()
#     arr_copy = arr.copy()
#     merge_sort(arr_copy)
#     merge_memory = tracemalloc.get_traced_memory()[1]
#     tracemalloc.stop()
    
#     # Quick Sort memory
#     tracemalloc.start()
#     arr_copy = arr.copy()
#     quicksort_inplace(arr_copy)
#     quick_memory = tracemalloc.get_traced_memory()[1]
#     tracemalloc.stop()
    
#     # Heap Sort memory
#     tracemalloc.start()
#     arr_copy = arr.copy()
#     heap_sort(arr_copy)
#     heap_memory = tracemalloc.get_traced_memory()[1]
#     tracemalloc.stop()
    
#     print(f"\nMemory usage for {size} elements:")
#     print(f"Merge Sort: {merge_memory / 1024:.2f} KB")
#     print(f"Quick Sort: {quick_memory / 1024:.2f} KB")
#     print(f"Heap Sort:  {heap_memory / 1024:.2f} KB")
    
#     print(f"\nWinner: {'Heap Sort' if heap_memory < quick_memory else 'Quick Sort'}")

# memory_comparison()