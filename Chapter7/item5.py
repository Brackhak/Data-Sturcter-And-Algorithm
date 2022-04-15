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
        self.count = 0

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
        if level > self.count :
            self.count = level
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,check,check_level = 1):
        while self.root.left != None or self.root.right != None :
            if check == self.root.data :
                if check_level == 1 :
                    return "Root"
                elif check_level < self.count :
                    return "Inner"
            if check < self.root.data and self.root.left is not None :
                self.root = self.root.left
                if check == self.root.data and check_level == self.count :
                    return "Leaf"
            elif check >= self.root.data and self.root.right is not None : 
                self.root = self.root.right
                if check == self.root.data and check_level == self.count-1 :
                    return "Leaf"
            check_level += 1
        return "Not exist"

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(inp[0]))
#print(T.count)