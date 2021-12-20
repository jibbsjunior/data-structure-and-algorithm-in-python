class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        pass

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        pass

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    