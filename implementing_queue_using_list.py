class Queue:
    def __init__(self, q_size):
        self.arr = [0] * q_size
        self.size = 0
        self.capacity = q_size
        self.front = 0

    # Function to add an element to queue
    def enqueue(self, x):

        # If queue is full
        if self.size == self.capacity:
            print("Queue is Full")
            return

        self.arr[self.size] = x

        # Increment queue size
        self.size += 1

        print(x, "added to the queue")

    # Function to remove front element from queue
    def dequeue(self):

        # If queue is empty
        if self.size == 0:
            print("Queue is Empty")
            return

        # Store the element being removed
        removed = self.arr[0]

        # Shift all the elements to the left
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]

        # Decrement queue size
        self.size -= 1

        print(removed, "removed from the queue")

    # Function which returns the front element
    def getFront(self):

        # If queue is empty
        if self.size == 0:
            print("Queue is Empty")
            return -1

        return self.arr[self.front]

    # Function which prints the elements of array
    def display(self):

        if self.size == 0:
            print("Queue is Empty")
            return

        print("Queue:", end=" ")

        for i in range(self.front, self.size):
            print(self.arr[i], end=" ")

        print()


# Creating queue
q_size = int(input("Enter the size of the queue: "))
q = Queue(q_size)


# Menu-driven program
while True:

    print("\n--- Queue Operations ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Get Front")
    print("4. Display Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter element to add: "))
        q.enqueue(x)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        front_element = q.getFront()

        if front_element != -1:
            print("Front element:", front_element)

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
