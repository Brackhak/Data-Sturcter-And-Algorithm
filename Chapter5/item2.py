class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizelist = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head == None :
            self.head = new_node
            self.tail = self.head
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = new_node
            t.next.previous = t
            self.tail = t.next
        self.sizelist += 1

    def addHead(self,item) :
        t = self.head
        new_node = Node(item)
        if self.head == None :
            self.head = new_node
        else :
            self.head = new_node
            self.head.next = t
            t.previous = self.head
        t_new = self.head
        while t_new.next != None :
            t_new = t_new.next
        self.tail = t_new
        self.sizelist += 1

    def pop(self,pos) : 
        count = 0
        if self.head == None :
            return "Out of Range"
        else :
            t = self.head
            while t != None :
                if count == pos :
                    t.value = ''
                    t2 = t
                    if count != 0 :
                        while t2.next != None :
                            t2.value = t2.next.value
                            t2 = t2.next
                            t2.next.previous = t2
                            t.next.previous = t
                        self.sizelist -= 1
                        return "Success"
                    else :
                        self.head = None
                        self.sizelist -= 1
                        return "Success"
                t = t.next
                count += 1
            return "Out of Range"

    def size(self) :
        return int(self.sizelist)

    def insert(self,pos,item) :
        new_node = Node(item)
        t = self.head
        if self.head == None :
            self.head

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
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())