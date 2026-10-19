# Take 2 num from User and print its Div and Remainder by using Function
a = int(input("Enter Num 1 :"))
b = int(input("Enter Num 2 :"))

def my_func (a,b):
    div = a // b
    remain = a%b
    print(div , remain)
print(my_func(a,b))  


#Table of num using Function
x = int(input("Enter a Num to print its table :"))
i =1
def table(x):
    for i in range(1,11):
        print(x ,"*",i,"=",x*i)
       
table(x)