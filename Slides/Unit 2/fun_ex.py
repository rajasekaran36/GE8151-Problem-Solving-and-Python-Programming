def leap_year_finder(x_year):
    if (x_year%4 == 0):
        if(x_year%100 == 0):
            if(x_year%400 == 0):
                print ("Leap Year")
            else:
                print("Not Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")

y = 2000
leap_year_finder(y)