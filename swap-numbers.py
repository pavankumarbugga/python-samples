num1=10
num2=20

print(f'Values before swap num1={num1}, num2={num2}')

# Method1
temp=num1
num1=num2
num2=temp

print(f'Values after swap num1={num1}, num2={num2}')

# Method2
number1=input('Enter number 1:')
number2=input('Enter number 2:')
print(f'Values before swap num1={number1}, num2={number2}')
number1,number2=number2,number1
print(f'Values after swap num1={number1}, num2={number2}')
