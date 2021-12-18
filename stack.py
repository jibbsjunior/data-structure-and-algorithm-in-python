class Stack:
    def __init__(self):
        self.items = []
        pass

    def push(self, item):
        self.items.append(item)
        pass

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

stack = Stack()
# stack.push("Ajibola")
# stack.push("Adebayo")
# print(stack.get_stack())
# stack.push("Rilwan")
# print(stack.get_stack())
# stack.pop()
# print(stack.get_stack())
print(stack.is_empty())
print(stack.peek())
    