
a = 'fecklessness'

most_frequent = max(a, key=(a.count))

print(f'the most frequent letter is, {most_frequent}')


import collections

print(collections.Counter(a).most_common(2))
