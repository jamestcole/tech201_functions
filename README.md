# tech201_functions
tech201_functions

## Functions

- D R Y

- Don't Repeat Yourself

## Creating a function
```
def print_something():
    print("Something has been printed")
```

`print_something()`

 def print_something(print_string):
     print(print_string)

 print_something("this is my variable")

 print_something("second time")

in java
public void print_string(string_text)

 def greetings(name):
     print(f"Hello, my name is {name}")

 greetings("James")

 The Return statement

 def addition(int1,int2):
     return int1 + int2

 print(addition(1,1))

 def addition(int1=2, int2=2):
     return int1 + int2

 print(addition())
 print(addition(10, 10))
 print(addition())

mutliple arguments
needs * infront of arg to turn args into tuple

 def multi_args(*multiargs):
     print(type(multiargs))

     for arg in multiargs:
         print(arg)

 multi_args(1, 2, 3, 4)

 def greeting(name):
     print("Hello my name is: " + name)

 greeting(24601)


 def division(num1: int = 5, num2: int = 2) -> float:
     return num1 / num2

 print(division())

Function best practices

Nam your functions clearly using lower case and underscores
All arguments should be clear in their need and where possible and include their expected type
remember the return statement or your function will return none
keep functions small to preserve readility and simplicity
use comments in your functions/methods to give instructions on how to use them
consider using type hints to avoid type errors when you run your code

