# Input the full name of the user
full_name = input("Enter yout full name (incorrect casing): ")

# Convert to upper case manually
result = ""
for character in full_name:
    if 'a' <= character <= 'z':  
        result += chr(ord(character) - 32)  
    else:
        result += character  

# Print the entered full name in upper case without using isupper() function
print("Output:", result)