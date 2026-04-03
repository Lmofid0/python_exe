def fibonacci_naive(n):
    """
    Recursive Fibonacci - Classic O(2ⁿ) example
    Each call creates 2 more calls!
    """
    if n <= 1:
        return n
    
    # This creates exponential branching
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
print(f"Fibonacci Naive (n=10): {fibonacci_naive(30)}")