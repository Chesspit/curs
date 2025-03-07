def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return n
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
if __name__ == "__main__":
    # Test both functions
    n = 10
    print(f"The {n}th Fibonacci number (iterative): {fibonacci_iterative(n)}")
    print(f"The {n}th Fibonacci number (recursive): {fibonacci_recursive(n)}")

All tests passed successfully!
The 10th Fibonacci number (iterative): 55
The 10th Fibonacci number (recursive): 55
