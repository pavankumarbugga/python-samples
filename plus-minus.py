# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def plusMinus(arr):
    
    plus = minus = zero = 0
    n = len(arr)
    
    for i in arr:
        if(i > 0):
            plus += 1
        elif(i < 0):
            minus += 1
        else:
            zero += 1
    print("{0:.6f}".format(plus/n))     # Prints formated to 6 decimal o/p
    print("{0:.6f}".format(minus/n))
    print("{0:.6f}".format(zero/n))
    #print(plus/n)  # Prints decimal o/p with "/"
    #print(minus/n)
    #print(zero/n)  

    #print(plus//n) # Prints non-decimal o/p with "//"

arr = [3,-2,-9,8,0,5]
plusMinus(arr)