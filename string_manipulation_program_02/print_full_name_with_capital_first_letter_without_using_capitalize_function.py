# Input the user's full name
full_name = input("Enter your full name (incorrect casing): ")

# Convert the first letter to upper case and the rest will be lower case manually
change_name = full_name[0].upper() + full_name[1:].lower()

# Print the first letter of the full name in capital letter and the rest is small letter
print("Output:", change_name)