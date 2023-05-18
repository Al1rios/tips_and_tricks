
from operator import itemgetter

names = [('Ben', 'Smith'), ('Peter', 'Parker'), ('Lady', 'Gaga')]
sorted_names = sorted(names, key=itemgetter(0))
print('sorted by first name', sorted_names)


sorted_names2 = sorted(names, key=itemgetter(1))
print('sorted by last name', sorted_names2)