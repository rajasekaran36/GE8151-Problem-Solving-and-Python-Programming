print("Sum of digits")
print("-------------")

number = int(input("Enter any number"))
sum = 0
while (number != 0):
    d = number % 10
    sum = sum + d
    number = number//10
print ("Sum of digits :",sum)