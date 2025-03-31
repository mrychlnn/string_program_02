# Input a first name 
first_name = input("Enter your first name: ")

# Print 'Yes" or 'No' if the name is in all capital letter or not
all_caps = "Yes, the entered name is all in upper case"
for char in first_name:
    if 'a' <= char <= 'z': 
        all_caps = "No, the entered name contains a small letter/s"
        break

# Print result
print(all_caps)