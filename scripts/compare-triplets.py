# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen&isFullScreen=false

def compareTriplets(a,b):
    alice = bob = 0
    for i in range(len(a)):
        if(a[i]>b[i]):
            alice += 1
        elif(a[i]<b[i]):
            bob += 1
    return alice,bob


a = [1, 2, 3]
b = [3, 2, 1]
result = compareTriplets(a,b)
print(result)