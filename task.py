# Comparison Operator

x,y = 10,7

print(x > y) # True as 10 is greater than 7
print(x < y) # False as 10 is not less than 7
print(x == y)# False as 10 is not equal to 7
print(x != y)# True as 10 is not equal to 7

# Boolean Variables 

print()
status = True
print(status) 
print(type(status))

status = False
print(status) 
print(type(status))

# String Creation and length
print()
text = "Hello World!"
print(len(text))
print(type(text))

# String indexing
print()
s = "Python"

for i in s:
    print(i)

print() 
print(s[-1])
print(s[-6])
print(s[-6:-1:5])

# String Slicing
print()
lang = "Programming"
print(lang[:4])
print(lang[3:])
print(lang[2:9])

# Exploring len() on slices

part1 = lang[:7]
print(len(part1))
print(len(lang))
'''
len() function returns the length of the string.
Here, part1 is a substring obtained from the string lang having lesser characters that the source string.'''

# String Methogs - Case conversion
phrase = "Hello, Python!"
print("\n"+phrase)
print(phrase.upper())
print(phrase.lower())

# Combining strings 

str1 = "Data"
str2 = "Science"
combined = str1 + " " + str2
print("\n"+combined)

# Arithmetic Operator Precedence

a,b,c = 5,3,2
print(a+b*c)
print((a+b)*c)
'''
In python, paranthesis has the highest precedence, so the calculations inside the paranthesis are performed before the rest.
In the first print statement, the multiplication is performed first, then the addition. In the second print
statement, the addition is performed first, then the multiplication. This is why the results are different.
'''

#String Index Out of range

text = "Hello"
print(len(text))
#print(text[10])
# The length of the string text is 5 , so there is no index 10. This will result in an IndexError as the index is more than the length of the string.

# Equality vs. Identity check
s1 = "test" 
s2 = "test"  
print(s1 == s2)

'''
The code `print(s1 == s2)` is checking if the values of the variables `s1` and `s2` are equal.
It will print `True` if the values are equal, and `False` if they are not.
'''

print(s1 is s2)
'''
The code `print(s1 is s2)` is checking if the variables `s1` and `s2` are referring to the same object in memory.
It checks for identity, meaning it verifies if both variables point to the same
memory location. If they do, it will print `True`; otherwise, it will print `False`.
'''
#Complex Numbers
print()
z = 3+4j
print(z.real)
print(z.imag)
print(type(z))

#Comparisons with float
f1 = 0.1 + 0.2 
f2 = 0.3
print(f1 == f2)
print(f1)
print(f2)
'''
f1 is the result of adding two floating point numbers (0.1 and 0.2).This results in a value very close to but not exactly 0.3. 
f2 is assigned to 0.3, which is also an approximate but slightly different from the sum of 0.1 and 0.2 due to representation differences in binary floating point numbers.
'''