a=input("enter a string")
count=0
for i in a:
    if i in ('aeiou'or'AEIOU'):
        count=1 
    else:
        count=0
if count==1:
    print("accepted")
else:
    print("not accepted")