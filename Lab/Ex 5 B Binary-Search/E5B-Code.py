print("Binary Search")
print("-------------")
alist = []
print ("enter any 5 numbers")
for i in range(5):
    data = int(input())
    alist.append(data)

key = int(input("Enter any number to search"))
found = False

start = 0
end = len(alist)-1

while(start<=end and not found):
    mid = (start+end)//2
    if (key == alist[mid]):
        found = True
    else:
        if (key < alist[mid]):
            end = mid-1
        else:
            start = mid+1
if(found):
    print("Element Found")
else:
    print("Element not Found")