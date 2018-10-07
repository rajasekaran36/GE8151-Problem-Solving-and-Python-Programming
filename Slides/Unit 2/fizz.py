for i in range(1,31):
    if(i%3 == 0):
        p = "Fizz"
        if(i%5 == 0):
            p = p+"Buzz"
    else:
        p = i
    print(p, end=" ")