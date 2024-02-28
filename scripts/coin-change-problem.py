# Given an amount and the denominations of coins available, determine how many ways change can be made for amount. There is a limitless supply of each coin type.

# Example


# There are  ways to make change for : , , and .

# Function Description

# Complete the getWays function in the editor below.

# getWays has the following parameter(s):

# int n: the amount to make change for
# int c[m]: the available coin denominations
# Returns

# int: the number of ways to make change
# Input Format

# The first line contains two space-separated integers  and , where:
#  is the amount to change
#  is the number of coin types
# The second line contains  space-separated integers that describe the values of each coin type.

# Constraints

# Each  is guaranteed to be distinct.
# Hints

# Solve overlapping subproblems using Dynamic Programming (DP):
# You can solve this problem recursively but will not pass all the test cases without optimizing to eliminate the overlapping subproblems. Think of a way to store and reference previously computed solutions to avoid solving the same subproblem multiple times. * Consider the degenerate cases:
# - How many ways can you make change for  cents? - How many ways can you make change for  cents if you have no coins? * If you're having trouble defining your solutions store, then think about it in terms of the base case . - The answer may be larger than a -bit integer.

# Sample Input 0

# 4 3
# 1 2 3
# Sample Output 0

# 4


amount=8         #int(input())
coins=[1,2,3,5]

def findCombinations(amt, coins):
    combinations=[0]*(amt+1)
    #print(len(combinations))
    combinations[0]=1
    for coin in coins:
        print("---------------")
        for i in range(coin,amt+1):
            combinations[i]+=combinations[i-coin]
            print(combinations[i])

    #print(combs[amt])
    return combinations[amt]

print(f"Final combinations: {findCombinations(amount,coins)}")