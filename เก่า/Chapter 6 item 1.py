    class Node:
    def __init__(self, value, next = None):
        self.value = value
        if next == None:
            self.next = None
        else:
            self.next = next
    def getData(self):
        return self.value
    def getNext(self):
        return self.next
    def setData(self,value):
        self.value = value
    def setNext(self,next):
        self.next = next
    def __str__(self):
        return self.value



class LinkedList:
    def __init__(self):
        self.head = None
        self.sizeList = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        P = Node(item)
        if self.head is None:
            self.head = P
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = P
        self.sizeList += 1

    def addHead(self, item):
        if(self.head is None):
            self.head = Node(item)
        else:
            P = self.head
            self.head = Node(item,P)
        self.sizeList += 1

    def search(self, item):
        P = self.head
        Check = False
        while P is not None:
            if P.value == item:
                Check = True
                return "Found"
                break
            P = P.next
        if Check == False:
            return "Not Found"
        
    def index(self, item):
        P = self.head
        Check = False
        index = 0
        while P is not None:
            if P.value == item:
                Check = True
                return int(index)
                break
            else:
                P = P.next
                index += 1
        if Check == False:
            return -1
    
    def size(self):
        return self.sizeList

    def pop(self, pos):
        P = self.head
        if P is None:
            return "Out of Range"
        if pos < self.sizeList and pos != 0:
            for j in range(pos-1):
                P = P.next
            if P.next is not None:
                i = P.next
                P.setNext(i.next)
            else:
                P.setNext(None)
            self.sizeList -= 1
            return "Success"
        elif pos < self.sizeList and pos == 0:
            self.head = None
            self.sizeList -= 1
            return "Success"
        elif pos > self.sizeList:
            return "Out of Range"



L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
lstr = 'AP KMITL'