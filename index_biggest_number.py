import pdb

x = [12,45,67,89,347,67,13,5]

max_num = max(enumerate(x, start=0), key=lambda x: x[1])
#pdb.set_trace()

print('The index of the largest numbers is', max_num)


y = [12,45,67,89,34,67,13,2]

min_num = min(enumerate(y, start=0), key=lambda y: y[1])

print('the index of the smallest number is', min_num)

min_test = min(enumerate(y, start=0))

print(min_test)