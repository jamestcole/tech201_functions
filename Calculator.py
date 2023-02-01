def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1/num2)

def calculator():
    calculate = True
    while calculate:
        button = input("press calculator button here (+,-,*,/,(x for exit)):")
        if button == "-":
            subtract(int((input("first number:"))),int((input("second number:"))))
        elif button == "+":
            add(int((input("first number:"))),int((input("second number:"))))
        elif button == "*":
            multiply(int((input("first number:"))),int((input("second number:"))))
        elif button == "/":
            divide(int((input("first number:"))),int((input("second number:"))))
        elif button == "x":
            print("exiting ...")
            calculate = False
        else:
            print("not a button")

calculator()