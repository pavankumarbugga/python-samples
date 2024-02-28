# input: arr[] = {4,23,62,14,34,3}
# output: min=3, max=62

arr=[40,23,62,14,34,3]
#min,max=arr[0],arr[1]
#print(f'Min={min}, Max={max}')

maxi=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i] > maxi:
        maxi=arr[i]

mini=arr[0]
for i in range(1,n):
    if arr[i] < mini:
        mini=arr[i]

print(f'Min={mini}, Max={maxi}')
print(min(arr),max(arr))