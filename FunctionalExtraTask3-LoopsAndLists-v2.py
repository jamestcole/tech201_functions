#Task 3 loops and lists
#Program1


def HelloWorldx10():
    count = 0

    while count < 10:
        print("Hello World")
        count += 1
    quit = input("would you like to print again(y/n)")
    if quit.lower() == "y":
        HelloWorldx10()

# Create a loop that iterates over each name in list_name and appends:
# Program 2
def ListIterator():
    count2 = 0
    list_names = []
    list_lower = []
    program = True
    print("This program will accept names for a register, between how many people are you expecting")
    mi = input("The minimum number of people is:")
    ma = input("The maximum number of people is:")
    gate = True
    while gate:
        if mi.isdigit() and ma.isdigit():
            mi = int(mi)
            ma = int(ma)
            gate = False
        else:
            print("These must be integers")
            mi = (input("please enter your hours here:"))
            ma = (input("please enter your pay here:"))
    while program:
        name = input("Give a name")
        list_names.append(name)
        count2 += 1
        if count2 >= ma:
            print("We have the maximum number of people")
            program = False
        if count2 >= mi and count2 < ma:
            q = input("Would you like to continue the register?(y/n)")
            if q.lower() != "y":
                program = False
    print("The following people have been admitted:")
    for name in list_names:
        print(name)
    for name in list_names:
        a = name.lower()
        list_lower.append(a)
    AreTheyEven(count2)
    quit = input("would you like to make another list (y/n)")
    if quit.lower() == "y":
        ListIterator()
    else:
        print("END OF PROGRAM")

#Iterate over teh list of values to find if they are even
def AreTheyEven(count2):
    if count2%2 == 0:
        print("There are an even number of people")
    if count2%2 != 0:
        print("There are an odd number of people")


def Extras():
    print("here are the sum of all number 1 : 100")
    ininum = 1
    totnum = 0
    while ininum < 101:
        totnum += ininum
        ininum += 1
    print(totnum)
    ininum = 1
    totnum = 0
    while ininum < 101:
        if ininum % 2 != 0:
            totnum += ininum
        ininum += 1
    print("the sum of all odd numbers, 1:100 is:",totnum)
    ininum = 1
    totnum = 0
    while ininum < 101:
        if ininum % 2 == 0:
            totnum += ininum
        ininum += 1
    print("the sum of all even numbers, 1:100 is:",totnum)
    print("END OF PROGRAM")

HelloWorldx10()
ListIterator()
Extras()


