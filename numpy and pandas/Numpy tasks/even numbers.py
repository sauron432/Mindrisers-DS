import numpy as np 
# numbers = [i for i in range(1,100)]
num = np.arange(0,11)
print(num % 2 == 0)
print("Even Numbers:", num[num%2 == 0])