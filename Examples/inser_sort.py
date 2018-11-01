unsorted = [4,1,3,6,5,1,2]
sorted = []
print(unsorted)
for i in range(len(unsorted)):
    mini = min(unsorted)
    sorted.append(mini)
    unsorted.remove(mini)
print(sorted)