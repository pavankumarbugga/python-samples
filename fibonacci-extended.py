# This question expands on our earlier Fibonacci Lite challenge. While the goal of Fibonacci Lite was to understand recursion, this challenge is about solving problems efficiently with dynamic programming.
# The difference in this challenge is that each test case will consist of many inputs instead of just one. Furthermore, we're allowing larger values of n. You'll need to use dynamic programming to solve all the inputs without running out of time.
# So, given many numbers n, print the nth value of the Fibonacci sequence for each of them, in order, on their own line.
# Here are the definitions of the sequence again:

## input
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

## output
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55


# count=int(input())

# mylist=[]
# for i in range(0,count):
#     mylist.append(int(input()))

count = 5
#mylist = [ int(input()) for i in range(count)]
mylist = [2, 12, 7, 9, 3]

print(mylist)
max=0
for j in mylist:
    if(j>max):
        max=j
print(max)

e1=0
e2=1
arr=[e1,e2]
if(count==0):
    print(0)
else:
    for k in range(2,max):
        sumn=e1+e2
        arr.append(sumn)
        e1,e2=e2,sumn

print(arr)  

# Printing fibonacci sequence for each element in i/p array
for n in mylist:
    print(arr[0:n])