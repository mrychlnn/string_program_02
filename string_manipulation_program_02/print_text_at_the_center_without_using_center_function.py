# Input a text
text_input = input("Enter a text: ")

# Ask user a width for centering
width = int(input("Enter the total width for centering: "))

# Print the centered text
if len(text_input) >= width:
    print(text_input)
else:
    total_spaces = width - len(text_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    
    centered_text = " " * left_spaces + text_input + " " * right_spaces
    print(centered_text)