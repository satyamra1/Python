a=input("enter a sentence: ")
b=a.lower()
for i in range(97,123):
    if chr(i) not in b:
        print("not a panagram")
        break
    
else:
    print("panagram")
        