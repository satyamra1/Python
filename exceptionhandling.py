try:
    num=int(input("enter any number"))
    a=[6,4]
    print(a[num])
except ValueError:
    print("given value is not an integer")
except IndexError:
    print("index error")