inp_file = open("file1.txt","r",encoding="utf8")

data = inp_file.read()

print(data)

data_dict = {}

for ele in data.split(" "):
    if ele in data_dict:
        data_dict[ele] += data_dict[ele]+1
    else:
        data_dict[ele] = 1

for key in data_dict:
    print("{} -- {}".format(key,data_dict[key]))
