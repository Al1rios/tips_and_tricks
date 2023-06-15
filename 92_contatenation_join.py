import time


a = 'hello'
b = 'python'
c = 'world'
d = 'People'

start = time.perf_counter()

for _ in range(10000):
    f = a + b + c + d
end = time.perf_counter()

print(f'concatenation time is {end- start:.5f}')

a2 = 'hello'
b2 = 'python'
c2 = 'world'
d2 = 'People'

start = time.perf_counter()

for _ in range(10000):
    f2 = ''.join([a2,b2,c2,d2])

end = time.perf_counter()

print(f'concatenation time is {end- start:.5f}')

