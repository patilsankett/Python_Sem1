#Reverse the accepted string 

strng=input("Enter the String :")
rev_strng=""

for i in range(len(strng)-1,-1,-1):
    rev_strng += strng[i]
print("Reverse String :",rev_strng)