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
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        print(prev_node.next)

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
    
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = next
                return
            
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
            
            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def len_of_linked_list_using_iterative_method(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def len_of_linked_list_using_recursive_method(self, node):
        if node is None:
            return 0
        return 1 + self.len_of_linked_list_using_recursive_method(node.next)


node = LinkedList()
node.append("A")
node.append("B")
node.append("C")
node.append("D")
node.append("E")
# print(node.insert_after_node(node.head.next, "M"))
# print(node.delete_node("M"))
# print(node.print_list())
# print(node.print_list())
# node.delete_node_at_pos(0)
# print(node.print_list())
print(node.len_of_linked_list_using_iterative_method())
print(node.len_of_linked_list_using_recursive_method(node.head))
    