aList = [10,23,34,67,89,90,93]
key = 93
def bin_searcher(aList, key):
    mid_i = len(aList)//2
    if mid_i is not 0:
        if(aList[mid_i]==key):
            return (aList[mid_i])
        else:
            if(key<aList[mid_i]):
                return bin_searcher(aList[:mid_i],key)
            else:
                return bin_searcher(aList[mid_i:],key)
    else:
        return False
        
print(bin_searcher(aList,key))