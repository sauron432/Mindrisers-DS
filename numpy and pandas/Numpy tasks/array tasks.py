import numpy as np
array2d = np.arange(18).reshape(3,6)
array3d = np.arange(18).reshape(3,3,2)
print("2-d array:\n",array2d)
print("3-d array:\n",array3d)
print("\nNow we will change 2-d into 3-d and 3-d into 2-d.\n")
print("2-d to 3-d array:\n",array2d.reshape(3,3,2))
print("3-d to 2-d array:\n",array3d.reshape(3,6))
