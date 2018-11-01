a_list = [3,4,5,6,2,1]
for i in range(0,len(a_list)-1):
    minimum = i;
    for j in range(i+1, len(a_list)):
        if(a_list[j] < a_list[minimum]):
           minimum = j
    if (minimum !=i):
                   a_list[i],a_list[minimum] = a_list[minimum],a_list[i]

print(a_list)