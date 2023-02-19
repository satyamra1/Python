#WRIETE A PROGRAM TO GIVE GRADE OF NUMBERS
marks=int(input("enter your marks\n"))
if marks>=90:
    print( 'grade="Ex"')
elif (marks>=80 and marks<90):
    print( 'grade="A"')
elif (marks>=70 and marks<80):
    print( 'grade="B"')
elif (marks>=60 and marks<70):
  print( 'grade="C"')
elif (marks>=50 and marks<60):
   print( 'grade="D"')
    
else:
    print("fail ")