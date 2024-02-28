# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def diagonalDifference(arr):
    leftd = rightd = 0
    n = len(arr)
    for i in range(n):
        leftd += arr[i][i]
        rightd += arr[i][n-1-i]
    return abs(leftd-rightd)


arr = [[11,2,4],[4,5,6],[10,8,-12]]
print(diagonalDifference(arr))