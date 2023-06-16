
from functools import reduce

num = 10

f = reduce(lambda a, b: a * b, range(1, num+1))

print(f)