
nested_list = [[2,4,6],[8,10,12]]

new_list = sum(nested_list, [])

print(new_list)

from functools import reduce

nested_list2 = [[3,5,7],[9,11,13]]

new_list2 = reduce(lambda x, y: x+y, nested_list2)

print(new_list2)