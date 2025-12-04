# Find the longest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)