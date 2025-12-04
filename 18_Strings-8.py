# Remove duplicate characters from a string.

s = input("Enter string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)
