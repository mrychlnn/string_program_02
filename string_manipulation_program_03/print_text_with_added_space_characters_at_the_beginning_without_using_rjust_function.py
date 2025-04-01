# Input a text
text = input("Enter a text: ")

# Ask the user for the total length
length = int(input("Enter the total length: "))

# Print space at the beginning of the text to complete the number of characters specifies in function parameter without using rjust() function
if len(text) < length:
    padding = " " * (length - len(text))
    padded_text = padding + text

print(f'Output: {padded_text}')