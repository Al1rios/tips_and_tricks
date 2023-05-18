
list1 = ['Mary', 'Peter', 'Kelly']

a = lambda x: x[-1]

y = sorted(list1, key=a)

# a = lambda x: x[:1]

# y = sorted(list1, key=a)

# list2 = sorted(list1)

print(y)

