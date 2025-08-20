import random
import numpy as np
list1, list2, list3, list4, list5 = [], [], [], [], []

for _ in range(5):
    list1.append(random.randint(1, 100))
    list2.append(random.randint(1, 100))
    list3.append(random.randint(1, 100))
    list4.append(random.randint(1, 100))
    list5.append(random.randint(1, 100))

array1 = np.array(list1)
array2 = np.array(list2)
array3 = np.array(list3)
array4 = np.array(list4)
array5 = np.array(list5)

arrays = np.array([array1,array2,array3,array4,array5])
print(arrays)
for array in arrays:
    print(type(array))
    

