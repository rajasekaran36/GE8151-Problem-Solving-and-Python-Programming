print("Insertion Sort")
print("--------------")
alist = []
print ("enter any 5 numbers")
for i in range(5):
    data = int(input())
    alist.append(data)

print("Unsorted List",alist)
for i in range(len(alist)):
   pivot = i
   while pivot > 0 and alist[pivot]<alist[pivot-1]:
       (alist[pivot],alist[pivot-1]) = (alist[pivot-1],alist[pivot])
       pivot = pivot - 1
       
print("Sorted List",alist)