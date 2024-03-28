def move_element_to_end(arr,ele):
    # Initialize a pointer to keep track of the position to swap with 0's
    pointer = 0

    # Iterate through the array
    for i in range(len(arr)):
        if arr[i] != ele:
            # If the current element is not 0, swap it with the element at the pointer
            # print(i,pointer)
            arr[i], arr[pointer] = arr[pointer], arr[i]
            # print(arr)
            pointer += 1

    # Fill the remaining positions with 0's
    # for i in range(pointer, len(arr)):
    #     arr[i] = 0

    # return arr

# Example usage:
arr = [1, 0, 1, 0, 1, 0, 0, 1]
element = 1
result = move_element_to_end(arr,element)
print(f"Array after moving {element}'s to the end: {arr}")
