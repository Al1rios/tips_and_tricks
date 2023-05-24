
import os.path

# os.remove("garbage.txt")

file = os.path.exists('gabage.txt')

if file:
    os.remove('gabage.txt')
else:
    print('this file does not exist')