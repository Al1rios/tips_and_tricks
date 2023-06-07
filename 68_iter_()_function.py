
names = ['jake', 'mpho','peter']

iter_object = iter(names)

# name1 = next(iter_object)

# print(f'First name is {name1}')

# name2 = next(iter_object)

# print(f'First name is {name2}')


while True:
    try:
        print(next(iter_object))
    except:
        break