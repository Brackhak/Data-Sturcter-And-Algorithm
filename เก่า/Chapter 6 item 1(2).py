class Node:
    def __init__(self, value ,next =None):
        self.value = value
        self.next = next
        
   

class LinkedList:
    def __init__(self):
        self.head = None
        self.sizelist = 0

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
        p = Node(item)
        if self.head == None :
            self.head = p
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = p
        self.sizelist += 1

    def addHead(self,item) :
        if self.head == None :
            self.head = Node(item)
        else :
            p = self.head
            self.head = Node(item,p)
        self.sizelist += 1

    def search(self,item) :
        p = self.head
        check_stat = False
        while p is not None :
            if p.value == item :
                return "Found"
                check_stat = True
                break
            p = p.next
        if check_stat == False :
            return "Not Found"

    def size(self) :
        return self.sizelist
    
    def index(self,item) :
        count = 0
        if self.head == None :
            return "-1"
        else :
            p = self.head
            while p is not None :
                if p.value == item :
                    break
                else :
                    count += 1
                p = p.next
            return str(count)
    
    def pop(self,item) :
        if self.head == None :
            return "Out of Range"
        else :
            p = self.head
            while p.next is not None :
                if p.value == item :
                    
                

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:] , L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)