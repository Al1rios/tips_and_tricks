

arr = ['i', 'love','working','with','python']

try:
    iter_check = iter(arr)
except TypeError:
    print('Object a not iterable')
else:
    print('Object a is iterable')

b: float = 45.7

try:
    iter_float = iter(b)
except TypeError:
    print('object b is not iterable')
else:
    print('object b is iterable')
    