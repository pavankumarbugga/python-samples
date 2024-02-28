## Insertion Sort Algorithm
# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
# Insertion sort works similarly as we sort cards in our hand in a card game.
# We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put in their right place.
# A similar approach is used by insertion sort.

def insertion_sort(arr):
    n =len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j]. 
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # Place key at after the element just smaller than it.
        arr[j+1] = key

if __name__ == "__main__":
    arr = [41,9,3,25,28,39,19,47,4,50,21,8]
    insertion_sort(arr)
    print("Sorted array is:")
    print(arr)


## Insertion Sort Complexity
    # Time Complexity	 
    # Best	O(n)
    # Worst	O(n2)
    # Average	O(n2)
    # Space Complexity	O(1)
    # Stability	Yes

## Time Complexities

# Worst Case Complexity: O(n2)
    # Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worst case complexity occurs.
    # Each element has to be compared with each of the other elements so, for every nth element, (n-1) number of comparisons are made.
    # Thus, the total number of comparisons = n*(n-1) ~ n2
# Best Case Complexity: O(n)
    # When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.
# Average Case Complexity: O(n2)
    # It occurs when the elements of an array are in jumbled order (neither ascending nor descending).

## Space Complexity
    # Space complexity is O(1) because an extra variable key is used.

## References:
# https://www.programiz.com/dsa/insertion-sort
# https://www.youtube.com/watch?v=8mJ-OhcfpYg
