def recursive_sum(arr):
    # Base case: empty list
    if len(arr) == 0:
        return 0
    # Recursive case: first element + sum of rest
    return arr[0] + recursive_sum(arr[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))  # Output: 15