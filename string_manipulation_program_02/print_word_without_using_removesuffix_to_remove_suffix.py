# Input a word
word = input("Enter a word: ")

# Ask the user what prefix to be removed
suffix = input("Enter the suffix to remove: ")

if word.endswith(suffix):
    word = word[:-len(suffix)]

# Print the word without the specific suffix
print("Output:", word)