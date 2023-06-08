
from itertools import permutations

def get_permutations(s:str):
    arr = []
    for i in permutations(s):
        arr.append(''.join(i))
    return arr

print(get_permutations('ABC'))


def find_permute(string, j):
    if len(string) == 0:
        print(j, end=" ")
    
    for i in range(len(string)):
        char = string[i]
        s = string[0:i] + string[i + 1:]
        find_permute(s, j + char)
    return j

print(find_permute('ABC', ''))
