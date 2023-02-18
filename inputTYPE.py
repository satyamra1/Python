'''TO CHECK INPUT IS ALPHABET , DIGIT OR SPECIAL CHARACTER'''
ch=input("enter any character")
if(ch>='a' and c<='z')or (ch>='A' and ch<='Z'):
    print("input is a alphabet")
elif(ch>='0' and ch<='9'):
    print("input is a digit")
else:
    print("special character")
