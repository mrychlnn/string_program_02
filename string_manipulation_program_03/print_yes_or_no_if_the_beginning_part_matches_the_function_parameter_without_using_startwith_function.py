# Input a complete statement
statement = input("Enter a complete statement: ")

# Ask the user what to check in the beginning part
beginning_part = input("Enter the beginning to check: ")

# Print 'Yes' or 'No' if the beginning part matches the function parameter without using startswith() function
if statement[:len(beginning_part)] == beginning_part:
    print(f"Yes. It starts with {beginning_part}")
else:
    print(f"No. It doesn't start with {beginning_part} ")