# Input a first name
first_name = input("Enter your first name: ")

# Print 'Yes' or 'No' if the name is in all lower case
all_lower = "Yes, the entered name is all in lower case"
for char in first_name:
    if 'A' <= char <= 'Z':  
        all_lower = "No, the entered name contains a big letter/s"
        break

# Print result
print(all_lower)