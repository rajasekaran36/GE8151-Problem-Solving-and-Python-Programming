import math

def power_finder(number,power):
    res = 1
    for i in range(power):
        res = res * number
    return res

def fact_finder(number):
    if(number <= 1):
        return 1
    else:
        return number*fact_finder(number - 1)

#number = int(input("Enter any number"))
number = 3
result = 0

for i in range (100):
    result = result + (power_finder(number,i)/fact_finder(i))
    print(i,power_finder(number,i),fact_finder(i),result)
print(result)