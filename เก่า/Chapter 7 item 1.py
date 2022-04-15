class Node:
    def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = None 
      self.right = None 
      
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
      self.root = None

    def insert(self, data):
      if self.root is None:
        self.root = Node(data)
      else:
        fp = None
        p = self.root
        while p:
          fp = p
          if data < p.data:
            p = p.left
          else:
            p = p.right

        if data < fp.data:
          fp.left = Node(data)
        else:
          fp.right  = Node(data)
      return self.root

    def printTree(self, node, level = 0):
      if node is not None:
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
  root = T.insert(i)
T.printTree(root)