
list1 = ['LOVE', 'HATE', 'WAR', 'PEACE', 'PEACE']

set1 = {word.lower() for word in list1}

print(set1)

arr = [10, 23, 30, 30, 40, 45, 50]

new_set = {num for num in arr if num % 2 == 0}

print(new_set)