def changeValue(b):
    print("Value of b ",b)
    b[0] = 500
    b[1] = 700
    print("New Value of b ",b)

a=[10,20,30]
print("Value of a before passing ",a)
changeValue(a)
print("Value of a after passing ",a)
