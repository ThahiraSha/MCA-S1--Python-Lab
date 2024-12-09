class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
        self.__area=length*breadth
    def __lt__(self,other):
        if self.__area < other.__area:
            print(f"{other.__area}is greatest ")
        else:
            print(f"{self.__area} is greatest")
r1= Rectangle(10,20)
r2=Rectangle(40,4)
r1<r2