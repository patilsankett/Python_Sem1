#program to count letters in string
txt = input("Enter the Text :")
letter_counts=0

for char in txt:
    if char.isalpha():
        letter_counts +=1
print("Total letters in the string are :",letter_counts)    #char.isalpha() : Count letters only (ignore numbers/spaces)