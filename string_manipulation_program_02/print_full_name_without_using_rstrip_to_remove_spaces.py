# Input the full name with trailing spaces
full_name = input("Enter your full name (with trailing spaces): ")

# Find the index of the first non-space character
index = len(full_name) - 1
while index >= 0 and full_name[index] == ' ':
    index -= 1

# Slice the string from the first non-space character
remove_spaces = full_name[:index + 1]

# Print the full name without the spaces at the end
print("Output:", remove_spaces)