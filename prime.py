n=int(input("enter the number"))
i=2
while i<=n-1:
    if n%i==0:
        break
    i+=1
if i==n:
     print("PRIME")
else:
     print("not prime")
