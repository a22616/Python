'''
32 WHAT IS TRY EXCEPTION.
ans : The try block lets you test a block of code for errors.
    The except block lets you handle the error.
    The finally block lets you execute code, regardless of the result of the try- and except blocks.

33 WHAT IS EXCEPTION HANDLING ?
ans : When an error occurs, or exception as we call it, Python will 
    normally stop and generate an error message.
    These exceptions can be handled using the try statement

'''
try:
    print(x)
except Exception as e:
    print(e)
finally:
    print("this code always work")