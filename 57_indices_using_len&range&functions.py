
names = ['John', 'Art', 'Maradona', 'Carl']

for i in range(len(names)):
    print(i, names[i])


for i in range(len(names)):
    if names[i] == 'Maradona':
        print(f'the index of the name {names[i]} is {i}')

