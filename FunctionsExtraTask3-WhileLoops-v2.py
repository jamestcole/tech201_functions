# Task 4 while loops
#Take 10 integers from the user and print their average value once you have them all

def AverageOfTen():
    number1 = 0
    totnum1 = 0
    print("I will ask you for ten numbers and return the average")
    while number1 <10:
        n = int(input("give me a number:"))
        number1 += 1
        totnum1 += n
    print("the average value of your numbers is: ", totnum1/10)

#Program number 2
#write a loop to print the following series
serinum = 10
while serinum <301:

    print(serinum)
    serinum += 10

#Additional program 2
print("this program will take every number that you enter, until you enter 0")
print("It will then seperate te them into positive and negative numbers")
negative_nums = []
positive_nums = []
program = True
while program:
    n = int(input("add a number: "))
    if n == 0:
        program = False
    elif n > 0:
        positive_nums.append(n)
    elif n < 0:
        negative_nums.append(n)
    else:
        print("that doesn't seem to be valid")
print("The positive numbers are :")
for n in positive_nums:
    print(n)
print("The negative numbers are :")
for n in negative_nums:
    print(n)