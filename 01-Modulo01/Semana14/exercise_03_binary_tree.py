class Node:
    data: int
    left_son: int
    right_son: int

    def __init__(self, data):
        self.data = data
        self.left_son = None
        self.right_son = None


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root
    
    def insert_node(self, new_node):
        
        if self.root is None:
            self.root = Node(new_node)
        else:
            self.recursive_insert(self.root, new_node)

    def recursive_insert(self, current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left_son is None:
                current_node.left_son = new_node
            else:
                self.recursive_insert(current_node.left_son, new_node)
        elif new_node.data > current_node.data:
            if current_node.right_son is None:
                current_node.right_son = new_node
            else:
                self.recursive_insert(current_node.right_son, new_node)

    def print_structure(self):
        if self.root is None:
            print("Structure Doesn't Have Data")
        else:
            self.print_in_order(self.root)
    
    def print_in_order(self, current_node):
        if current_node is None:
            return
        self.print_in_order(current_node.left_son)
        print(current_node.data)
        self.print_in_order(current_node.right_son)
            




first_node = Node(20)
structure = BinaryTree(first_node)
second_node = Node(15)
structure.insert_node(second_node)
third_node = Node(30)
structure.insert_node(third_node)
forth_node = Node(18)
structure.insert_node(forth_node)
fifth_node = Node(29)
structure.insert_node(fifth_node)
structure.print_structure()