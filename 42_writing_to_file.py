
names = ['John Kelly', 'Moses Nkosi', 'Joseph Marley', 'Ali Rios']

with open('names.csv', 'w') as file:
    for name in names:
        file.write(name)
        file.write('\n')


with open('names.csv', 'r') as file:
    print(file.read())


import csv

names = ['Ali Rios', 'John wick', 'Moses reacher', 'Bob Marley']

with open('names.csv', 'w') as file:
    for name in names:
        writer = csv.writer(file, lineterminator= '\n')
        writer.writerow([name])



with open('names.csv', 'r') as file:
    print(file.read())



