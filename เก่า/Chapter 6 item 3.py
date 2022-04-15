class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.preview = None
class LinkedList:
    def __init__(self):
         self.head = None
         self.tail = None
    def isEmpty(self):
        return self.head == None
    def addHead(self,data):
        i = Node(data)
        if self.isEmpty():
            self.head = i
            self.tail = i
        else:
            P = self.head
            P.preview = i
            i.next = P
            self.head = i
    def append(self,data):
        i = Node(data)
        if self.isEmpty():
            self.addHead(data)
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = i
            i.preview = p
            self.tail = i
    def __str__(self):
        s = str(self.head.data)
        P = self.head
        P = P.next
        while P is not None:
            s += " " + str(P.data) 
            P = P.next
        return s
    def reverse(self):
        s = str(self.tail.data)
        P = self.tail
        P = P.preview
        while P is not None:
            s += " " + str(P.data) 
            P = P.preview
        return s

I = input('Enter Input (L1,L2) : ').split(' ')
l1 = LinkedList()
l2 = LinkedList()
w = I[0].split('->')
for k in w:
    l1.append(k)
z = I[1].split('->')
for j in z:
    l2.append(j)
ll =LinkedList()
ll.append(l1)
ll.append(l2.reverse())
print('L1    : {0}'.format(l1))
print('L2    : {0}'.format(l2))
print('Merge : {0}'.format(ll))          