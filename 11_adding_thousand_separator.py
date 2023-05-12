
a = [10989767, 9876780, 9908763]


new_list = ['{:,}'.format(num) for num in a]

new_list12 = [f'{num:_}' for num in a]

print(new_list)
print(new_list12)
