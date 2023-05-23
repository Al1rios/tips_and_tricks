
str1 = 'string'

for index, value in enumerate(str1):
    if value == 'i':
        print(f'the index of n is {index}')


for i, j in enumerate(str1):
    print(f'index: {i}, valeu: {j}')

str_count = list(enumerate(str1))
print(str_count)