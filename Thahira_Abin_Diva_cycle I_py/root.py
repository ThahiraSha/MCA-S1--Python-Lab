import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b**2 - 4*a*c
if d==0:
    print("Roots of the quadratic equation is",-b/2*a)
elif d < 0:
    x=(-b/2*a)
    y=math.sqrt((-d)/2*a)
    print("Roots of the quadratic equation are:",x,"+",y,"i","and",x,"-",y,"i")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are", root1, "and", root2)
