def toh (n,a,b,c):
    if n>0:
        toh(n-1,a,c,b)
        print("move the discs from {} to {}".format(a,c))
        toh(n-1,b,a,c)
n=int (input("enter the number"))
toh(n,"a","b","c")