
a = [9,3,6,7,8,4]
b = [9,3,7,5,2,1]

diffence = set(a).difference(set(b))

print(list(diffence))

difference2 = []

for number in a:
    if number not in b:
        difference2.append(number)
print(diffence)

dif = [number for number in a if number not in b]
print(sorted(dif, reverse=True))
