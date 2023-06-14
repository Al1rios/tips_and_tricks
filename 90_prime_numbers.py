
def prime_numbers() -> list:

    prime_num = []

    n = int(input('Please enter a number (integer): '))

    for i in range(0, n+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_num.append(i)
    return prime_num

print(prime_numbers())


# if __name__ == '__main__':
#     prime_numbers()
                
