no=0
def honai(n,source,dest,aux):
    if(n==1):
        movedisk(n,source,dest)
    else:
        honai(n-1,source,aux,dest)
        movedisk(n,source,dest)
        honai(n-1,aux,dest,source)

def movedisk(disk,source,dest):
    global no
    print("move",disk,"disk",source,"to",dest)
    no=no+1

honai(10,"source","dest","aux")
print(no)