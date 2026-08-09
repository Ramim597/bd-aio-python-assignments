# Q6. Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# Create a dictionary that maps each word to its length.

# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]
word_with_length = {}
for word in words:
    word_with_length[word] = len(word)

print(word_with_length)
