class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to queue")

    # Dequeue operation
    def dequeue(self):
        if not self.queue:
            print("Queue Underflow! Cannot dequeue.")
        else:
            print(f"Dequeued element: {self.queue.pop(0)}")

    # Front operation
    def front(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print(f"Front element: {self.queue[0]}")

    # Rear operation
    def rear(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print(f"Rear element: {self.queue[-1]}")

    # Display operation
    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)


# Driver code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.front()
q.rear()
q.dequeue()
q.display()
