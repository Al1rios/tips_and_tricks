
import timeit
import sys

def timer(_, code):
    exc_time = timeit.timeit(code, number=1000)
    return f'{_}: execution time is {exc_time:.2f}'

def memory_size(_, code):
    size = sys.getsizeof(code)
    return f'{_}: allocated memory is {size}'

one = 'Generator'
two = 'list comprenhension'

print(timer(one, 'sum((num**2 for num in range(10000)))'))
print(timer(two, 'sum([num**2 for num in range(10000)])'))

print(memory_size(one, (num**2 for num in range(10000))))
print(memory_size(two, [num**2 for num in range(10000)]))