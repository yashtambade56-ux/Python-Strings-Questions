# Check if a given string is a palindrome.

num = input("Enter a string: ")
if num == num[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")