# Input the user's full name
full_name = input("Enter your full name (incorrect casing): ")
words = full_name.split()  
capital_words = []

# Print the entered full name in all capital first letters in each word without using title() function
for word in words:
    capital_words.append(word.capitalize()) 

change_name = ' '.join(capital_words)  
print("Output:", change_name)