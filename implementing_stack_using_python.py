
class stack:
    # Method for pushing data into stack
    def push(self, st, data):
        st.append(data)

    # Method for pop
    def pop(self, st):
        if len(st) > 0:
            ans = st.pop()
            print("Removed element from the stack:", ans)
        else:
            print("The stack is Empty")

    # Method to get top of stack
    def top(self, st):
        if len(st) > 0:
            return st[len(st) - 1]
        else:
            print("The stack is Empty")

    # Method to check stack is Empty or not
    def isEmpty(self, st):
        if len(st) == 0:
            return 1
        else:
            return 0

    # Method to get size of stack
    def size(self, st):
        return len(st)


# Creating object of stack class
st = stack()

# Creating an empty stack
s = []

while True:
    print("\n--- Stack Operations ---")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Check if Empty")
    print("5. Size")
    print("6. Display Stack")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter element to push: ")
        st.push(s, data)
        print("Element pushed successfully.")

    elif choice == 2:
        st.pop(s)

    elif choice == 3:
        ans = st.top(s)
        if ans is not None:
            print("Top element in the stack:", ans)

    elif choice == 4:
        if st.isEmpty(s):
            print("The stack is Empty")
        else:
            print("The stack is not Empty")

    elif choice == 5:
        print("Size of stack:", st.size(s))

    elif choice == 6:
        print("Stack:", s)

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
