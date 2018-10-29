a_list = [1,4,5,6]
b_list = [100,300,250]
print(id(a_list),a_list)
print(id(b_list),b_list)
con_list = a_list + b_list
print(id(con_list),con_list)
con_list_2 = con_list*2 
print(id(con_list_2),con_list_2)
print(con_list[2:len(con_list):1])
