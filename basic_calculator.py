# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + int(num2)
# float will convert a string into a number
# print(result)

# calc 2
num1 = float(input("Enter 1st numb: "))
op = input("Enter operator: ")
num2 = float(input("Enter number 2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num1)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")