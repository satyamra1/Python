def isshorted(my_list):
    
    if(lst==b):
        print("list is shorted")
    else:
        print("list is not shorted")
lst=[]
n=int(input("enter no of element in list"))
for i in range(0,n):
    a=int(input())
    lst.append(a)
print(lst)
b=sorted(lst)
print(b)

isshorted(lst)
