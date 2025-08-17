# Section 1: Lists
a  = list(range(1,16))
print(a)

favourite_fruits = ['pineapple','mango','watermelon','apple','strawberry']
print(favourite_fruits)

list1 = [10,20,30,40,50]
sliced = list1[-5::4]
print(sliced)

any_list = [1,2,"Hello","World",1+9j]
print(len(any_list))

empty_list = []
for i in range(3):
    empty_list.append(i)
print(empty_list)

list2 = [1,3,4]
list2.insert(1,2)
print(list2)

list3 = [1,2,3,4,5]
list3.remove(3)
print(list3)

list4 = [10,20,30,40]
print(list4.pop())
print(list4)

list5 = [0,1,2,3,4,5]
print(list5[2:5])

list_6 = [1,2,3]
list_7 = [4,5,6]
print(list_6 + list_7)

list8 = [1,2]
print(list8 * 3)

copied_list = list8.copy()
print(f"Copied List: {copied_list}")
print(f"Original List: {list8}")
print(f"Cleared List: {list8.clear()}")


# Section 2 Tuples

print()
tuple =(1,2,3)
print(tuple) 

color_tuple = ('red','green','blue')
print(color_tuple)

tuple1 = (10,20,30,40)
print(tuple1[1])

tuple2 = (0,1,2,3,4)
print(tuple2[1:4])

tuple3 = (1,2)
tuple4 = (3,4)
print(tuple3 + tuple4)

tuple5 = ("Alice",25,"New York")
Name, age,city = tuple5
print("Name:" + Name)
print(f"Age:{age}")
print("Address:" + city)

list_to_tuple = [1,2,3,4]
new_tuple = (*list_to_tuple,)
print(new_tuple)

tuple6 = (1,2,2,3,2)
print(tuple6.count(2))

tuple7 = (10,20,30,40)
print(f"The index of 30 is '{tuple7.index(30)}\'")