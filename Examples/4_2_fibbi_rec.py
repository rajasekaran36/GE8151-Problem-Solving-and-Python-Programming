def fibi(n):
    if(n<=1):
        return n
    else:
        return fibi(n-1)+fibi(n-2)
for i in range(5):
    print(fibi(i))