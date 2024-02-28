import random

orginal_list = [3,65,63,6,346,7]
print(orginal_list)
shuffled_list = random.sample(orginal_list,len(orginal_list))     # Get a new shuffled list without modifying the original list
print(orginal_list)
print(shuffled_list)
random.shuffle(orginal_list)    # Shuffles original list
print(orginal_list)