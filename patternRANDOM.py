import random
a=random.randint(0,16)
for i in range (0,a):
    for j in range (0,a-1):
        print(" ",end="")
    for j in range (0,a+1):
        print("*",end=" ")
    print("")
for i in range (0,a):
    for j in range (0,a+1):
        print(" ",end="")
    for j in range (0,a-1):
        print("*",end=" ")
    print("")
print(a)