
def sort_names(x):
    return x[0]

names = [('John', 'Kelly'), ('Chris', 'Rock'), ('will', 'Smith')]

# sorted_names = sorted(names, key=sort_names)

sorted_names = sorted(names, key=lambda x:x[0])

print(sorted_names)