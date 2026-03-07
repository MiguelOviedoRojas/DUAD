class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def print_structure(self):
        if self.head is not None:
            current_node = self.head

            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
        else:
            print("Stack doesn't have Elements")
        
    def push(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Stack doesn't have Elements")



structure = Stack()
structure.pop()
first_node = Node("Primero en Entrar")
structure.push(first_node)
second_node = Node("Segundo en Entrar")
structure.push(second_node)
third_node = Node("Tercero en Entrar")
structure.push(third_node)
structure.print_structure()
structure.pop()
structure.print_structure()