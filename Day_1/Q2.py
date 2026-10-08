# Accept two values S and N , print sq of first N numbers starting from S

S=int(input("Enter the Num 1 :"))
N=int(input("Enter the Num 2 :"))
for i in range(N):
    print((S+i)**2)