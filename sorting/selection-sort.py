# Working of Selection Sort
#   - Set the first element as minimum.
#   - Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.
#   - Compare minimum with the third element. Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing. The process goes on until the last element.
#   - After each iteration, minimum is placed in the front of the unsorted list.
#   - For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions.

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            # to sort in descending order, change < to > in this line
            # select the minimum element in each loop
            if arr[j] < arr[min]:
                min = j
        # put min at the correct position
        arr[i],arr[min] = arr[min],arr[i]
                

if __name__ == "__main__":
    arr = [41,9,3,25,28,39,19,47,4,50,21,8]
    selection_sort(arr)
    print("Sorted array is:")
    print(arr)

## Selection Sort Complexity
# ---------------------------
# Time Complexity	 
# Best	O(n2)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	No

# Also, we can analyze the complexity by simply observing the number of loops. There are 2 loops so the complexity is n*n = n2.

## References:
# - https://www.youtube.com/watch?v=g-PGLbMth_g
# - https://www.programiz.com/dsa/selection-sort