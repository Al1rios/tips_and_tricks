
def number_factors(n: int):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

print(number_factors(8))


n = int(input('Please enter number: '))

factors = [i for i in range(1, n+1) if n % i == 0]

print(factors)