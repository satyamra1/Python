import random
import string

a=string.ascii_uppercase
b=string.digits
c=string.punctuation

d=random.sample(a,2)
e=random.choice(b)
f=random.choice(c)
g=random.choices(string.ascii_lowercase,k=5)
password=d+[e]+[f]+g
random.shuffle(password)
password1=''.join(password)
print("generated password:",password1)
