var1 = 200
def myfunction():
    var1 = 50
    print("In function block")
    print ("var1 value",var1)

print("In main block")
print("var1 value before calling",var1)
myfunction()
print("In main block")
print("var1 value after calling",var1)
