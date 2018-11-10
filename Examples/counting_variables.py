name = "Rajasekaran"
d = {}
for char in name:
    if (char in d):
        d[char]+=1
    else:
        d[char]=1

uni_string = ""
for key in d:
    if(d[key]==1):
        uni_string = uni_string + key        
print(uni_string)

d2 = {}