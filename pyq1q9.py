a=input("enter any string")
word=0
line=0
char=0
for i in a:
    word+=len(a.split())
    line+=1
    char=len(i)
print(word)
print(line)
print(char)