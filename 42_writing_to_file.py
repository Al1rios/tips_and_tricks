
names = ['John Kelly', 'Moses Nkosi', 'Joseph Marley', 'Ali Rios']

with open('names.csv', 'w') as file:
    for name in names:
        file.write(name)
        file.write('\n')


with open('names.csv', 'r') as file:
    print(file.read())