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

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next_right
            
    
    def pop_left(self):
        if self.head:
            self.head = self.head.next_right
            
    
    def pop_right(self):
        if self.head:
            current_node = self.head
            last_node = Node

            while current_node.next_right is not None:
                last_node = current_node
                current_node = current_node.next_right
            
            last_node.next_right = None
            current_node.next_left = None


    def push_right(self, new_node):
        current_node = self.head

        while current_node.next_right is not None:
            current_node = current_node.next_right
        
        current_node.next_right = new_node
        new_node.next_left = current_node
        new_node.next_right = None
    

    def push_left(self, new_node):
        if self.head:
            new_node.next_right = self.head
            new_node.next_left = None
            self.head = new_node

'''
print("Insert Head")
first_node = Node("Soy el primero")
print("Insert Second Node")
second_node = Node("Soy el segundo")
structure = DoubleEndedQueue(first_node)
structure.push_right(second_node)
print("Insert Third Node at the End")
third_node = Node("Soy el tercero")
structure.push_right(third_node)
print("Print 1 - 2 - 3")
structure.print_structure()
print("Insert New Head")
forth_node = Node("Soy el cuarto")
structure.push_left(forth_node)
print("Print 4- 1 - 2 - 3 with a New Head")
structure.print_structure()
fifth_node = Node("Soy el Quinto")
print("Insert New Head")
structure.push_left(fifth_node)
print("Print 5 - 4- 1 - 2 - 3 with a New Head")
structure.print_structure()
print("Pop head")
structure.pop_left()
print("Print 4- 1 - 2 - 3 with a New Head")
structure.print_structure()
print("Pop Right")
structure.pop_right()
print("Print 4- 1 - 2")
structure.print_structure()
six_node = Node("Soy el Sexto")
structure.push_right(six_node)
print("Print 4- 1 - 2 - 6")
structure.print_structure()
structure.pop_right()
structure.pop_right()
structure.pop_right()
structure.pop_right()
structure.pop_right()

structure.print_structure()
structure.pop_left()

structure.print_structure()
structure.pop_right()
structure.pop_left()
'''