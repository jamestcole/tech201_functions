def add(num1, num2):
    return(num1 + num2)

def subtract(num1, num2):
    return(num1 - num2)

def multiply(num1, num2):
    return(num1 * num2)

def divide(num1, num2):
    return(num1/num2)

def CMtoM(num1):
    return(num1/100)

def MtoFEET(num1):
    return(round((num1*3.2808399),2))

def calculator():
    calculate = True
    while calculate:
        button = input("press calculator button here (+,-,*,/,(CM for m from cm),(F for feet from m),(x for exit)):")
        if button == "-":
            print(subtract(int((input("first number:"))),int((input("second number:")))))
        elif button == "+":
            print(add(int((input("first number:"))),int((input("second number:")))))
        elif button == "*":
            print(multiply(int((input("first number:"))),int((input("second number:")))))
        elif button == "/":
            print(divide(int((input("first number:"))),int((input("second number:")))))
        elif button.upper() == "CM":
            print(CMtoM(int(input("number of cm:"))))
        elif button.upper() == "F":
            print(MtoFEET(int(input("number of m:"))))
        elif button == "x":
            print("exiting ...")
            calculate = False
        else:
            print("not a button")

calculator()