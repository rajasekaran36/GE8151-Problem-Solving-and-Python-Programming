alist = []
print ("enter any 5 numbers")
for i in range(5):
    data = int(input())
    alist.append(data)
max = alist[0]
for element in alist:
    if (element > max):
        max = element
print("Maximum in the list" ,alist,"is:",max)