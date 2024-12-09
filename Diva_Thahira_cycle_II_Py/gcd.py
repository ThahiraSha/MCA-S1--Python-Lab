num1=int(input("Enter the first no:"))
num2=int(input("Enter the second no:"))
if num2>num1:
    num1,num2=num2,num1
r=1
while r!=0:
    r=num1%num2
    num1=num2
    num2=r
print("GCD is",num1)





