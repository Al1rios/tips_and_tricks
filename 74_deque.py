from collections import deque

arr = deque([1, 3])

arr.appendleft(5)
arr.append(7)

print(arr)

arr1 = deque([1,3,9,6])
arr1.popleft()
arr1.pop()

print(arr1)