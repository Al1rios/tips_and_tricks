
def check_list(arr: list):
    return all(arr[0] == arr[i] for i in arr)

print(check_list([2,2,2,2]))
print(check_list([2,2,2,3]))