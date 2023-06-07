count=0
with open ("gla.txt",'r') as b:
    c=b.read()
    d=c.split()
    count=count+len(d)
    print(count)
   
