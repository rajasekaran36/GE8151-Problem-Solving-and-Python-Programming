print("Linear Search")
print("-------------")
alist = []
print ("enter any 5 numbers")
for i in range(5):
    data = int(input())
    alist.append(data)

key = int(input("Enter any number to search"))
found = False
for element in alist:  
    if (element == key):
        found = True
        break
if(found):
    print("Element Found")
else:
    print("Element not Found")
