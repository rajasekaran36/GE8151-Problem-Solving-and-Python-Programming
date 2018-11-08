def inser_sort(l):
    for i in range(len(l)):
        pivot = i
        while(pivot>0 and l[pivot]<l[pivot-1]):
            (l[pivot],l[pivot-1]) = (l[pivot-1],l[pivot])
            pivot = pivot - 1
l = [7,4,3,2,1,5]

print(l)
inser_sort(l)
print(l)