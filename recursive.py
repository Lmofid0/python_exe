# def recursive_sum(arr):
#     if len(arr) == 0:
#         return 0
#     # Recursive case: first element + sum of rest
#     return arr[0] + recursive_sum(arr[1:])
# numbers = [1, 2, 3, 4, 5]
# print(recursive_sum(numbers))  # Output: 15
def sum_natural(n):
    if n <= 1:
        return n
    return n + sum_natural(n - 1)
print(sum_natural(11))  # Output: 66

# --------------------------------------------------#
def recursive_subtract_safe(a, b):
    if b == 0:
        return a
    elif b > 0:
        return recursive_subtract_safe(a - 1, b - 1)
    else:  # b is negative
        return recursive_subtract_safe(a + 1, b + 1)
print(recursive_subtract_safe(10, -3)) # Output: 13

# --------------------------------------------------#
def recursive_multiply(a, b):
    # Handle negative numbers
    if b < 0:
        return -recursive_multiply(a, -b)
    # Base cases
    if b == 0:
        return 0
    if b == 1:
        return a
    # Recursive case: a + (a * (b-1))
    return a + recursive_multiply(a, b - 1)
print(recursive_multiply(5, -3))  # Output: -15

# --------------------------------------------------#
def recursive_divide(dividend, divisor):
    # Handle division by zero
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    
    # Handle negative numbers
    if dividend < 0 and divisor < 0:
        return recursive_divide(-dividend, -divisor)
    elif dividend < 0:
        return -recursive_divide(-dividend, divisor)
    elif divisor < 0:
        return -recursive_divide(dividend, -divisor)
    
    # Base case: dividend < divisor
    if dividend < divisor:
        return 0
    
    # Recursive case: 1 + division of remainder
    return 1 + recursive_divide(dividend - divisor, divisor)
print(recursive_divide(15, 4))  # Output: 3


# O(1)-constant time
def dict_lookup(d, key):
    return d.get(key, None)
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(dict_lookup(my_dict, 'b')) # Output: 2

def get_first_element(arr):
    if len(arr) == 0:
        return None
    return arr[0]
print(get_first_element([10, 20, 30]))  # Output: 10

def if_even(n):
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'
print(if_even(4))  # Output: 'even'

# O(log n)-logarithmic time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(sorted_arr, 5))  # Output: 4

def fast_exponentiation(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half = fast_exponentiation(base, exp // 2)
        return half * half
    else:
        return base * fast_exponentiation(base, exp - 1)
print(fast_exponentiation(2, 10))  # Output: 1024