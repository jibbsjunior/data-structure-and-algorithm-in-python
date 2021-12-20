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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

node = LinkedList()
node.append("A")
node.append("B")
node.append("C")
node.append("D")
node.append("E")
print(node.print_list())
    