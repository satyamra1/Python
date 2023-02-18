#write a python program to take number of legs and heads from user in a poultry form . find hens and no of goats in that farm..
#hens have 2 legs
#goat have 4 legs 

# 4 legs and 4 heads-1 goat 2 hens
legs=int(input("enter no of legs"))
heads=int(input("enter no of heads"))
a=(legs-2*heads)//2
b=heads-legs
print("no of goat are",a)
print("no of hens are",b)

