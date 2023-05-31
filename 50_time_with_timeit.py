import timeit
def timer(code):
    tm = timeit.timeit(code,number=1000)
    return f'Execution time is {tm:.2f} secs.'

if __name__ == "__main__":
    print(timer('sum(num**2 for num in range(10000))'))