### Most frequent operations

## There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

## Reverse a list of numbers
# Method 1
from collections import deque
import heapq

arr=[3,67,25,46,7,2,7,373]
print(arr)
arr.reverse()
print(arr)

# Method 2
arr=[3,67,25,46,7,2,7,373]
print(arr)
print(arr[::-1])

# Method 3
arr=[3,67,25,46,7,2,7,373]
print(arr)
print(list(reversed(arr)))

## Reverse a string
str="Hello World"
print(str)
print(str[::-1])

## Sorting a list
arr=[3,67,25,46,7,2,7,373]
print(arr)
arr.sort()              # Ascending
print(arr)
arr.sort(reverse=True)  # Descending
print(arr)
print(max(arr))
print(min(arr))

arr1=[45,"hi",3,"world"]
print(arr1)

## Traverse a list of strings
fruits=["mango","banana","blueberry","grape","apple","pear","strawberry"]
for i in fruits:
    print(i)
for i in range(len(fruits)):
    print(i,fruits[i])
for i in range(len(fruits)-1,-1,-1):
    print("Reverse of fruit",fruits[i])

print(fruits[::-1])
fruits.reverse()
print(fruits)
print(sorted(fruits,key=len))
print(fruits)
fruits.sort(key=lambda x:len(x))
print(fruits)

arr=[3,67,25,46,7,2,7,373]
print(arr)
arr.append(64)
arr.append(53)
arr.append(86)
print(arr)
print(arr.pop())
print(arr)
arr.insert(3,77)
print(arr)

## Initializing an array
n=5
arr=n*[1]
print(arr[-1])

## Enumerate
arr=[3,67,25,46,7,2,7,373]
print(arr)
for i,n in enumerate(arr):
    print(i,n)

## Loop through multiple array and unpack
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1,n2 in zip(nums1,nums2):
    print(n1,n2)

## List comprehension
arr = [i for i in range(0,10,2)]
print(arr)
arr = [i+i for i in range(0,10,2)]
print(arr)

## 2-D lists
arr = [[i]*5 for i in range(1,6,1)]
print(arr)
arr = [[i,i+1,i+2,i+3,i+4] for i in range(1,26,5)]
print(arr)
arr = [ j for j in range(1,6,1)]
print(arr)
arr = [[ j+i for j in range(0,5,1)] for i in range(1,26,5)]
print(arr)

## Conversions
s1="123"
print(int(s1))
s2="123"
print(int(s1)+int(s2))
print(s1+s2)

## ASCII value of a char
print(ord("d"))
print(ord("H"))

## Combine lists of strings
sarr = ["aaa","bbb","ccc"]
print("".join(sarr))

## Queues
queue = deque()     # Double ended queue
queue.append(1)
queue.append(2)
print(queue)

## HashSet
s = set()
s.add(1)
s.add(2)
s.add(1)
print(s)
print(1 in s)   # Check if specified number exists in the set
print(5 in s) 
s.remove(2)
print(s)

myset = set([1,2,3,4])      ## Initialize
print(myset)
# set comprehension
mset = {i for i in range(5)}
print(mset)

## Hash maps
mymap = {}      # initialize empty map
mymap["bob"]=123
mymap["Sita"]="Ram"
print(mymap)
print(len(mymap))
print(mymap.pop("bob"))
print(mymap["Sita"])
# Dictionary/hashmap comprehension
hm = {i:i*2 for i in range(5)}
print(hm)
# looping
for key in hm:
    print(key,hm[key])
for val in hm.values():
    print(val)
for k,v in hm.items():
    print(k,v)

## Tuples: A tuple is a collection which is ordered and unchangeable.
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
# Since tuple can't be changed, we can convert tuple into list and then add/append element and convert back to tuple
l=list(tuple1)
print(l)
l.append("python")
tup1=tuple(l)
print(tup1)

## Heaps
# import heapq
myheap = []
# heapq.heappush(myheap,"jack")
# heapq.heappush(myheap,"jim")
heapq.heappush(myheap,53)
heapq.heappush(myheap,64)
heapq.heappush(myheap,3)
heapq.heappush(myheap,8)
print(myheap)                   # print elements from smallest to biggest by default
print(heapq.heappop(myheap))    # pop's the minimum element by default
print(myheap[len(myheap)-1]) 
# converting array or defined values to a heap
arr=[45,6,257,2,67,5]
heapq.heapify(arr)
print(arr)      # Print sorted array

## Functions
def myfunc(m,n):
    return m*n
print(myfunc(5,3))
# Nested functions
def outer(a,b):
    c="c"
    def inner():
        return a+b+c
    return inner()
print(outer("a","b"))
# Modify objects using non-local
def double(arr, val):
    def helper():
        # modify only array elements
        for i,n in enumerate(arr):
            arr[i]=n*2
        #modifying val will modify only scope of the double function
        #val *= 2
        
        # Declare it as nonlocal will modify the scope of the val
        nonlocal val
        val *= 2
    helper()
    print(arr,val)

nums=[1,2,3]
val=4
double(nums,val)

## Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x= lambda a: a+10
print(x(10))

x= lambda a,b : a*b
print(x(10,5))

## Class
class Myclass:
    # constructor
    def __init__(self,nums):
        self.nums = nums
        self.size = len(nums)
    def getLength(self):
        return self.size
    def doubleLength(self):
        return self.size*2

nums=[2,4,6]
c=Myclass(nums)
print(c.doubleLength())

