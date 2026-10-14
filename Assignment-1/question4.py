# Program to count total and unique words in a file

file = open("sample.txt", "r")
content = file.read()
file.close()
words = content.lower().split()
print("Total number of words:", len(words))
unique_words = set(words)
print("Unique words:", sorted(unique_words))
