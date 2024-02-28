## Merge Sort Algorithm
# Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
# Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

## Divide and Conquer Strategy
# Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, we 'combine' the results from the subproblems to solve the main problem.
# Suppose we had to sort an array A. A subproblem would be to sort a sub-section of this array starting at index p and ending at index r, denoted as A[p..r].

# Divide
    # If q is the half-way point between p and r, then we can split the subarray A[p..r] into two arrays A[p..q] and A[q+1, r].

# Conquer
    # In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.

# Combine
    # When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r], we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].

def merge_sort(arr):
    if len(arr) > 1:

        lef_arr = arr[:len(arr)//2]
        rht_arr = arr[len(arr)//2:]

        # recurssion
        merge_sort(lef_arr)
        merge_sort(rht_arr)

        # Merge
        i = 0   # left array index
        j = 0   # right array index
        k = 0   # merged array index
        # i = j = k = 0     # Above statements can be replaces in one statement

        # Until we reach either end of either Left or Right, pick larger among
        # elements Left and Right arrays and place them in the correct position at origin array - arr
        while i < len(lef_arr) and j < len(rht_arr):
            if lef_arr[i] < rht_arr[j]:
                arr[k] = lef_arr[i]
                i += 1
            else:
                arr[k] = rht_arr[j]
                j += 1
            k += 1
        # When we run out of elements in Left array,
        # pick up the remaining elements and put into array - arr
        while i < len(lef_arr):
            arr[k] = lef_arr[i]
            i += 1
            k += 1
        # When we run out of elements in Right array,
        # pick up the remaining elements and put into array - arr
        while j < len(rht_arr):
            arr[k] = rht_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [41,9,3,25,28,39,19,47,4,50,21,8]
    merge_sort(arr)
    print("Sorted array is:")
    print(arr)


## Merge Sort Complexity
    # Time Complexity	 
    # Best	O(n*log n)
    # Worst	O(n*log n)
    # Average	O(n*log n)
    # Space Complexity	O(n)
    # Stability	Yes
## Time Complexity
    # Best Case Complexity: O(n*log n)
    # Worst Case Complexity: O(n*log n)
    # Average Case Complexity: O(n*log n)

## Space Complexity
    # The space complexity of merge sort is O(n).

## References:
# https://www.youtube.com/watch?v=cVZMah9kEjI
# https://www.programiz.com/dsa/merge-sort