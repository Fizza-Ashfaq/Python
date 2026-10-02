from my_package import add,sub,mul,div,length,title_format

print("---Math Operations---")
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

print(f"Addition: {add(num1,num2)}")
print(f"Subtraction: {sub(num1,num2)}")
print(f"Multiplication: {mul(num1,num2)}")
print(f"Division: {div(num1,num2)}")

print("---String Operations---")
string=input("Enter a word: ")
print(f"Length of characters: {length(string)}")
print(f"Title Format: {title_format(string)}")