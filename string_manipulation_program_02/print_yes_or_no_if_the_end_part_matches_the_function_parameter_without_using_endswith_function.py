# Input a complete statement
statement = input("Enter a complete statement: ")

# Ask the user what to check in the ending part
ending_part = input("Enter the ending to check: ")

# Print 'Yes' or 'No' if the end part matches the funtion parameter without using endswith() function
if statement[-len(ending_part):] == ending_part:
    print("Yes")
else:
    print("No")