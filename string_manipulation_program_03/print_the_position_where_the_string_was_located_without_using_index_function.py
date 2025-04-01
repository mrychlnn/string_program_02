# Input a text
text = input("Enter a text: ")

# Input the character that you want to locate
search_char = input("Enter the character that you want to locate: ")

position = text.find(search_char)

# Print the location of the character that the user searching for
if position != -1:
    print("Found the character at position:", position)
else:
    print("The character was not found")