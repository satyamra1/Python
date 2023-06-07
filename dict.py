


def displayInventory(d):
    sum=0
    for i,j in d.items():
        print(i,j)
        sum=sum+j
    #print("total=",sum)
    return sum
    
    
x=int(input("enter the value of rope"))
y=int(input("enter the value of gold coin"))
z=int(input("enter the value of arrow"))
p=int(input("enter the value of torch"))
a={'rope':x,'gold coin':y,'arrow':z,'torch':p}

total=displayInventory(a)
print(total)