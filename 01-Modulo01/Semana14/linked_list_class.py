class Node:
    data: str
    next : "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):            
            print(current_node.data)
            current_node = current_node.next


first_node = Node("First Node")
second_node = Node("Second Node")
first_node.next = second_node
third_node = Node("Third Node")
second_node.next = third_node

structure = LinkedList(first_node)
structure.print_structure()
