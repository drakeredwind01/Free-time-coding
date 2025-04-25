'''
@b001
What Are Python DECORATORS?? #python #programming #coding
https://www.youtube.com/shorts/n-Rf3EJ_WaU
'''

def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print("Complete")
    return wrapper

@my_decorator
def do_this():
    print('Doing This')

@my_decorator
def do_that():
    print('Doing That')

do_this()
do_that()





