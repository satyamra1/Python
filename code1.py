x=int(input("enter"))
a=x%10
x=x//10
b=x%10
x=x//10
rev=a*100+b*10+x
print(rev)
