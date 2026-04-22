class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed to stack")

    def safe_pop(self):
        if len(self.items) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.items.pop()

    def display(self):
        print("Stack:", self.items)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())   