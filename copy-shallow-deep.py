import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)
original_list[0][0] = 99  # Modifying the original list
print(shallow_copied_list)  # Changes are reflected in the shallow copy
print(deep_copied_list)