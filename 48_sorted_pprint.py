
import pprint

a = {'c': 2, 'b': 3, 'y':5, 'x':10}

pp = pprint.PrettyPrinter(sort_dicts=True)

pp.pprint(a)

arr = [1034567, 1234567, 1246789, 12345679, 987654367]

pp = pprint.PrettyPrinter(underscore_numbers=True)

pp.pprint(arr)