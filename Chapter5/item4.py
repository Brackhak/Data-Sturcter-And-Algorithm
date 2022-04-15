class Node :
    def __init__(self,data,next = None) :
        self.data = data
        if next == None :
            self.next = None
        else : self.next = next
        self.previous = None

    def __str__(self) :
        return self.data

class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.check = False
    
    def __str__(self) :
        if self.head == None :
            return "Empty"
        t = self.head 
        s = str(t.data)
        infi = 0
        while t.next != None and infi != 20:
            infi += 1
            t = t.next
            s += '->'
            s += str(t.data)
        return s

    def reverse(self) :
        if self.tail == None :
            return "Empty"
        h = self.tail
        s = str(h.data)
        while h.previous != None :
            h = h.previous
            s += "<-"
            s += str(h.data)
        return s

    def append(self,data):
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
            self.tail = self.head
        else :
            t = self.head
            while t.next != None:
                t = t.next
            t.next = new_node
            t.next.previous = t
            self.tail = t.next
        t_print = self.head
        print(t_print.data,end='')
        while t_print.next != None :
            t_print = t_print.next
            print("->",end='')
            print(t_print.data,end='')
        print('')
        return self.head
    
    def set_next(self,index1,index2) :
        self.index1 = index1
        self.index2 = index2
        if self.head == None :
            return "Error! {list is empty}"
        t_count = self.head
        count = 0
        while t_count.next != None :
            t_count = t_count.next
            count += 1
        if self.index1 > count :
            return "Error! {index not in length}: " + str(index1)
        elif int(self.index2) > count :
            t_append = self.head
            new_node = Node(index2)
            while t_append.next != None :
                t_append = t_append.next
            t_append.next = new_node
            return "index not in length, append : " + str(index2)
        else :
            if index1 >= int(index2) :
                self.check = True
            count = 0
            t_index1 = self.head
            t_index2 = self.head
            while count != index1 :
                count += 1
                t_index1 = t_index1.next
            count = 0
            while count != int(index2) :
                count += 1
                t_index2 = t_index2.next
            t_index1.next = t_index2
            return "Set node.next complete!, index:value = " + str(index1) + ":" + str(t_index1) + " -> " + str(index2) + ":" +  str(t_index2)

    def Check_loop(self):
        return self.check

inp = input("Enter input : ").split(',')
link = LinkedList()
for i in inp :
    if i[0] == 'A' :
        link.append(i[2:])
    elif i[0] == 'S' :
        print(link.set_next(int(i[2]),i[4]))
if link.Check_loop() :
    print("Found Loop")
else :
    print("No Loop")
    print(link)



