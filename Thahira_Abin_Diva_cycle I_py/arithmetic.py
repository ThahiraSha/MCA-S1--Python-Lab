n1 = int(input("Enter 1st no: "))
n2 = int(input("Enter 2nd no: "))
i = 0
while i == 0:
    print("Choose your Operations..\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.Exit")
    op = int(input("Enter the operation number: "))

    if op == 1:
        add = n1 + n2
        print("Sum of", n1, "and", n2, "is", add)
    elif op == 2:
        sub = n1 - n2
        print("Difference of", n1, "and", n2, "is", sub)
    elif op == 3:
        pro = n1 * n2
        print("Product of", n1, "and", n2, "is", pro)
    elif op == 4:
        if n2 != 0:
            div = n1 / n2
            print("Division of", n1, "and", n2, "is", div)
        else:
            print("Cannot divide by zero")
    elif op == 5:
        i = 1
        print("Exiting...")
    else:
        print("Enter a valid Operation")
