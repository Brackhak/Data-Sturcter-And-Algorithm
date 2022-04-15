class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None :
            self.root = Node(data)
        else :
            root_t = self.root
            if data < root_t.data :
                if root_t.left is None :
                    root_t.left = Node(data)
                else :
                    while root_t.left != None or root_t.right != None :
                        if data < root_t.data :
                            if root_t.left is not None :
                                root_t = root_t.left
                            else :
                                root_t.left = Node(data)
                                return self.root
                        else :
                            if root_t.right is not None :
                                root_t = root_t.right
                            else :
                                root_t.right = Node(data)
                                return self.root
                    if data < root_t.data :
                        root_t.left = Node(data)
                    else :
                        root_t.right = Node(data)
            else :
                if root_t.right is None :
                    root_t.right = Node(data)
                else :
                    while root_t.left != None or root_t.right != None :
                        if data < root_t.data :
                            if root_t.left is not None :
                                root_t = root_t.left
                            else :
                                root_t.left = Node(data)
                                return self.root
                        else :
                            if root_t.right is not None :
                                root_t = root_t.right
                            else :
                                root_t.right = Node(data)
                                return self.root
                    if data < root_t.data :
                        root_t.left = Node(data)
                    else :
                        root_t.right = Node(data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def serch_tree(self,node):
        print("--------------------------------------------------")
        node_min = node
        while node_min.left != None :
            node_min = node_min.left
        print("Min :",node_min.data)
        node_max = node
        while node_max.right != None :
            node_max = node_max.right
        print("Max :",node_max.data)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
T.serch_tree(root)
