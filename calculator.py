A = float(input("enter the number:"))
B = input("enter a operator (+,-,*,/):")
C = float(input("enter the number:"))
if B == "+":
    print( A + C )
elif B == "-":
    print( A - C )
elif B == "*":
    print( A * C )
elif B == "/":
   if "A/0":
       print("unable")
   else:
    print( A / C )
