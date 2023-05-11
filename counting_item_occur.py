from collections import Counter

list1 = ['John', 'kelly', 'Peter', 'Moses', 'Moses', 'Moses', 'John']


count_moses = Counter(list1).get("Moses")

print(f'the name moses appers in the list {count_moses} times')

count = 0
for p in list1:
    if p == 'John':
        count += 1
print(count)
