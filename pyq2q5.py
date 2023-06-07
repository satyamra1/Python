#string method in python
#titl,upper,lower,index, find,captalize,join

a=input("enter a string")
all_same = all(ch == a[0] for ch in a)
print(all_same)