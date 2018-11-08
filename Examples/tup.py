x=(23,)
print(x)
print(type(x))
x = (44,)
print(x)
print(type(x))

x1 = (10,11)
x2 = (100,111)
print("x1:",x1,"id:",id(x1))
print("x1:",x2,"id:",id(x2))
z = x1 + x2
print("z:",z,"id:",id(z))
print(z*4)