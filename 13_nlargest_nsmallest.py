
def sort_list(arr: list):
    a = sorted(arr, reverse=True)
    return a[:5]

result = [12,34,67,98,90,68,55,54,64,35]

print(sort_list(result))

# library heapq

import heapq

result2 = [12,34,67,98,90,68,55,54,64,35]

print(heapq.nlargest(5, result2))

result3 = [12,34,67,98,90,68,55,54,64,35]

print(heapq.nsmallest(6, result3))