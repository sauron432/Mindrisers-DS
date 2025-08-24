import numpy as np
import random
lst = [random.randint(1,10) for _ in range(5)]
print(lst)
arr = np.array(lst)
print(arr[::-1])
print(arr[-3])