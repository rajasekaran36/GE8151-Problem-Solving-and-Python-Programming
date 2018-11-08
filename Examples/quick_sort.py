def quick_sort(list):
    a = []
    b = []
    c = []
    if (len(list) > 1):
        pivot = list[0]
        for element in list:
            if(element<pivot):
                a.append(element)
            elif(element == pivot):
                b.append(element)
            else:
                c.append(element)
        
        return quick_sort(a) + b + quick_sort(c)
    else:
        return list

print(quick_sort([3,12,1,4,2]))