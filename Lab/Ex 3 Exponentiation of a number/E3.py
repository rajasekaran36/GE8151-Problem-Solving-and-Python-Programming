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

print ("E^x finder")
print ("----------")
number = int(input("Enter any number : "))
result = 0

for i in range (10):
    power_value = power_finder(number,i)
    fact_value = fact_finder(i)
    current_term = power_value/fact_value
    result = result + current_term
print("E^",number,"value is",result)
