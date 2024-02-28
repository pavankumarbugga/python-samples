# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
    # Input: nums = [5,7,7,8,8,10], target = 8
    # Output: [3,4]
#     
# Example 2:
    # Input: nums = [5,7,7,8,8,10], target = 6
    # Output: [-1,-1]
#  
# Example 3:
    # Input: nums = [], target = 0
    # Output: [-1,-1]


def findTarget(arr,tar):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == tar:
            if first == -1:
                first = i
            else:
                last = i
    result = [first,last]
    print(result)

# Above method fails when array consists only one element and it's a match as
# Input: nums = [1], target = 1
# Expected is [0,0]
# Output: [0,-1]

def findElement(arr,tar):
    first = -1
    last = -1

    for i in range(len(arr)):
        # Skip the iteration when there is no match
        if arr[i] != tar:
            continue
        # Perform this step when there is a match ( i.e skipping when there is no match)
        # Check if first match is present or not and store the index
        if first == -1:
            first = i
        # Store last match always as there is scenario of being first & last being same in an array of single element with a match
        last = i
    result = [first,last]
    print(result)

if __name__ == "__main__":
    arr = [5,7,7,8,8,10]
    #arr = [5,7,7,8,8,10,8,4,3,8,7,0]
    # arr = [1]
    target = 8
    #findTarget(arr,target)
    findElement(arr,target)