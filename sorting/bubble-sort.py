# Working of Bubble Sort
# Suppose we are trying to sort the elements in ascending order.
# 1. First Iteration (Compare and Swap)
#     - Starting from the first index, compare the first and the second elements.
#     - If the first element is greater than the second element, they are swapped.
#     - Now, compare the second and the third elements. Swap them if they are not in order.
#     - The above process goes on until the last element
# 2. Remaining Iteration
#     - The same process goes on for the remaining iterations.
#     - After each iteration, the largest element among the unsorted elements is placed at the end.


def bubble_sort(arr):
    n = len(arr)
    # loop through each element of array
    for i in range(n-1):
        #print("i=",i)
        # loop to compare array elements
        for j in range(n-i-1):
            # compare two adjacent elements
            # change > to < to sort in descending order
            if arr[j] > arr[j+1]:
                #print(i,j)
                #print(arr)
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = [41,9,3,25,28,39,19,47,4,50,21,8]
    bubble_sort(arr)
    print("Sorted array is:")
    print(arr)


## Time complexity: O(n)2 as there are 2 for loops
## Space Complexity: O(1) as there is no extra space used in manipulation, existing array is used to swap

## Optimized Bubble Sort Algorithm:
# - In the above algorithm, all the comparisons are made even if the array is already sorted.This increases the execution time.
# - To solve this, we can introduce an extra variable swapped. The value of swapped is set true if there occurs swapping of elements. Otherwise, it is set false.
# - After an iteration, if there is no swapping, the value of swapped will be false. This means elements are already sorted and there is no need to perform further iterations.
# - This will reduce the execution time and helps to optimize the bubble sort.

# def bubble_sort(arr):
#     n = len(arr)
#     swapped = False
#     # loop through each element of array
#     for i in range(n-1):
#         # loop to compare array elements
#         for j in range(n-i-1):
#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if arr[j] > arr[j+1]:
#                 print(i,j)
#                 print(arr)
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True

#         # no swapping means the array is already sorted
#         # so no need for further comparison
#         if not swapped:
#             break

# if __name__ == "__main__":
#     arr = [3, 4, 8, 9, 19, 21, 25, 28, 39, 41, 47, 50]
#     bubble_sort(arr)
#     print("Sorted array is:")
#     print(arr)