# Input a complete statement
statement = input("Enter a complete statement: ")

# Ask the user what to check in the ending part
ending_part = input("Enter the ending to check: ")

# Print 'Yes' or 'No' if the end part matches the funtion parameter without using endswith() function
if statement[-len(ending_part):] == ending_part:
    print(f"Yes. It ends with {ending_part}")
else:
    print(f"No. It doesn't end with {ending_part} ")