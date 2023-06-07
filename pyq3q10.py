palindrome_no=[]
for i in range(1000,10000):
    b=str(i)
    c=b[::-1]
    if(b==c):
        palindrome_no.append(i)

for palindrome in palindrome_no:
    print(palindrome)

with open("gla.txt", "a") as file:
    for p in palindrome:
        file.write(str(palindrome) + "\n")
    
    