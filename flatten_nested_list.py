
list1 = [[1,2,3],[4,5,6]]

# new_list = []

# for list2 in list1:
#     for j in list2:
#         new_list.append(j)

# Using Itertools
import itertools

# flat_list = list(itertools.chain.from_iterable(list1))

flat_list = [j for list2 in list1 for j in list2]

print(flat_list)