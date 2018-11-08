def mer_sort(list):
    if (len(list)<2):
        return list
    else:
        mid_val = len(list)//2
        x = mer_sort[:mid_val]
        y = mer_sort[mid_val:]
    out = []
    i = 0
    j = 0
    while (i<len(x) and j<len(y)):
        if(x[i]>y[j]):
            out.append(y[j])
            j+=1
        else:
            out.append(x[i])
            i+=1
    out += x[i:]
    out += y[j:]
    return out

l = [7, 4, 3, 2, 1, 5]
print(mer_sort(l))
