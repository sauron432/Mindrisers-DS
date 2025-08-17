new_list = [i for i in range(5,100) if i % 2 == 0]

try:
    print(new_list[50])
except Exception as e :
    print(e)
else:
    print("Nothing went wrong.")
finally:
    print("This is finally block.")

print()
 
try:
    file = open("hello.txt", "r")
except Exception as asd:
    print(asd)
else:
    print("Nothing went wrong.")    
    
print()    
    
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
# finally:
#     print("This if finally block. This will be printed no matter what.")
    
