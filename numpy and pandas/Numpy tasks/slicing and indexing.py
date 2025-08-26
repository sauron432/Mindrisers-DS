import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
#1
print(arr[::3])
#2
print(arr[-4:])
#3
arr [arr% 2 == 0]  = -1
print(arr)
#4
print(arr[[2,3,6,8]])