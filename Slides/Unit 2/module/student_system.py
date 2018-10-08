print ("Student Grade Calculator")
print ("------------------------")

name = input("Enter name :")
roll_no = int(input("Enter roll no :"))

m1 = int(input("Enter mark1 :"))
m2 = int(input("Enter mark2 :"))
m3 = int(input("Enter mark3 :"))

total = m1 + m2 + m3

avg = total/3

print("Total :", total)
print("Avg :",avg)

#check for grade

if (avg>90):
    print ("O Grade")
elif (avg>80 and avg<=90):
    print ("A Grade")
elif (avg>70 and avg<=80):
    print ("B Grade")
elif (avg>60 and avg<=70):
    print ("C Grade")
elif (avg>50 and avg<=60):
    print ("D Grade")
else:
    print ("F Grade")
