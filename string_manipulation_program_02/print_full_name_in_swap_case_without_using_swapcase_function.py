# Input a word
word_input = input("Enter a word (incorrect casing): ")

# Print the word in swap case of the entered word
result = ""
for character in word_input:
    if 'A' <= character <= 'Z':  
        result += chr(ord(character) + 32)
    else:
        result += chr(ord(character) - 32)
        
print("Output:", result)