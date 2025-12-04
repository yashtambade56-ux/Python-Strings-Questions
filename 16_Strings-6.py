# Count occurrences of a specific character in a string.
string = input("Enter a string: ")
char = input("Enter the character to count: ")
count = string.count(char)
print(f"The character '{char}' occurs {count} times in the string.")