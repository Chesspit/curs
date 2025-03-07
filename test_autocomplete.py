def maximum(lst):
    """
    Find the maximum value in a list.
    Args:
        lst (list): List of comparable elements (numbers or strings)
    Returns:
        The maximum value in the list
    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains elements that can't be compared
    """
    if not lst:
        raise ValueError("Cannot find maximum of empty list")
    
    try:
        max_value = lst[0]
        for item in lst[1:]:
            if item > max_value:
                max_value = item
        return max_value
    except TypeError as e:
        raise TypeError("List contains elements that cannot be compared") from e

# Example usage:
if __name__ == "__main__":
    # Test with numbers
    numbers = [4, 2, 9, 7, 1, 8, 3]
    print(f"Maximum of numbers: {maximum(numbers)}")  # Should print 9
    
    # Test with strings
    words = ["apple", "zebra", "banana", "cat"]
    print(f"Maximum of strings: {maximum(words)}")  # Should print "zebra"
    
    # Test error cases
    try:
        print(maximum([]))  # Empty list
    except ValueError as e:
        print(f"Error: {e}")
        
    try:
        print(maximum([1, "2", 3]))  # Mixed types that can't be compared
    except TypeError as e:
        print(f"Error: {e}")
git remote -v
