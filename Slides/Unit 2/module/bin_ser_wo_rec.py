aList = [10,23,34,67,89,90,93]
key = 90
found = False
found_i = -1
start_i = 0
end_i = len(aList)-1

while(start_i<=end_i):
    mid_i = int((start_i+end_i)/2)
    if(aList[mid_i]==key):
        found = True
        found_i = mid_i
        break;
    else:
        if(key<aList[mid_i]):
            end_i=mid_i-1
        else:
            start_i = mid_i+1
        
if(found):
    print("Element found at",found_i)
else:
    print("Element not found")