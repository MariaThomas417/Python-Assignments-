from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
        else:
            removed = self.queue.popleft()
            print(removed, "removed from queue")

    def display(self):
        print("Current Queue:", list(self.queue))


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.safe_dequeue()
q.safe_dequeue()
q.safe_dequeue()
q.safe_dequeue()   