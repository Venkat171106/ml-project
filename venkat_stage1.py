a, b, op = input("Enter: ").split(", ")

a = int(a)
b = int(b)

if op == '+':
    result = a + b

elif op == '-':
    result = a - b

elif op == '*':
    result = a * b

elif op == '/':
    if b == 0:
        print("Error: Division by zero")
        exit()
    result = a / b

else:
    print("Invalid operator")
    exit()

print("Result =", result)
