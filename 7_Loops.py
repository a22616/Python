'''
22 Application of loops
ans : loops make it easy for a programmer to tell the computer,
    which set of intruction to repeat.

23 TYPES OF LOOPS IN PYTHON
ans : Two types
    1 while loop
    2 for loop

    while loop
--> IN while loop , the condition is checked first if it evaluates
    to TRUE, the body of the loop is executed otherwise NOt.
--> if the loop is entered the process of is continued until 
    the condition bicome FALSE.

    For loop
--> A for loop is used for iterating over a sequence 
    (that is either a list, a tuple, a dictionary, a set, or a string).

'''
print("\n factorial using while loop \n")
num = int(input("enter number \n")) 
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"value is {factorial}")    

print("\n sum using while loop \n")
n = int(input("enter number\n"))
i = 0
while i <= n :
    sum = i + n 
    i = i + 1

print(f"value of sum {sum}")

print("\n example of for loop")
l = ['n1','n2','n3','n4','n5','n6','n7']

for item in l :
    print(item,end=" ")

print("\n")
for anand in range(1,8):
    print(anand,end=" ")

print("\n table of n using for loop")
a = int(input("enter value \n"))
i = 1
for j in range(10):
    print(f"{a} * {i}= {a*i}")
    i = i + 1

