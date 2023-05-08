

# Method 1 python > 3.9

# name1 =  {
#     "kelly": 23,
#     "Ali": 50,
#     "Derick": 14,
# }

# name2 = {
#     "Ravi": 45,
#     "Mpho": 67,
#     "John": 7,
#     #"Derick": 14
# }

# names = name1 | name2

# print(names)

# Other option 

# name1 =  {
#     "kelly": 23,
#     "Ali": 50,
#     "Derick": 19
# }

# name2 = {
#     "Ravi": 45,
#     "Mpho": 67,
#     "John": 7,
#     "Derick": 14,
#     "Ali": 40
# }

# name1.update(name2)

# print(name1)


# method 3

name1 =  {
    "kelly": 23,
    "Ali": 30,
    "Derick": 19
}

name2 = {
    "Ravi": 45,
    "Mpho": 67,
    "John": 7,
    "Derick": 14,
    "Ali": 40
}

names = {**name1, **name2}
print(names)