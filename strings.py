'''
12 WHAT IS STRINGS?
ans : String is a data type in pyton.
    write a string in these three way ,single,double,triple quoted

13 WHAT IS STRING SLICING ?
ans : A string slicing in pytin can be sliced for 
    getting a part of the string.we can skip value in slicing
    string function like
    String.endwith("")
    string.count("c")
    string.capitalise()
    string.find()
    string.replace

    Escape sequence charaters
    \n newline ,\t tab ,\' singleqoute,\\ backslach, etc
'''
a = '''anand is good'''
print(a[0:3:2])
print(len(a))
print(a.endswith("nd"))
print(a.count("a"))
print(a.capitalize())

print(a[0:5])

print(a.replace("anand","Ram")) 