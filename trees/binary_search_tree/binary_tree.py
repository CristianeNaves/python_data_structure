class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

class BinaryTree(Tree):
    def insert(self, new_node, current_node=None):
        if self.root is None:
            self.root = new_node
            return new_node
        
        if current_node is None:
            current_node = self.root
        
        if new_node.data < current_node.data:
            if current_node.left:
                return self.insert(new_node, current_node.left)
            current_node.left = new_node
        elif new_node.data > current_node.data:
            if current_node.right:
                return self.insert(new_node, current_node.right)
            current_node.right = new_node
    
    def inorderTraversal(self, node=None):
        if node is None:
            node = self.root
        left_list = []
        right_list = []
        if node.left:
            left_list = self.inorderTraversal(node.left)
        if node.right:
            right_list = self.inorderTraversal(node.right)
        return left_list + [node.data] + right_list

if __name__ == "__main__":
    tree = BinaryTree()
    node0 = Node(5)
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(10)

    tree.insert(node0)
    tree.insert(node1)
    tree.insert(node2)
    tree.insert(node3)

    l = tree.inorderTraversal()
    print(l)