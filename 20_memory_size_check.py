
import sys

a = ['love', 'cold', 'hot', 'python']
b = {'love', 'cold', 'hot', 'python'}
c = ('love', 'cold', 'hot', 'python')


print(f'the memory size of a {type(a)} is {sys.getsizeof(a)}')

print(f'the memory size of a {type(b)} is {sys.getsizeof(b)}')

print(f'the memory size of a {type(c)} is {sys.getsizeof(c)}')