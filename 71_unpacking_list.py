
names = ['John', 'Mary', 'Lisa', 'Rose']

boy_name, *girs_name = names
print(boy_name)
print(girs_name)

names2 = ['Rose', 'Mary','Lisa', 'John']

*girs_name, boy_name

print(girs_name)
print(boy_name)