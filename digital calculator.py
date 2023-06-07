import math
n1=input("enter the first number")
s=input("enter the operation which you want ")
n2=input("enter the second number ")
if s=="+":
    result=n1+n2
elif s=="-":
    result=(n1-n2)
elif s=="*":
    result=n1*n2
elif s=="/":
    result=n1/n2
elif s=="sqrt":
    result=math.sqrt(n1)
elif s=="pow":
    result=math.pow(n1,n2)
elif s=="log":
    result=math.log(n1)
else:
    print("please enter the valid operations")
print(result)