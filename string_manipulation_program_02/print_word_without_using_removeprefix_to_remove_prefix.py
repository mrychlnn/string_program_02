# Input a word
word = input("Enter a word: ")

# Ask the user what prefix to be removed
prefix = input("Enter the prefix to remove: ")

if word.startswith(prefix):
    word = word[len(prefix):]

# Print the entered word without prefix
print("Output:", word)