
import time

def timer(func):
    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f'Run time is {end-start:.2f} secs')
    return inner

@timer
def range_tracker():
    lst = []
    for i in range(10_000_000):
        lst.append(i**2)

range_tracker()
