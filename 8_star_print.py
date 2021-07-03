n = int(input("enter number \n"))
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i-1))

print("\n")
for i in range(n):
    print("* " * n)
    
    for j in range(n-2):
        z = n*2 - 1
        print("*" * (n-(n-1)),end="")
        print(" " * (z-2),end="")
        print("*" * (n-(n-1)))
    
    print("* " * n)
    i == 1
    break