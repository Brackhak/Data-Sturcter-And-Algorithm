class Node :
    def __init__ (self,data) :
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self) :
        return self.data

class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def __str__(self) :
        if self.head == None :
            return "Empty"
        else :
            cur , s = self.head , str(self.head) + ' '
            while cur.next != None :
                s += str(cur.next.data) + ' '
                cur = cur.next
            return s

    def append(self,data) :
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
        else :
            t = self.head  
            while t.next != None :
                t = t.next
            t.next = new_node
        return self.head

def sorting(link_head) :
    link_number_0 = LinkedList()
    link_number_1 = LinkedList()
    link_number_2 = LinkedList()
    link_number_3 = LinkedList()
    link_number_4 = LinkedList()
    link_number_5 = LinkedList()
    link_number_6 = LinkedList()
    link_number_7 = LinkedList()
    link_number_8 = LinkedList()
    link_number_9 = LinkedList()
    rount = 0
    

inp = input("Enter Input : ").split(' ')
link = LinkedList()
for i in inp :
    link.append(i)
print(link)

    