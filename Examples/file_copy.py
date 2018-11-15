source = input("source")
dest = input("dest")

in_file = open(source,"r")
out_file = open(dest,"w")

data = in_file.read()
out_file.write(data)

in_file.close()
out_file.close()