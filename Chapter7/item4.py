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
        self.heigth = 0

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
        if node != None :
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preorder(self,node):
        if node != None:
            print(node,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
        
    def inorder(self,node,level = 0):
        if level > self.heigth :
            self.heigth = level
        if node != None :
            self.inorder(node.left , level +1)
            print(node,end=' ')
            self.inorder(node.right , level+1)
            
    def postorder(self,node) :
        if node != None :
            self.postorder(node.left)
            self.postorder(node.right)
            print(node,end=' ')

    def printBreadth(self,root,level) :
        if root is None :
            return 0
        else :
            if level == 1 :
                print(root.data, end= ' ')
            elif level > 1 :
                self.printBreadth(root.left,level - 1)
                self.printBreadth(root.right,level - 1)

    def breadth(self,root) :
        if root == None :
            return 0
        else :
            h = self.heigth
            for i in range(1, h + 1) :
                self.printBreadth(root,i)
    
    

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
#T.printTree(root)
print("Preorder : ",end='')
T.preorder(root)
print("\nInorder : ",end='')
T.inorder(root)
print('\nPostorder : ',end='')
T.postorder(root)
print("\nBreadth : ",end='')
T.breadth(root)
