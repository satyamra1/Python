'''Write a Python program to input electricity unit. charges and calculate total electricity bill according

and side" to the given condition:
 For first 50 units Rs 0.50/unit
 For next 100 units Rs. 0.75/unit
 For next 100 units Rs. 1.20/ unit
For unit above 250 Rs. 1.50/unit 
An additional surcharge of 20% is added to the bill.'''
a=int(input("enter the units of electricity"))
if (a>=50):
    amt=(a*0.50)
    print("The electricity bill is",amt)
elif (a>50 and a<=150):
    amt=(50*0.50)+((a-50)*0.75)
    print("The electricity bill is",amt)
elif (a>150 and a<=250):
    amt=(50*0.50)+(100*0.75)+((a-150)*1.20)
    print("The electricity bill is",amt)
else:
    amt=(50*0.50)+(100*0.75)+(100*1.20)+((a-250)*150)
    print("The electricity bill is",amt)




