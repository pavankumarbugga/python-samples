mylist=[42,13,6,27,44,7,22]
print("Initial list:",mylist)
pos1,pos2=1,3

# Approach-1 : simple swap
# mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
# print("Swapped list:",mylist)

# Approach-2 : Using pop built-in function
first=mylist.pop(pos1)
second=mylist.pop(pos2-1)
print(first,second)
mylist.insert(pos1,second)
mylist.insert(pos2,first)
print("Swapped list:",mylist)