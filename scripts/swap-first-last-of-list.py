mylist=[42,13,6,27,44,7,22]
print("Initial list:",mylist)

# Approach-1 : temporary variable
# temp=mylist[0]
# mylist[0]=mylist[-1]
# mylist[-1]=temp 
# print("Swapped list:",mylist)

# Approach-2
# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print("Swapped list:",mylist)

# Approach-3 : tuple variable
# mytuple=(mylist[-1],mylist[0])      # called packing
# mylist[0],mylist[-1]=mytuple        # unpacking
# print("Swapped list:",mylist)

# Approach-4 : * operand
# start,*middle,end=mylist
# print(middle)
# mylist=[end,*middle,start]
# print("Swapped list:",mylist)

# Approach-5 : Using pop built-in function
first=mylist.pop(0)
last=mylist.pop(-1)
mylist.insert(0,last)
mylist.append(first)
print("Swapped list:",mylist)
