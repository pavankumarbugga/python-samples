mylist=[42,13,6,27,44,7,22]
print("Initial list:",mylist)

ele=27

# Approach 1
flag=0
for i in mylist:
    if i==ele:
        print("Element found")
        flag=1
        break

if(flag==0):
    print("Element not found")

# Approach 2
if(ele in mylist):
    print("Element found")
else:
    print("Element not found")

