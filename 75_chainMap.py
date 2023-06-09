
from collections import ChainMap

x = {'name':'ali', 'sex':'male'}
y = {'name': 'flor', 'sex': 'female'}

dict1 = ChainMap(x, y)

print(dict1)



print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))
