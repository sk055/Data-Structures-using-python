import queue

class Queue:

    def __init__(self):

        self.maxsize = int(input("Enter length of queue : "))
        self.queue_1 = queue.Queue(self.maxsize)

    def insert(self):

        if self.queue_1.qsize() >= self.maxsize:
            print("Queue is Overflow..")

        else:

            userData = input("Enter value : ")
            self.queue_1.put(userData)
            self.show()

    def remove(self):
        if self.queue_1.qsize() <=0:
            print("Queue is Empty")

        else:
            print(self.queue_1.get())
            # self.show()

    def show(self):

        for n in list(self.queue_1.queue):
            print(n, end=" ")


print("""
*****************Select Operation*****************
                    1. Insert
                    2. Delete
                    3. Exit

""")

element = Queue()

while True:
    userChoice = int(input("\nEnter your choice : "))

    if userChoice == 1:
        element.insert()

    elif userChoice == 2:
        element.remove()

    elif userChoice == 3:
        break

    else:
        print("Select Proper operation...")