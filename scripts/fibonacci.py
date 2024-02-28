# 0 1 1 2 3 5 8 13 21 34

n1=0
n2=1
fib=12
#print(f'{n1}')
#print(f'{n2}')
arr=[0]
for i in range(2,fib+1):
    sum=n1+n2
    #print(f'{sum}')
    arr.append(sum)
    n1,n2=n2,sum


print(arr[len(arr)-1])

# Approach-2

def fib(n):
    if n <= 1:
       return n
    else:
        return fib(n-1)+fib(n-2)

# Approach-3
def fibo(n):
    return n if n<=1 else fibo(n-1)+fibo(n-2)

print("-------")
arr = [10,8,12,7]
for i in range(0,len(arr)):
    #print(fib(arr[i]))
    print(fibo(arr[i]))

