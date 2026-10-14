# Program to count vowels in a file

file = open("sample.txt", "r")
content = file.read()
file.close()
count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count = count + 1
print("Total number of vowels:", count)
