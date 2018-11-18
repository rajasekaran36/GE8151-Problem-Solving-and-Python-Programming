def mergesort(alist):
    if (len(alist)<2):
        return alist
    mid = int(len(alist)/2)
    x = mergesort(alist[:mid])
    y = mergesort(alist[mid:])
    out = []
    i = 0
    j = 0
    while i<len(x) and j<len(y):
        if(x[i]>y[j]):
            out.append(y[j])
            j+=1
        else:
            out.append(x[i])
            i+=1
    out = out + x[i:]
    out = out + y[j:]
    return out

print("Merge Sort")
print("----------")
alist = []
print ("enter any 5 numbers")
for i in range(5):
    data = int(input())
    alist.append(data)

print("Unsorted List",alist)
alist = mergesort(alist)      
print("Sorted List",alist)