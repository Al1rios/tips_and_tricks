
import more_itertools

nested_list = [[12,14,34,56],[23,56,78]]

print(list(more_itertools.collapse(nested_list)))


list_tuples = [(12,14,34,56),(23,56,78),(12,23,56)]

print(list(more_itertools.collapse(list_tuples)))