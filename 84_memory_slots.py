
import sys

class Cars:
    def __init__(self, make, brand):
        self.make = make
        self.brand = brand

print(f'the memory size is {sys.getsizeof(Cars)}')


class Cars:
    __slots__ = ['make', 'brand']

    def __init__(self, make, brand):
        self.make
        self.brand

print(f'the memory is {sys.getsizeof(Cars)}')