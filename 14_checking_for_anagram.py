
from collections import Counter

a = 'lost'
b = 'stol'

print(Counter(a)==Counter(b))


a1 = 'lost'
b1 = 'stol'

if sorted(a1)==sorted(b1):
    print(sorted(a1), sorted(b1))
    print("it's anagrams")
else:
    print('not anagrams')