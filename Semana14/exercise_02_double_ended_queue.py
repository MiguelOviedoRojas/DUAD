class Node:
    data: str
    next_right: "Node"
    next_left: "Node"

    def __init__(self, data):
        self.data = data
        self.next_right = None
        self.next_left = None


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None


    def print_structure(self):
        if self.head:
            current_node = self.head

            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next_right
            
    
    def pop_left(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.data
        else:
            old_head = self.head
            self.head = self.head.next_right
            self.head.next_left = None
            return old_head.data

    def pop_right(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            old_tail = self.tail
            self.head = None
            self.tail = None
            return old_tail.data
        else:
            old_tail = self.tail
            self.tail = self.tail.next_left
            self.tail.next_right = None
            return old_tail.data
    
    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next_right = None
            new_node.next_left = None
        else:
            self.tail.next_right = new_node
            new_node.next_left = self.tail
            new_node.next_right = None
            self.tail = new_node
            
    def push_left(self,new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next_left = None
            new_node.next_right = None
        else:
            self.head.next_left = new_node
            new_node.next_right = self.head
            new_node.next_left = None
            self.head = new_node
            



structure = DoubleEndedQueue()
first_node = Node("First")
structure.push_left(first_node)
second_node = Node("Second")
structure.push_left(second_node)
third_node = Node("Third")
structure.push_right(third_node)
forth_node = Node("Forth")
structure.push_right(forth_node)
fifth_node = Node("Fifth")
structure.push_left(fifth_node)
structure.pop_left()
structure.pop_right()
structure.pop_right()
structure.pop_right()
structure.pop_right()
structure.pop_left()

print("structure.print")
structure.print_structure()


