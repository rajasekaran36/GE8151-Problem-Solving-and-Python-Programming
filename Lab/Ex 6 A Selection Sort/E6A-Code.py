print("Selection Sort")
print("--------------")
alist = []
print ("enter any 5 numbers")
for i in range(5):
    data = int(input())
    alist.append(data)

print("Unsorted List",alist)
for i in range(0,len(alist)-1):
    minimum = i;
    for j in range(i+1, len(alist)):
        if(alist[j] < alist[minimum]):
           minimum = j
    if (minimum !=i):
                   alist[i],alist[minimum] = alist[minimum],alist[i]

print("Sorted List",alist)