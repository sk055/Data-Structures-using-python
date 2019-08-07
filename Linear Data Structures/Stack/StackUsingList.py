print("""
*****************Select Operation*****************
                    1. Push
                    2. Pop
                    3. Exit

""")

Stack = []

while True:

    userChoice = int(input("Enter your operation no.:  "))

    if userChoice == 1:
        userData = input("Enter Value :  ")
        Stack.append(userData)

        for i in reversed(Stack):
            print(i)

    elif userChoice == 2:
        print(Stack.pop())


    elif userChoice == 3:
        break

    else :
        print("\nEnter a valid choice...")
