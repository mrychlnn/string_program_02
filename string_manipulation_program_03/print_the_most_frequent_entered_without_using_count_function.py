# Initialize an empty list
numbers = []

# Input 5 numbers
for i in range(5):
    num = input(f"Enter number {i + 1}: ")
    numbers.append(num)

# Print the most frequent entered number 
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

most_frequent = max(frequency, key=frequency.get)
print(f"Output: {most_frequent}")