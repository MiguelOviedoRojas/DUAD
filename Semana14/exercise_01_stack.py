class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        if self.head.next is not None:
            current_node = self.head

            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
        else:
            print("No hay elementos en el Stack")
        
    
    def push(self, new_node):
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head.next is not None:
            self.head = self.head.next






first_node = Node("Primero en Entrar")
second_node = Node("Segundo en Entrar")
third_node = Node("Tercero en Entrar")
structure = Stack(first_node)

structure.push(second_node)

structure.print_structure()

structure.push(third_node)

structure.print_structure()

structure.pop()

structure.print_structure()
structure.pop()

structure.print_structure()
structure.pop()

structure.print_structure()
structure.pop()
structure.pop()
structure.pop()
