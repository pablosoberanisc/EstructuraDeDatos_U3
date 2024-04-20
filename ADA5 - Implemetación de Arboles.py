class Node:
    def __init__(self, value=None, parent=None, is_root=False, is_left=False, is_right=False):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.is_root = is_root
        self.is_left = is_left
        self.is_right = is_right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def add(self, value):
        if self.empty():
            self.root = Node(value=value, is_root=True)
        else:
            node = self.get_place(value)
            if value <= node.value:
                node.left = Node(value=value, parent=node, is_left=True)
            else:
                node.right = Node(value=value, parent=node, is_right=True)

    def get_place(self, value):
        aux = self.root
        while aux:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp

    def show_inorder(self, node):
        if node is not None:
            self.show_inorder(node.left)
            print(node.value, end=" ")
            self.show_inorder(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(1)
    bst.add(4)

    print("Orden del árbol:")
    bst.show_inorder(bst.root)