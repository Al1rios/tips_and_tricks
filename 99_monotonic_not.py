
def check_monotonic(arr: list):
    if all(arr[i] >= arr[i +1] for i in range(len(arr)-1)):
        return True
    elif all(arr[i] <= arr[i +1] for i in range(len(arr)-1)):
        return True
    else:
        return False
    
print(check_monotonic(list1:=[4,2,5,7]))
