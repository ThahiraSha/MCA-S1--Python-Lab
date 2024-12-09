n=int(input("Enter the no of terms:"))
n1=0
n2=1
if n==0:
    print("Enter valid terms")
elif n==1:
    print(n1)
else:
    print(n1,n2,end=" ")
    for i in range(2,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")