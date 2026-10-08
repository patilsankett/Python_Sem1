# Accept Sentence from user and count the vowels

sentence = input("Enter a sentence: ")

count = 0
for char in sentence:
    if char in "AEIOUaeiou":
        count += 1
print("Number of vowels:", count)