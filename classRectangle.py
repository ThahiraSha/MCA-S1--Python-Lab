class Rectangle:
    def __init__(self,length=7,breadth=8):
        self.length=length
        self.breadth=breadth
    def getArea(self):
        return self.length * self.breadth
    def getPerimeter(self):
        return 2 * (self.length + self.breadth)
r1=Rectangle(5,6)
a=int(input("Enter the length of second rectangle:"))
b=int(input("Enter the breadth of second rectangle:"))
r2=Rectangle(a,b)
print("Area of first rectangle is:",r1.getArea())
print("Perimeter of first rectangle is:",r1.getPerimeter())
print("Area of second rectangle is:",r2.getArea())
print("Perimeter of second rectangle is:",r2.getPerimeter())
r3=Rectangle()
print("Area of third rectangle is:",r3.getArea())
print("Perimeter of third rectangle is:",r3.getPerimeter())
if r1.getArea() > r2.getArea():
        print("Area of first rectangle is greater than area of second rectangle")
elif r2.getArea() > r1.getArea():
        print("Area of first rectangle is less than area of second rectangle")
else:
    print("fist and second rectangles have equal area")