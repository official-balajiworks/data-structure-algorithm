class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    # Pop operation
    def pop(self):
        if not self.stack:
            print("Stack Underflow! Cannot pop.")
        else:
            print(f"Popped element: {self.stack.pop()}")

    # Peek operation
    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(f"Top element: {self.stack[-1]}")

    # Display operation
    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)


# Driver code
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
