def longest_even(text):
    longest = '00'
    for word in text.split():
        if len(word) % 2 == 0 and len(word) >= len(longest):
            longest = word
    return longest

strings = [
    "Feel free to customize this",
    "",
    "Run the program",
    "a bb ccc dddd fffff",
]

for string in strings:
    print(f'in "{string}" the longest even word is -> "{longest_even(string)}"')