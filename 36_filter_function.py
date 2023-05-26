
names = ['Derick', 'John', 'moses', 'linda']
lower_case = []

for name in names:
    if name.islower():
        lower_case.append(name)
print(lower_case)


# lower_case2 = list(filter(lambda x:x.islower(), names))
# print(lower_case2)

lower_case3 = [ x for x in names if x.islower()]
print(lower_case3)


def lower_names(n:str):
    return n.islower()

lower_case4 = list(filter(lower_names, names))
print(lower_case4)