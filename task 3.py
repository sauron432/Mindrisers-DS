import random

#Integer & Float mix
a = 3
b = 3.33
add = a + b 
subtract = a - b
product = a * b
divison = a/b
print(f"Sum:{add}\nDifference:{subtract}\nProduct:{product}\nDivision:{ divison}")
#type(print(add))

#Large Integers & Type
annual_sales = 645681258237800
print(annual_sales)
print(type(annual_sales))

#Complex Number Basics
z = 3+4j
print(z.real)
print(z.imag)
print(type(z))
complex_addition = z + (2+1j)
print(complex_addition)

#Boolean from Comparisons
m,n = 10,15
status = m>n
print(type(status))
status = m!=n 
print(type(status))

#String Creation and Indexing
text = "Helloworld"
print(text[0::9])
print(text[-10::9])

#String Slicing
lang = "PythonProgramming"
print(lang[2:8]) 
print(lang[:6])
print(lang[::-1])

#String methods
phrase = " Hello, Python World! "
print(phrase.strip())
print(phrase.upper())
print(phrase.replace("Python","New "))
'''
Strings are immutable in Python as their content cannot be changed after the initialisation of the variable.
'''

name = "Rajesh"
score = 95
print(f"{name} scored {score} points.") #f-string formatting
print(name + " scored " + str(score) + " points.") #concatenation


age = 23    
have_voter_id = 1
nepali_citizen = 1
output = age > 18 or nepali_citizen == True and not(have_voter_id)  

print(output)
'''
At first, the expressions inside the paranthesis is handled first, followed by the not operator.
After that, the comparison operators are evaluated from left to right. Lastly, the and operation is evaluated before the or operation.
'''

new_list = [10,34,52,10,9]
print(f"First item:{new_list[0]}")  
print(f"Last item:{new_list[len(new_list)-1]}")
print(f"Middle item:{new_list[2]}")

nums = [10,20,30,40]
nums.insert(2,25)
nums.pop()
print(nums)

letters = ["a","b","c","d","e"]
print(letters[1:4])

random_int = [10,30,14,50,-4,110,95,-52,0,1,9,4]
random_int.sort() 
print(random_int)   
random_int.reverse()
print(random_int)

list1 = [1,2,3] 
list2 = [4,5,6]
print(list1 + list2)  #concatenation
list1.extend(list2) #extended
print(list1)

float_list = [1.2,1.9,3.3,4.98,3.14]
print(f"Sum :{sum(float_list)}")
print(f"Min :{min(float_list)}")
print(f"Max :{max(float_list)}")

t = (10,20,"Hello",True)
print(t)
print(type(t))
print(t[0:2])
print(t[-1:])

t2 = ("Tom",25,"Engineer")
name,age,profession = t2
print(name)
print(age)
print(profession)

#t[0] = 120
'''
This displays an error because tuples are immutable in Python, meaining the value of the elememnts of a tuple cannot be altered. 
Adding new elements or removind existing elements is also not possible in a tuple.
'''

my_set = {1,3,5,7}
print(f"Contains 5: {my_set.__contains__(5)}")
print(f"Does not contain 2: {not(my_set.__contains__(2))}")

my_set.add(9)
my_set.remove(3)
print(my_set)

setA  = {1,2,3}
setB = {3,4,5}
print(f"Union: {setA.union(setB)}")
print(f"Intersection: {setA.intersection(setB)}")   
print(f"Difference: {setA.difference(setB)}")

vals = [1,2,2,3,3,3,4]
list_to_set = set(vals)
print(vals)
print(list_to_set)

my_list = [2,4,4,6]
my_frozenset = frozenset(my_list)
print(my_frozenset)
# Frozenset, like set, only stores unique elements. Duplicate elements will be ignored.
#my_frozenset.add(5)
''''
This will result in an 'AttributeError as "add" attirbute is only available for set objects.
Frozensets are immutable , meaning the elements of a frozenset cannot be modified once it is created.
'''

new_dict = {my_frozenset:"Frozen set as a key."}
print(new_dict)
# set_dict = {setA:"Set as key"}
# print(set_dict)
'''
This will result in unhashable type error. Dictionary keys must be hashable i.e the hash value must not change during it's lifetime.
Sets are mutable and therefore not hashable thus making them unsuitable as dictionary keys.
'''

student = {
    "name": "Ramesh",
    "age": 20,
    "grade": "A"
}
print(student["name"])
print(student["age"])
student["city"] = "Kathmandu"
student.update({"age":'21'})
print(student)
student.pop("grade")
print(student)

record = {
    "id":101,
    "info":{"name":"Bob","dept":"IT"},
}

print(record["info"]['dept'])


a,b,c = 4,2,5
print(a+b*c)
print((a+b)*c)
'''
The operation is conducted from left to right in order of precedence of the operators.
In first case, the multiplication is conducted first and then addition.
In second case, the paranthesis is operated first. The addition is conducted first and then multiplication.
'''

x,y = 19,4
print(x%y)
print(x//y,"\n")
'''
The modulo operator returns the remainder of the division.
It will return 0 if the dividend is perfectly divisible by the divisor i.e quotient is not float.
"//" performs floor division i.e if the quotient has decimal then it will be ignored.
'''

print(2**3)
out = 3**4
print(2**3+out)

print("apple"<"banana")
print("apple">"banana")
print("apple"=="banana\n")

print(5 == 5.0)
print(5 is 5.0,'\n')

'''
The quality operator checks if the values are equal or not whereas 'is' operator checks if the values refer to same memory location or not.
'''

print(2<3<5,'\n')
'''
Python handles chained comparisons as if they were written with 'AND' operator.
2<3<5 is equivalent to (2<3) and (3<5). It evaluates (2<3) first, then (3<5).
since both are True amd True, it returns True.
'''

p,q = True,False
print(p)
print(q)

has_id = 0
print((age>18) and (has_id == True),'\n')

print(p or q)

r = (10>5)
print(not(r))

length_of_list = ['nepal','china','bhutan',1,2,3,5+8j]
print(len(length_of_list))


type_list = [10,10.5,'ten',True,3+2j]

for i in type_list:
    print(type(i))
# int are number without a decimal point
# float are numbers with a decimal point
# str are sequence of characters or anything written wihtin quotes.
# bool are boolean values i.e True or False
# complex are numbers with a real and imaginary part. They are written with a 'j'.

print()

print(abs(10))
print(abs(-10))
print(abs(-3.5),'\n')
# abs() function returns the absolute value of a number i.e positive

print(round(3.14159,2))
# round() function returns a number rounded to the nearest integer or to a given number of decimals.
# round(3.14159,2.5) will raise an error as we can't round to a non-integer number of decimals i.e only integers are accepted.

numeric_values = [random.randint(1, 100) for _ in range(5)]
print(sum(numeric_values))
print(min(numeric_values))
print(max(numeric_values))

vals = (3,1,4,2)
print(f"Sorted:{sorted(vals)}")
print(f"Original:{vals}")

booleans_list = [0,1,1,0,1]
print(any(booleans_list))
#any() returns True if at least one element of an iterable is true.
print(all(booleans_list))
#all() returns True if all elements of an iterable are true.

exp_a = (10.12 > 10.122)
exp_b = (10.00 == 10)
print(exp_b or exp_a) 
print(exp_b and exp_a)  

multiline_string = """ My favourite hobby is fishkeeping. I have been a fishkeeper for more than 10 years.
Fish keeping is more than just putting fish in a fish tank or aquarium. It is a fascinating blend of biology, chemistry, and art.
It requires patience, dedication, and a willingness to learn. A fish is more than just a pet.
"""

# string_of_a = "a a A A a a "
# print(string_of_a.count("A"))
# print(string_of_a.count("a"))

print(multiline_string.count("a"))
# count() returns the number of occurrences of a substring in a string. The parameter passed is also case sensitive, so it counts either uppercase or lowercase letters bsaed on the parameter given.

advanced_string = "ABCDEFGHIJ"
print(advanced_string[0::2])
print(advanced_string[::-2])

string1 = "Case"
string2 = "case"
print(string1 == string2)
string1 = string1.casefold()
print(string1 == string2)
# casefold () is similar to lower() but it is more aggressive in removing case distinctions. casefold() handles a broader set of characters from various Unicode scripts than lower() does.


name1 = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50

print(f"{name1} purchased {quantity} {product} for a total of ${quantity*price:.2f}")

'''user_input_str = input("Enter a string that represents a number: ")
print(user_input_str)
print(float(user_input_str))
print(bool(user_input_str))'''

fruits = ["apple","banana","cherry"]
fruits.reverse()
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
# fruits.sort(reverse=True) sorts the list in descending order and modifies the original list.
# fruits.reverse() reverses the list in-place and modifies the original list. In this case, double reversing results in the original list.

number_list = [2,5,7,1,9]
number_list = number_list[:1] + [4] + number_list[1:]
print(number_list)

info = ["John",28,True,4500.75]
print(info[0],info[3])

tuple1 = (1,2)
tuple2 = (3,4)
print(tuple1+tuple2)
print(tuple1*3)

single_tuple = (42,)
single_tuple1= (42)
print(type(single_tuple))
print(type(single_tuple1))

set_a = {1,2,3,4}
set_b = {1,2,3}
print(set_a.intersection(set_b))

print(set_b.issubset(set_a))
print(set_a.issubset(set_b))


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome"
}

print(capitals.keys())
print(capitals.values())
print(capitals.items())

numbers = {
    "x":4,
    "y":10,
    "z":6
}
print(sum(numbers.values()))