# It's a natural number > 1
# It should have only 2 factors : 1 and itself
#
# 19: It's a prime
# 22: It's not a prime
# 

num=25
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print('Number is Prime')
    else:
        print('Number is not Prime')
