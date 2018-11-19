def prime_finder(number):
    is_prime = True
    if (number==1 or number==2 or number==3):
        return is_prime
    else:
        for i in range (2,number):
            if(number%i == 0):
                is_prime = False
                break
    return is_prime

print ("Finding N Prime numbers")
print ("-----------------------")
limit = int(input("Enter limit:"))
count = 0
i = 1
while(count != limit):
    is_prime = prime_finder(i)
    if(is_prime):
        print(i)
        count+=1
    i+=1