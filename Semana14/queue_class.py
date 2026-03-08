class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

# QUEUE: Es una FILA agrega elementos al final de la FILA y quita elementos del inicio de la FILA
class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def enqueue(self, node):
        current_node = self.head

        while(current_node.next is not None):   #Aca validamos que el next del ultimo nodo no sea Null
            current_node = current_node.next

        current_node.next = node

    def dequeue(self):
        if self.head:                   #aca valoramos si el head es null, no hay nada que sacar, porq no hay elementos en la pila - queue
            self.head = self.head.next  #aca el nuevo primero va a ser el segundo, por eso el head va a ser el head.next


first_node = Node("Soy el primero")
second_node = Node("Soy el segundo")
first_node.next = second_node
third_node = Node("Soy el tercero")
second_node.next = third_node

structure = Queue(first_node)
forth_node = Node("Soy el nuevo")
structure.enqueue(forth_node)

structure.print_structure()

# print("DEQUEUE")
# structure.dequeue()
# structure.dequeue()
# structure.dequeue()
# structure.print_structure()


