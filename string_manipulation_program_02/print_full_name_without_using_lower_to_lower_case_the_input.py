# Input the full name of the user
full_name = input("Enter your full name (incorrect casing): ")

# Convert to lowercase manually
result = ""
for character in full_name:
    if 'A' <= character <= 'Z':  
        result += chr(ord(character) + 32)  
    else:
        result += character  

# Print the full name in lower case without using lower() function
print("Output:", result)