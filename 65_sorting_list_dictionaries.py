

from operator import itemgetter

d = [{'school':'yale', 'city':'Beijing'}, {'school':'cat', 'city':'Cairo'}]

# sorted_list = sorted(d, key=itemgetter('school'))


sorted_list = sorted(d, key=itemgetter('school'), reverse=True)
print(sorted_list)

