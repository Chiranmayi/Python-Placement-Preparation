
def first_non_repeating(text):
    # Remove spaces from the input
    text = text.replace(" ", "")

    # Count the frequency of each character
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Find the first non-repeating character
    for char in text:
        if freq[char] == 1:
            return char

    return "No non-repeating character found"


# Test cases
print(first_non_repeating("programming"))
print(first_non_repeating("aabbcdd"))
print(first_non_repeating("aabbcc"))
print(first_non_repeating("a b c"))
print(first_non_repeating("Aa"))
print(first_non_repeating(""))
print(first_non_repeating("   "))
print(first_non_repeating("a"))
