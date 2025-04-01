# Input a string
string = input("Enter a string: ")

# Input the character that you want to locate
char_find = input("Enter the character that you want to locate: ")

# Print The position where the last character was located
for i in range(len(string) - 1, -1, -1):
    if string[i] == char_find:
        print("Output:", i)
        break
else:
    print(f"'{char_find}' not found")