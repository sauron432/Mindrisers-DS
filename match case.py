# day = int(input("Enter the day:"))

# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("wednesday") 
#     case 5:
#         print("Thursday")
#     case _:
#         print("Invalid.")


def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def product(a,b):
    return a*b
def division(a,b):
    return a/b

while True:

    input1 = float(input("Enter first number:"))
    input2 = float(input("Enter second number:"))
    perform = input("Which operatoin to perform:")

    if perform == "+":
        print("Sum:",add(input1,input2))
    elif perform == "-":
        print("Difference:",diff(input1,input2))
    elif perform == "*":
        print("Product:",product(input1,input2))
    elif perform == "/":
        if input2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Division:",division(input1,input2))
    else:
        print("Invalid operation")
        
    match perform:
        case "+":
            print("Sum:",input1+input2)
        case "-":
            print("Difference:",input1-input2)
        case "*":
            print("Product:",input1*input2)
        case "/":
            if input2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Division:",input1/input2)
        case _:
            print("Invalid operation.")                                
    again = input("Do u want to exit?(Y/N):").upper()
    if(again == "Y"):
        print("You are now exiting the program.")
        break
    