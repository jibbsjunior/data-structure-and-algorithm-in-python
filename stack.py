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
    