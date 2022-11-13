import math

print('Welcome')

help = input('If you need Help Press [y], If not Press [n]')
if help == "y":
    print("Operators:")
    print("Addition       -->  +   ")
    print("Subtraction    -->  -   ")
    print("Multiplication -->  *   ")
    print("Division       -->  /   ")
    print("Exponentiation -->  ^   ")
    print("sqrt           --> sqrt ")
    print("cosine         --> cos  ")
    print("sine           --> sin  ")
    print("tangent        --> tan  ")
    print("arc tangent    --> cot  ")
    print("factorial      --> fact ")
else: 
    result = 0

    a = float(input('Enter first Number'))

    op = input("State your Operator (if you need help, Press [h]")

    if op == "h":
        print("Operators:")
        print("Addition       -->  +   ")
        print("Subtraction    -->  -   ")
        print("Multiplication -->  *   ")
        print("Division       -->  /   ")
        print("Exponentiation -->  ^   ")
        print("sqrt           --> sqrt ")
        print("cosine         --> cos  ")
        print("sine           --> sin  ")
        print("tangent        --> tan  ")
        print("arc tangent    --> cot  ")
        print("factorial      --> fact ")
        op = input("State your Operator")

    if op == "sqrt":
        result = math.sqrt(a)
    elif op == "sin":
        a = math.radians(a)
        result = math.sin(a)
    elif op == "cos":
        a = math.radians(a)
        result = math.cos(a)
    elif op == "tan":
        a = math.radians(a)
        result = math.tan(a)
    elif op == "cot":
        a = math.radians(a)
        result = math.atan(a)
    elif op == "fact":
        a = math.ceil(a)
        result = math.factorial(a)
    elif op == "log":
        a = math.log10(a)
    elif op == "+":
        b = float(input())
        result = a + b
    elif op == "-":
        b = float(input())
        result = a - b    
    elif op == "*":
        b = float(input())
        result = a * b
    elif op == "/":
        b = float(input())
        if b == 0:
            print("NaN")
        else:
            result = a / b
    elif op == "^":
        b = float(input())
        result = math.pow(a,b)


    print(result)
