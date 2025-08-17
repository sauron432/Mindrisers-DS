import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
              [1, 2, 3, 4, 5, 6, 78 ,9]])
c = np.array([[[1, 2, 3, 4, 5, 6, 7, 8,0],
               [1, 2, 3, 4, 5, 6, 8 ,9,0],
               [1, 2, 3, 54 ,65 ,6 ,5 ,810,0]]])
print("\nTHIS IS PART 1:\n")
print(a)
print(b)
print(c)
print()
print(a.size)
print(b.size)
print(c.size)
print()
print(a.shape)
print(b.shape)
print(c.shape)
print()
print(a.dtype)
print(b.dtype)
print(c.dtype)
print()
print(type(a))
print(type(b))
print(type(c))
print(b.transpose())

print("\nTHIS IS PART 2:\n")
print(np.empty((4,4),dtype=bool))
print(np.ones((4,5),dtype=int))
print(np.ones((4,5),dtype=str))
print(np.ones((4,5),dtype=bool))
print(np.zeros((4,5),dtype=bool))
print(np.zeros((4,5),dtype=str))

print("\nTHIS IS PART 3:\n")

print(np.arange(2,10,2))
print(np.arange(2,10,2).reshape(2,2))
print(c.ravel())
print(c)
print(c.flatten())
print(c)

print("\nTHIS IS PART 4:\n")

arr = np.arange(1,51)
arr = arr.reshape(10,5)
print(arr)

for i in range(10):
    print(f"Row {i+1}:{arr[i]}")

print(arr[3,0])
print(arr[0:5])
print(arr[8:10])
print(arr[:,4])
print(arr[:,2:4])

print("\nTHIS IS PART 5:\n")
arr1 = np.arange(0,18).reshape(3,6)
arr2 = np.arange(30,48).reshape(3,6)

print(arr1)
print(arr2)
print(arr2+arr1)
print(np.add(arr1,arr2))
print(arr2-arr1)
print(np.subtract(arr2,arr1))
print(arr2*arr1)
# print(arr2/arr1)
