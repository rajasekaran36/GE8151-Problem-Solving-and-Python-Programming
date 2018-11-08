def sel_sort(l):
    for i in range(len(l)-1):
        mini = i
        for j in range(i+1,len(l)):
            if(l[mini]>l[j]):
                mini = j
        if (mini!=i):
            (l[i],l[mini])=(l[mini],l[i])

l = [7, 4, 3, 2, 1, 5]
sel_sort(l)
print(l)