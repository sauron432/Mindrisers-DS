def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("You are now inside the decorator.")

# This is what the @my_decorator syntax actually does behind the scenes:
# say_hello = my_decorator(say_hello)
say_hello()


# import time
# def timer(func):  
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs) # Call the original function
#         end_time = time.time()
#         print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to run.")
#         return result
#     return wrapper

# @timer
# def my_complex_calculation(n):
#     sum_val = 0
#     for i in range(n):
#         sum_val += i
#     return sum_val

# my_complex_calculation(1000000)