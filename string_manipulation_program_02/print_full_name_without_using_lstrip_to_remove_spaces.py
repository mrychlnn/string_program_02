# Input full name with spaces at the beginning 
full_name = input("Enter your full name (with several spaces at the beginning): ")

# Find the index of the first non-space character
index = 0
while index < len(full_name) and full_name[index] == ' ':
    index += 1

# Slice the string from the first non-space character
remove_spaces = full_name[index:]

# Print the full name without the spaces at the beginning 
print("Output:", remove_spaces)