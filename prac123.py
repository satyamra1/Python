a=20
def f():
    a=15
    print(a)
    a=10
    print(a)
    def t():
        global a
        a=5
        print(a)
    t()
    print(a)
    def g():
        nonlocal a
        a=7
        print(a)
    g()
    print(a)
f()
print(a)