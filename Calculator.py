def add(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return(float(num1) + float(num2))
    else:
        print("please type valid numbers")

def subtract(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return(float(num1) - float(num2))
    else:
        print("please type valid numbers")

def multiply(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return(float(num1) * float(num2))
    else:
        print("please type valid numbers")

def divide(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return(float(num1) / float(num2))
    else:
        print("please type valid numbers")

def CMtoM(num1):
    if num1.isdigit():
        return((float(num1))/100)
    else:
        print("please type valid numbers")

def MtoFEET(num1):
    if num1.isdigit():
        return(round(((float(num1))*3.2808399),2))
    else:
        print("please type valid numbers")


def calculator():
    calculate = True
    while calculate:
        button = input("press calculator button here (+,-,*,/,(CM for m from cm),(F for feet from m),(x for exit)):")
        if button == "-":
            print(subtract(input("first number:"),input("second number:")))
        elif button == "+":
            print(add(input("first number:"),input("second number:")))
        elif button == "*":
            print(multiply(input("first number:"),input("second number:")))
        elif button == "/":
            print(divide(input("first number:"),input("second number:")))
        elif button.upper() == "CM":
            print(CMtoM((input("number of cm:"))))
        elif button.upper() == "F":
            print(MtoFEET((input("number of m:"))))
        elif button == "x":
            print("exiting ...")
            calculate = False
        else:
            print("not a button")

calculator()