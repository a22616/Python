'''
17 WHAT IS DICTIONARY ?
ans : Dictionary is a collection of key-value pairs.
    syntax:
        a ={
            "key":"value"
            "mark":"100"
            "list":[1,2,3]
        }

18 TELL ITEM METHODS
ans : a.items() , a.keys() ,a.update("":"") ,a.get("")

19 WHAT IS SETS ?
ans : Set is a collection of non respective elements.sets in python as
    data types containing unique values.
    s = set()

20 TELL OPERATIONS ON SETSS
ans : len(s), s.remove(),s.pop(),s.clear(),
    s.union(),s.intersection()
'''
mydict = {
    "anand" :  5 ,
    " prem " : " love " 
}
print("options is",mydict.keys())
print("options is",mydict.values())

a = input("enter value of dict ")
print("your value is",mydict.get(a))

n1 = int(input("enter the num 1"))
n2 = int(input("enter the num 1"))
n3 = int(input("enter the num 1"))
n4 = int(input("enter the num 1"))
n5 = int(input("enter the num 1"))
n6 = int(input("enter the num 1"))
n7 = int(input("enter the num 1"))

s = {n1,n2,n3,n4,n5,n6,n7}
l = [n1,n2,n3,n4,n5,n6,n7]
t =(n1,n2,n3,n4,n5,n6,n7)
print("set", s)
print("list", l)
print("tupels", t)
print(s.union({8,11}))
print(s.intersection({8,11}))
