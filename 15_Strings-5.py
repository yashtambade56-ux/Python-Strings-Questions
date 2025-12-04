# Input a sentence and print each word on a new line.

sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)