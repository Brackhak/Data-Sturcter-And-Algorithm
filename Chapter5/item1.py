class Node:
    def __init__(self, value):
        self.value = value
        self.next =None
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None :
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head == None :
            self.head = new_node
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = new_node

    def addHead(self, item):
        t = self.head
        new_node = Node(item)
        if self.head == None :
            self.head = new_node
        else :
            self.head = new_node
            self.head.next = t

    def search(self,item) :
        t = self.head
        if self.head == None :
            return "Not Found"
        while t != None :
            if t.value == str(item) :
                return "Found"
            t = t.next
        return "Not Found"

    def size(self) :
        t = self.head
        count = 0
        while t != None :
            t = t.next
            count += 1
        return count

    def index(self,item) :
        t = self.head
        count = 0
        if self.head == None :
            return -1
        while t != None :
            if t.value == item :
                return str(count)
            count += 1
            t = t.next
        return str(-1)

    def pop(self,pos) :
        t = self.head
        count = 0
        if self.head == None :
            return "Out of Range"
        while t != None :
            if count == pos :
                t.value = ''
                t2 = t
                if count != 0 :
                    while t2.next != None :
                        t2.value = t2.next.value
                        t2.next.value = ''
                        t2 = t2.next
                    return "Success"
                else :
                    self.head = None
                    return "Success"
            count += 1
            t = t.next
        return "Out of Range"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)