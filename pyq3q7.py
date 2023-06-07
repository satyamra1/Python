import random
b=random.sample(range(1,9),5)
print(b)
#sample module is used to produce random no in format of list
a=[random.randint(2,15) for iter in range(10)]
print(a)
#randrange is also used to generate random no is form of list
c=[random.randrange(1,20) for iter in range(6)]
print(c)