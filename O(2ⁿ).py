def fibonacci_naive(n):
    """
    Recursive Fibonacci - Classic O(2ⁿ) example
    Each call creates 2 more calls!
    """
    if n <= 1:
        return n
    
    # This creates exponential branching
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
print(f"Fibonacci Naive (n=10): {fibonacci_naive(10)}")

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Move n disks from source rod to target rod
    Using auxiliary rod as helper
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, target)
    
    # Move largest disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, target, source)


# Example usage
print("Tower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')