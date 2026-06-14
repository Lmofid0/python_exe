# O(n) Time Complexity examples

def lin_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(lin_search([1, 2, 3, 4, 5], 3))  # Output: 2
#recursive version
def rec_lin_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return rec_lin_search(arr, target, index + 1)
print(rec_lin_search([1, 2, 3, 4, 5], 3))  # Output: 2

#exemple 2
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
print(sum_array([1, 2, 3, 4, 5]))  # Output: 15
#recursive version
def rec_sum_array(arr, index=0):
    if index >= len(arr):
        return 0
    return arr[index] + rec_sum_array(arr, index + 1)
print(rec_sum_array([1, 2, 3, 4, 5]))  # Output: 15

#exemple 3
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
print(find_max([1, 2, 3, 4, 5]))  # Output: 5
#recursive version
def rec_find_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    max_of_rest = rec_find_max(arr, index + 1)
    return arr[index] if arr[index] > max_of_rest else max_of_rest
print(rec_find_max([1, 2, 3, 4, 5]))  # Output: 5

#exemple 4
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
print(count_occurrences([1, 2, 3, 4, 5, 3, 3], 3))  # Output: 3
#recursive version
def rec_count_occurrences(arr, target, index=0):
    if index >= len(arr):
        return 0
    return (arr[index] == target) + rec_count_occurrences(arr, target, index + 1)
print(rec_count_occurrences([1, 2, 3, 4, 5, 3, 3], 3))  # Output: 3