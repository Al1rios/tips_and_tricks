
def avg(*args):
    avg1 = sum(args)/len(args)
    return f'the average is {avg1:.2f}'

print(avg(12,34,56))
print(avg(23,45,36,41,25,25))

def myfunc(**kwargs):
    for key, valeu in kwargs.items():
        print(f'{key}: {valeu}')
    print('\n')

myfunc(Name = 'Bem', Age = 80, Occupation = 'Engineer')