# 5! = 1*2*3*4*5=120

def factorial(n):
    # if(n==0 or num==1):
    #     return 1
    # else:
    #     return n*factorial(n-1)
    
    # Ternary operator
    return 1 if(n==0 or num==1) else n*factorial(n-1)

num=10
# Approach 1
fact=1

if  num>=1:
    for i in range(1,num+1):
        fact=fact*i
else:
    print('Factorial doesnt exists for numbers less than 1')

print(f'Factorial of number: {num} is {fact}')

# Approach 2: Recursive 
print("Recursive method calculation:",factorial(num))
