def fact_finder(number):
    if(number == 1):
        return 1
    else:
        return number * fact_finder(number-1)

aNumber = int(input("Enter any number to find factorial : "))
result = fact_finder(aNumber)
print("Factorial of",aNumber,"is",result)