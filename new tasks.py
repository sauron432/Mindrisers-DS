import random
from functools import reduce
# list_a = [random.randint(1, 100) for _ in range(5)]
# list_b = [random.randint(1, 10) for _ in range(5)]

# print(f"List 1:{list_a}")
# print(f"List 2:{list_b}")

# sum_of_lists = []
# i = 0
# while i<len(list_a):
#     sum_of_lists.append(list_a[i]+list_b[i])
#     i += 1
  
# for i in range(len(list_a)):
#     sum_of_lists.append(list_a[i]+list_b[i]) 

# print(f"Sum of lists:{sum_of_lists}")
    
# 1. Reverse a list    
list_reverse = [1,2,3,4,5,6,7,8,9,10]

reversed_list = []

for i in range(len(list_reverse)):
    # print(list_reverse[len(list_reverse)-i-1])
    reversed_list.append(list_reverse[len(list_reverse)-i-1])
    
print('Reversed list:', reversed_list,"\n")

# 2. Even Numbers from a list
list_even = []
for i in list_reverse:
    if i%2 == 0:
        list_even.append(i)

print("Using for loop:", list_even,"\n")

list_even_new = list(map(lambda x : x if x%2 == 0 else None,list_reverse))
list_even_new = [num for num in list_even_new if num is not None]

print("Using map and lambda:", list_even_new,"\n")


# 3. Find squares of Numbers using map and lambda

given_list = [1,2,3,4,5]

squared_list = list(map(lambda x: x**2,given_list))
print("Square of list using map and lambda:",squared_list,"\n")

# 4. Sum of even numbers in a list 

random_list = [random.randint(1,100) for _ in range(10)]
# list_of_even_num = [x for x in random_list if (lambda x: x % 2 == 0)(x)]
list_of_even_num = list(filter(lambda x:x % 2 == 0,random_list))
print("List of even numbers:", list_of_even_num,"\n")

sum_of_even_num = reduce(lambda a,b:a+b,list_of_even_num)
print("Sum of even numbers:", sum_of_even_num,"\n")

# 5. Find words starting with a letter

list_names = ["Sanjay","Suraj","Akash","Ankit","Ares","Bill","Aurora"]
name_begin_a = list(filter(lambda x: x.startswith("A"),list_names))
print("These names begin with a:",name_begin_a,"\n")

# 6. Find the maxim numnber
list_for_sum = [random.randint(1,50) for _ in range(4)]
sum_from_list = reduce(lambda a,b:a+b,list_for_sum)
print("Max in the list:",sum_from_list,"\n")

# 7. Create a list of cubes

list_of_cubes = [x**3 for x in range(1,11)]
print("The list of cubes:",list_of_cubes,"\n")

# 8. Palindrome check

def palindrome_or_not(inp):
    if inp == inp[::-1]:
        return True
    else:
        return False

# print(palindrome_or_not("detartrated"))
   
# 9. Merge two lists into a dictionary

list_one = [1,3,5,3,25]
list_two = ['an','ce','np','in','cn']

zipped = {}
if len(list_one) == len(list_two):
    zipped = dict(zip(list_one,list_two))
    print("By usign zip():",zipped,"\n")
else:
    print("Lists are of different lengths.","\n")

dict_comprehension = {list_one[i]:list_two[i] for i in range(len(list_one))}
print("By using dict comprehension:",dict_comprehension,"\n")

# 10. Find the second largest number.

new_list = [1,45,2,32,654,34,121,232,-23,-89]
new_list.sort()
print("The second largest nubmer:",new_list[-2],"\n")
    
# for i in list_names:
#     if i[0] == "S" or i[0]=="s":
#         print(i)
        
