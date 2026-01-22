a=float(input("a: "))
b=float(input(" b: "))
c=float(input(" c: "))

d=b*b-4*a*c
if d<0:
 print("Коренів немає")
elif d==0:
 x=-b/(2*a)
 print("x=",x)
else:
 x1=(-b+d**0.5)/(2*a)
 x2=(-b-d**0.5)/(2*a)
 print("x1=",x1)
 print("x2=",x2)
