class Stack:

    def __init__(self):

        self.Stack = []
        self.size = int(input("Enter Size of Stack : "))
        self.top = len(self.Stack)
        # self.top = print(type(len(self.Stack)))

    def push(self):
        if len(self.Stack) >= self.size:
            print("Stack Overflow..")

        else:
            self.userData = input("Enter Value :  ")
            self.Stack.append(self.userData)
            self.display()




    def pop(self):
        if len(self.Stack) <= 0:
            print ("Stack Underflow : No element in the Stack")
        else:
            print(self.Stack.pop())
            self.display()

    def display(self):

         for i in reversed(self.Stack):

             print(i)


print("""
*****************Select Operation*****************
                    1. Push
                    2. Pop
                    3. Exit

""")

element = Stack()


while True:

    userChoice = int(input("Enter your operation no.:  "))

    if userChoice  == 1:

        element.push()

    elif userChoice == 2:
        element.pop()

    elif userChoice == 3:
        break

    else :
        print("\nEnter a valid choice...")




