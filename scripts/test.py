print("Hello Python programming")
'''
arr=[12,5,453,2,13,257,8,3]
#arr=[12, 3, 5, 2, 8, 13, 257, 453]
#arr=[2, 3, 5, 8, 12, 13, 257, 453]
print(arr)
count=0
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
swapped=False
count=0
n=len(arr)
# Selection sort
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         count=count+1
#         #print(j-1,j)
#         if arr[i] > arr[j]:
#             swap(arr,i,j)
#             swapped=True
#     if not swapped:
#         break
# print(count)

# Bubble sort
# for i in range(n-1):
#     for j in range(n-i-1):
#         count=count+1
#         # print(j,j+1)
#         if arr[j] > arr[j+1]:
#             swap(arr,j,j+1)
#             swapped=True
#     if not swapped:
#         break

# Insertion sort
for i in range(1,n):
    j=i-1
    key= arr[i]
    print(key,arr[j])
    while(j>=0 and key<arr[j]):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print(count)
print(arr)
'''

