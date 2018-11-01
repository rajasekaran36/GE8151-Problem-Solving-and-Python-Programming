p_list = [1,2,4,2,3,5,4]

for ele in p_list:
    while(p_list.count(ele)!=1):
        p_list.remove(ele)
        #p_list.sort()

print(p_list)