def create_frequency_table(input_list):
    """
    Create a frequency table from a list of elements.
    Args:
        input_list (list): List of elements to count frequencies for
    Returns:
        dict: Dictionary with elements as keys and their frequencies as values
    """
    freq_table = {}
    for item in input_list:
        if item in freq_table:
            freq_table[item] += 1
        else:
            freq_table[item] = 1
    return freq_table

# Example usage:
if __name__ == "__main__":
    # Test with numbers
    test_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    frequencies = create_frequency_table(test_list)
    print("Number frequency table:", frequencies)

    # Test with mixed data types
    complex_list = [
        "apple", "banana", "apple", "cherry",
        1, 2, 2, 1, 3,
        True, False, True,
        3.14, 2.718, 3.14,
        None, None,
        ("tuple", 1), ("tuple", 1),
        "banana"
    ]
    complex_frequencies = create_frequency_table(complex_list)
    print("\nComplex frequency table:")
    for item, freq in sorted(complex_frequencies.items(), key=lambda x: (-x[1], str(x[0]))):
        print(f"{item}: {freq}")

    # Test with a text string split into words
    text = "the quick brown fox jumps over the lazy dog the fox was quick"
    word_frequencies = create_frequency_table(text.split())
    print("\nWord frequency table:")
    for word, freq in sorted(word_frequencies.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word}: {freq}")
