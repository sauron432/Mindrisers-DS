import numpy as np
new_array = np.empty(6)
print("Empty array",new_array)
for i in range(6):
    # new_array = np.append(new_array,i)
    new_array[i] = i
    
print("\nAfter running loop", new_array)