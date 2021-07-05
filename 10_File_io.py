'''
26  WHAT IS FILE HANDELING IN PYTHON ?
ans : File handling is an important part of any web application.
    Python has several functions for creating, reading, updating, and deleting files.
--> A file is data storee in a storage device a pyhon programe can
    talk to the file by reading content from it and writting content to it

27 TYPES OF FILES
ans : there are two types of file 
   1 TEXT file like .txt
   2 Binary files like .jpg   

28 OPEN AND WITH OPEN 
ans open() function for opning files and read write and apdate
    f = open("filename.txt","r")
    text = f.read()
    print(test)
    f.colse()

    r = reading w = writing a = appending, + = updating

 also use with open auto close() funtion
    with open("filename.txt")as f:
        f.read()
'''
f = open("filename.txt","w")
f.write("file is create and add with text")
f.close()

with open("filename.txt")as f:
    a = f.read()
    print(a)