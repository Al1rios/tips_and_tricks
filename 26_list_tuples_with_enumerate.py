
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# days_tuples = list(enumerate(days, start=1))

days_tuples = [enumerate(day, start=1) for day in days]

print(days_tuples)


# def enumerate(days, start=1):
#     n = start
#     for day in days:
#         yield n, day
#         n += 1

# print(list(enumerate(days)))