# tech201_functions
tech201_functions

## Functions
Remember -
- D R Y

- Don't Repeat Yourself

## Creating a function

First we need to write def to define our function, then we name it and finish with open brackets,
by default this just returns whatever is in the indented code block. for example this will print the line stated when the function is called.
```
def print_something():
    print("Something has been printed") #Something has been printed #Something has been printed
```
    
Remember we have to call the function when we want to use it, in this case the function accepts no arguments so it is called how it is written.

`print_something()` #Something has been printed

In this case we have put an argument in the brackets, print_string must be defined elsewhere for this to work.

```
def print_something(print_string):
    print(print_string)
```

Here we can just write our string into the brackets and our function will accept it as an argument.

`print_something("this is my variable")`

This function can be called as many times as we want to.

`print_something("second time")`

In java and other programming languages we would have to add additional information such as public and void for this to work, however not in python, due to it's simplicity of use.

`public void print_string(string_text)`

Here we have an f string within our function that prints.

```
 def greetings(name):
     print(f"Hello, my name is {name}")
```

The string , James is accapted as a name and printed along with the rest of the string
```
 greetings("James") #Hello my name is James
```

### The Return statement
The return statement is useful to return data from a function to somewhere else in the code.
The following function will return the sum of the two arguments, note this does not print it out which must be stated elsewhere.

```
 def addition(int1,int2):
     return int1 + int2
```

These two integers should return their sum

```
 print(addition(1,1)) #2
```

Here we can put default integers into our code so that if no arguments are made, our function will run with the defaults.


```
 def addition(int1=2, int2=2):
     return int1 + int2
```

The following code block should demonstrate this with empty functions printing the default values.


```
 print(addition()) #4
 print(addition(10, 10)) #20
```

### Mutliple arguments

If we want to introduce an unknown number of arguments to our function we can specify this.
The code needs a * infront of arg to turn args into tuple.

```
 def multi_args(*multiargs):
     print(type(multiargs))
     for arg in multiargs:
         print(arg)
```
By writing a for loop inside of our function it will simply go through the tuple and run the indented code until the program reaches the end of the tuple.
```
 multi_args(1, 2, 3, 4) #tuple 1 2 3 4
```
Remember that the type of data is also important when concantination and running other code within our function.
```
 def greeting(name):
     print("Hello my name is: " + name)
```
This following code will not run correctly
```
 greeting(24601) # can only concatenate str (not "int") to str
```

In the following code we will now specify what data type we want to get the intended result

```
 def division(num1: int = 5, num2: int = 2) -> float:
     return num1 / num2
```
This should work since both are floats
```
 print(division()) #2.5
```

Function best practices

- Name your functions clearly using lower case and underscores
- All arguments should be clear in their need and where possible and include their expected type
- remember the return statement or your function will return none
- keep functions small to preserve readility and simplicity
- use comments in your functions/methods to give instructions on how to use them
- consider using type hints to avoid type errors when you run your code

## Calculator Walkthrough
```
def add(num1, num2):
    return(num1 + num2)
```

```
def subtract(num1, num2):
    return(num1 - num2)
```
```
def multiply(num1, num2):
    return(num1 * num2)
```

```
def divide(num1, num2):
    return(num1/num2)
```

```
def CMtoM(num1):
    return(num1/100)
```

```
def MtoFEET(num1):
    return(round((num1*3.2808399),2))
```

```
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
```
