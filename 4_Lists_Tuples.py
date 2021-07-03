'''
14 WHAT IS LISTS?
ans : Python lists are containers to store a set of 
    values of any data type.
    ex. fruits = ['apple','orenge','mango']
    list indexing fruits[0] = apple

15 TELL LIST METHODS
ans : L1 = [1,8,7,6,21,15]
    L1.sort() L1.reverse() L1.append() L1.insert()
    L1.pop() L1.remove()

16 WHAT IS TUPLES ?
ans : A tuple is an immutable(cannot change) data type in python
    a = () empty tupeles
    a =(1,) tupel with only one element
    a (1,7,2) tupel with more than element
'''
print('first example \n')
l1 = [1 , 8 , 2 ,5 ,8 ,25]
l1.sort()
l1.reverse()
l1.append(50)
l1.insert(3,"anand")
l1.pop(2)
l1.remove(5)
print(l1)

print('\n example with input funtion \n ')
l = input("enter fruit name:\n")
l2 = input("enter fruit name:\n")
l3 = input("enter fruit name:\n")
l4 = input("enter fruit name:\n")
l5 = input("enter fruit name:\n")
l6 = input("enter fruit name:\n")
l7 = input("enter fruit name:\n")
fruit_name = [l ,l2, l3 ,l3 ,l5 , l6 , l7]
print(fruit_name)

print('\n tuple example with method \n ')
a = (1,2,0,4,1,5,2,2)
print(a.count(1))
print(a.index(4))
print(a)