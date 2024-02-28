arr = [3,7,2,53]
revarr = []
print(arr)

# looping, range(start, stop, step) 
for i in range(len(arr)-1,-1,-1):
    revarr.append(arr[i])
print(revarr)   

# slicing, array[start:stop:step]
rev = arr[::-1]
print(rev)

# reverse method
arr.reverse()
print(arr)


