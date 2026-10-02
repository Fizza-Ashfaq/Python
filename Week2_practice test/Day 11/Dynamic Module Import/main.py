choice=int(input("Enter your choice (1=Addition or 2=Multiplication: )"))
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

if choice==1:
    from addition import add
    print(f"Addition: {add(num1,num2)}")
elif choice==2:
    from multiplication import mul
    print(f"Multiplication: {mul(num1,num2)}")