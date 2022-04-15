class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.preview = None
class LinkedList:
    def __init__(self):
        k = Node('|')
        self.head = k
        self.tail = k
    
    def addWord(self,data):
        P = self.head
        while P.data != '|':
            P = P.next
        i = Node(data)
        if P.preview == None and P.data == '|':
            i.next = P
            self.head = i
            P.preview = i
            
        elif P.preview != None and P.data == '|':
            i.next = P
            i.preview = P.preview
            P.preview.next = i
            P.preview = i
           
            

    def __str__(self):
        P = self.head
        s = str(self.head.data)
        P = P.next
        while P is not None:
            s += " "+str(P.data)
            P = P.next
        return s



    def Left(self):
        P = self.head
        while P.data != '|':
            P = P.next
        if P.preview is not None:
            J = P.preview #1
            J.next = P.next
            Z = J.preview #2
            if Z is not None:
                Z.next = P
                P.preview = Z
            else:
                self.head = P
                P.preview = None

            P.next = J
            J.preview = P
        if self.tail is P:
            self.tail = P

    def Right(self):
        P = self.head
        while P.data != '|':
            P = P.next
        if P.next is not None:
            Z = P.preview #1
            K = P.next #3
            if Z is not None:
                K.preview = Z
                Z.next = K
            else:
                K.preview = None
                self.head = K
            P.next = K.next
            K.next = P
            P.preview = K
        if P.next is None:
            self.tail = P
    
    def RemoveBack(self):
        P = self.head
        while P.data != '|':
            P = P.next
        if P.preview is not None:
            j = P.preview 
            k = j.preview 
            if k is not None:
                k.next = P
                P.preview = k
            else:
                self.head = P
                P.preview = None
        
    def Delete(self):
        P = self.head
        while P.data != '|':
            P = P.next
        if P.next is not None:
            j = P.next 
            k = j.next 
            if k is not None:
                P.next = k
                k.preview = P
            else:
                P.next = None
                self.tail = P


            

    def isEmpty(self):
        return self.head == None
    def size(self):
        P = self.head
        si = 0
        while P is not None:
            si+=1
            P=P.next
        return si

In = input('Enter Input : ').split(',')
lk = LinkedList()
for a in In:
    l = a.strip().split()
    if l[0] == 'I':
        lk.addWord(l[1])
    elif l[0] == 'L':
        lk.Left()
    elif l[0] == 'R':
        lk.Right()
    elif l[0] == 'B':
        lk.RemoveBack()
    elif l[0] == 'D':
        lk.Delete()
print(lk)
