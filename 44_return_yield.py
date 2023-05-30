
def num(n: int) -> int:
    for i in range(n):
        return i

print(num(10))

def num(n: int) -> int:
    for i in range(n):
        yield i

gen = num(15)

for i in gen:
    print(i, end=" ")

