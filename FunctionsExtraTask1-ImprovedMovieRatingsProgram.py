def MovieRatings():
    admitting = True
    u = "universal"
    plus12 = "12 and 12a"
    plus15 = "15"
    plus18 = "18"
    while admitting:
        age = input("What is your age?")
        if age.isdigit() and int(age) <118 and int(age) > 0:
            if int(age) < 12:
                print(f"you can watch {u} rated movies only")
            elif int(age) >= 12 and int(age) < 15:
                print(f"you can watch {u} and {plus12} rated movies")
            elif int(age) >= 15 and int(age) < 18:
                print(f"you can watch {u}, {plus12} and {plus15} rated movies")
            elif int(age) >= 18:
                print(f"you can watch {u}, {plus12}, {plus15} and {plus18}rated movies")
        else:
            print("Please provide your answer in digits and below 118 and above 0")
        x = input("press x to quit or c to continue")
        if x == "x":
            admitting = False
        else:
            continue

MovieRatings()