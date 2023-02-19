text=input("enter the text\n")
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("dont worry" in text):
    spam=True
elif("satyam is here for your help" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This text is spam")
else:
    print("This text is not a spam")