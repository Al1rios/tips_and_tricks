
dict1 = {'Grade':70, 'Weight':45, 'width':89}

# dict2 = {k: float(v) for (k, v) in dict1.items()}

dict2 = {k: v/2 for (k, v) in dict1.items()}

print(dict2)