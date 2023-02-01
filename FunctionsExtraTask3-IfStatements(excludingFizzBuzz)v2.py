#write a program that prompts user to enter hours and rate of pay
#take into account 1.5 times overtime over 40 hoursimport random
#Program 1

import random
def PayCalc():
    program = True
    while program:
        print("Hi employee, please enter your work hours and rate of pay")
        hours = (input("please enter your hours here:"))
        pay = (input("please enter your pay here:"))
        gate = True
        while gate:
            if hours.isdigit() and pay.isdigit():
                hours = int(hours)
                pay = int(pay)
                gate = False
            else:
                print("These must be integers")
                hours = (input("please enter your hours here:"))
                pay = (input("please enter your pay here:"))
        if pay > 1000 or pay < 6 or hours > 168 or hours < 1:
            print("impossible, please reenter your details. must be between 6 and 1000 pounds pay, 1 and 168 hours")
        else:
            program = False

    print("Thank you for entering your details ... calculating pay")

    if hours <= 40:
        total = (hours*pay)
    elif hours > 40:
        total = (40*pay) + ((hours-40)*pay*1.5)

    print(f"Your total weekly paycheck is {total} pounds")
    print("END OF PROGRAM")
    quit = input("would you like calculate pay again(y/n)")
    if quit.lower() == "y":
        PayCalc()

#asks the user a number
#if the number is odd print odd, if its even prink even
#Program 2

def Numberisoddoreven():
    number = (input("please enter a number:"))
    gate = True
    while gate:
        if number.isdigit():
            number = int(number)
            gate = False
        else:
            print("that's not an integer")
            number = (input("What is your guess:"))
    if number%2 == 0:
        print("the number is even !")
    if number%2 != 0:
        print("the number is odd !")
    print("END OF PROGRAM")
    quit = input("would you like to check number again(y/n)")
    if quit.lower() == "y":
        Numberisoddoreven()

#write a program that has a number variable assigned between 1-20.
#give user 3 guesses for correct number
# make number random
# clue each time higher or lower
#Program 3


def NumberGuess():
    print("Let's play a guessing game, pick a number between 1 and 20:")
    n = random.randint(1, 21)

    numberguess = 4
    failurecount = 0
    wincount = 0
    while numberguess > 0:
        g1 = (input("What is your guess:"))
        gate = True
        while gate:
            if g1.isdigit():
                g1 = int(g1)
                gate = False
            else:
                print("that's not an integer")
                g1 = (input("What is your guess:"))
        if g1 < 1 or g1 > 20:
            print("That guess is out of range, it must be between 1 and 20")
            print(f"guesses remaining: {numberguess-1}")
        elif g1 == n:
            print(f"That's right it was {n}")
            wincount += 1
            print(f"guesses remaining: {numberguess - 2}")
            print(f"you have won {wincount} times, you have lost {failurecount} times")
            q = input("would you like to play again? (y/n)")
            if q == "y":
                n = random.randint(1, 21)
                numberguess = 4
            else:
                break
        elif g1 > n:
            print("thats too high !")
            print(f"guesses remaining: {numberguess - 2}")
            numberguess -= 1
        elif g1 < n:
            print("that's too low !")
            print(f"guesses remaining: {numberguess - 2}")
            numberguess -= 1
        if numberguess == 1:
            print("you failed")
            failurecount += 1
            print(f"you have won {wincount} times, you have lost {failurecount} times")
            q = input("would you like to play again? (y/n)")
            if q == "y":
                n = random.randint(1, 21)
                numberguess = 4
            else:
                break
    print("END OF PROGRAM")

PayCalc()
Numberisoddoreven()
NumberGuess()

