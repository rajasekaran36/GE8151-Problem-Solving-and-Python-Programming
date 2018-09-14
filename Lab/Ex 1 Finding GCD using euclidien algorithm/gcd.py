print("GCD Finder")
print("----------")
print("Enter NUMBER 1 :")
num1 = int(input())
print("Enter NUMBER 2 :")
num2 = int(input())

a = num1
b = num2

while(a!=b):
    if(a>b):
        a = a - b
    else:
        b = b - a
print("GCD of given numbers",num1,"and",num2,"is",a);