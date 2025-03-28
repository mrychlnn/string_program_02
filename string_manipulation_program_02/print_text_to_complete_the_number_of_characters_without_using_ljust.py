# Input a text
text = input("Enter the text: ")

# Ask user for the total width
width = int(input("Enter the total width: "))

# Print space at the end of the string to complete the number of characters specifies in function parameter without using ljust() function
if len(text) < width:
    text = text + ' ' * (width - len(text))

print("Output:", text)