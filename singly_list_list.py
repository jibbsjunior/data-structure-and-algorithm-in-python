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
    
    def node_swap(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1, curr_1 = None, self.head
        #check is both the previous node found and curr1.data are not equals to key_1
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2, curr_2 = None, self.head
        #check if both the previous node found and curr2.data are not equals to key_2
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        #check if there's no curr_2 or curr_1 so far and break the function
        if not curr_2 or not curr_1:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
            
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative_method(self):
        prev, cur, = None, self.head
        while cur:
            nxt = cur.next
            # print(nxt)
            cur.next = prev
            # print(cur.next)
            prev, cur = cur, nxt
            # print(prev, cur)
        self.head = prev

    def reverse_recursive_method(self):

        def _recusive_helper_method(cur, prev):
            if not cur:
                return prev

            nxt, cur.next = cur.next, prev
            prev, cur = cur, nxt
            return _recusive_helper_method(cur, prev)

        self.head = _recusive_helper_method(self.head, None)

    def merged_two_sorted_linked_list(self, llist): #Algorithm To solve this problem, we’ll use two pointers (p and q) which will each initially point to the head node of each linked list. There will be another pointer, s, that will point to the smaller value of data of the nodes that p and q are pointing to. Once s points to the smaller value of the data of nodes that p and q point to, p or q will move on to the next node in their respective linked list. If s and p point to the same node, p moves forward; otherwise q moves forward. The final merged linked list will be made from the nodes that s keeps pointing to. 
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q is not None: #this line can also be written like this - while p and q
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q

        if not q:
            s.next = p
        
        self.head = new_head
        return self.head

    def remove_duplicates(self): #Algorithm - The general approach to solve this problem is to loop through the linked list once and keep track of all the data held at each of the nodes. We can use a hash table or Python dictionary to keep track of the data elements that we encounter. For example, if we encounter 6, we will add that to the dictionary or hash table and move along. Now if we meet another 6 and we check for it in our dictionary or hash table, then we’ll know that we already have a 6 and the current node is a duplicate.
        cur = self.head
        prev = None
        duplicate_values = dict()

        while cur:
            if cur.data in duplicate_values:
                #If the above condition is true then the current element already exist then we need to remove it because it is a duplicate
                prev.next = cur.next
                cur.next = None
            else:
                #Then we have not encountered the element before
                duplicate_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_to_last(self, n):
        total_len = self.len_of_linked_list_using_iterative_method()
        cur = self.head

        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return




newll = LinkedList()
# node = LinkedList()
# node2 = LinkedList()
# node.append(1)
# node.append(3)
# node.append(5)
# node.append(7)
# node.append(9)
# node2.append(2)
# node2.append(4)
# node2.append(6)
# node2.append(8)
# node2.append(10)
newll.append(1)
newll.append(2)
newll.append(3)
newll.append(2)
newll.append(1)
newll.append(4)
# node.merged_two_sorted_linked_list(node2)
print("Original Linked list: {}\n".format(newll.print_list()))
newll.remove_duplicates()
print("New linked list after removing duplicates: {}\n".format(newll.print_list()))
# print(node.insert_after_node(node.head.next, "M"))
# print(node.delete_node("M"))
# print(node.print_list())
# print(node.print_list())
# node.delete_node_at_pos(0)
# print(node.print_list())
# print(node.len_of_linked_list_using_iterative_method())
# print(node.len_of_linked_list_using_recursive_method(node.head))
# print(node.node_swap("A", "B"))
# print("Swapping node A and B where key_1 is the head node")
# print(node.print_list())
# print(node.node_swap("C", "E"))
# print("Swapping node C and D where there's no head among the 2 node")
# print(node.print_list())
# print(node.node_swap("C", "C"))
# print("Swapping key C and C where both keys are the same")
# print(node.print_list())
# node.node_swap("E", "A")
# print("Swapping key E and A where key A is the head node")
# print(node.print_list())
# node.reverse_iterative_method()
# node.reverse_recursive_method()
# print(node.print_list())
# def func():
#     x = 50
#     print(x)

# func()
# print(x)
# x = ['ab', 'bs']
# print(list(map(len, x)))
# print(list(map(len(x), x)))
# print(list(map(x.len), x))
# print(list(map(lambda x:len(x), x)))
# print(2**(3**2), (2**3)**2, (2**3)**3)
# list1 = [1,2,3,4,5]
# list2 = [5,4,3,2,1]
# print(list1 == list2)
# print(set(list1) == set(list2))
# l = [12,3,4,5]
# new = l.copy()
# # newL.copy(l)
# newL = list(l)
# print(newL)
    