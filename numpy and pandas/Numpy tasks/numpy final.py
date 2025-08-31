import numpy as np
#NUmber 1 
num_array = np.arange(10,51)
print(num_array)

#NUmber 2
i_matrix = np.identity(3,int)
print(i_matrix)

#NUmber 3
random_array = np.random.randint(1,101,10)
print(random_array)
#NUmber 4
print(random_array.min())
print(random_array.max())

#NUmber 5
array1d = np.arange(0,12)
print(array1d.reshape(3,4))

#NUmber 6
numbers = np.arange(50,101)
even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)

#NUmber 7
array = np.array([1,2,3,4,5])
print(array ** 2) 

#NUmber 8
array5by5 = np.arange(0,25).reshape(5,5)
print(array5by5.mean())

#NUmber 9
given_array = np.array([10,20,50,40,30])
print(given_array.argmax())

#NUmber 10
array2 = np.array([6,7,8,9,10])

print("Addition:",array + array2)
print("Subtraction:",array2 - array)
print("Multiplication:",array * array2)
print("Division:",array2 / array)