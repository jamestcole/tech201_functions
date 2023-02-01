def FizzBuzz():
    number = 0
    while number < 100:
        number += 1
        if number % 3 == 0 and number % 5 != 0:
            print("fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print("buzz")
        elif number % 5 == 0 and number % 3 == 0:
            print("fizzbuzz")
        else:
            print(number)
    print("END OF PROGRAM")
    quit = input("would you like to go again(y/n)")
    if quit.lower() == "y":
        FizzBuzz()

FizzBuzz()
