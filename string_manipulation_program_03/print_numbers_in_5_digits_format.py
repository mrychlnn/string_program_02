# Input a 1-3 digits numbers
num = int(input("Enter a number (0-999): "))

# Format the number as 6 digits string with leading zeros
five_digits = f"{num:05d}"

# Print the number with zero characters at the beginning to complete the 5 digits format
print("Output:", five_digits)