'''
24 WHAT IS FUNCTION ?
ans : A function is group of statement performing a specific task.
    'A function is a block of code which only runs when it is called.'
    A function can reused by the programer in a given program any number of
   syntax
        def func():
            print("hello")
    TYPE OF FUNCTION
    --> built in function : already present in python 
                            like print() , range()
    --> user defined function : difined by user

25 WHAT IS RECURSION ?
ans : Recursion is a function which calls itself 

'''
print("example of funtion :")

def func(name):
    print("hello " + name)

func("virat kohli \n")

print("example of recurtion :")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

a = factorial(5)
print(a)
    