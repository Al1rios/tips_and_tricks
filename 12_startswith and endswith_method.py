

list1 = ['lemon', 'Orange', 'apple', 'apricot']


new_list = [i for i in list1 if i.startswith('a')]

print(new_list)

new_list2 = [x for x in list1 if x.endswith('e')]

print(new_list2)