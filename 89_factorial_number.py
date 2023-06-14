
def factorial_number(n: int):
    f = 1
    if n < 0:
        return 'negatives numbers have no factorial'
    else:
        for k in range(1, n+1):
            f = f * k
        return f'the factorial of number {n} is {f}'
    
print(factorial_number(8))