# https://www.hackerrank.com/challenges/crush/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def arrayManipulation(n, queries):
    # initialize arrays
    arr = [0] * (n+2)
    print(arr)

    # perform the query operation
    for a,b,k in queries:
        arr = sum(arr,k)
        
        print(arr)
        maxnum = temp = 0
        # for val in arr:
        #     temp += val
        #     maxnum = max(maxnum, temp)

        # return maxnum
    

n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]
arrayManipulation(n,queries)