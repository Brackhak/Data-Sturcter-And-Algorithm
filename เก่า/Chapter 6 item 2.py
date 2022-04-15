class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.previous = None
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizeList = 0
    
    def __str__(self):
        if self.isEmpty():
            return " "
        else:
            s = str(self.head)
            p = self.head
            while p.next is not None:
                s += '->'+str(p.next.data)
                p = p.next
            return s
    
    def str_reverse(self):
        if self.isEmpty():
            return " "
        else:
            s = str(self.tail)
            p = self.tail
            while p.previous is not None:
                s += '->'+str(p.previous.data)
                p = p.previous
            
            return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        i = Node(data)
        if self.isEmpty():
            self.head = i
            self.tail = i
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = i
            i.previous = p
            self.tail = i
        self.sizeList += 1
    
    def insert(self,index,data):
        i = Node(data)
        p = self.head
        if (index > self.sizeList and index != 0) or index <0:
            print("Data cannot be added")
        elif index < self.sizeList:
            for l in range(index):
                p = p.next
            if p.previous is None:
                self.head = i
                i.next = p
                p.previous = i
            elif p.previous is not None:
                i.next = p
                i.previous = p.previous
                p.previous.next = i
                p.previous = i
               
            self.sizeList += 1
            print("index = {0} and data = {1}".format(index,data))
        elif index == 0 and self.sizeList == 0:
            self.head = i
            self.tail = i
            self.sizeList += 1
            print("index = {0} and data = {1}".format(index,data))
        elif index == self.sizeList and self.sizeList > 0:
            while p.next is not None:
                p = p.next
            p.next = i
            i.previous = p
            self.tail = i
            self.sizeList += 1
            print("index = {0} and data = {1}".format(index,data))

    def add_before(self,data):
        i = Node(data)
        if self.head is not None:
            p = self.head
            self.head = i
            i.next = p
            p.previous = i
        elif self.head is None:
            self.head = i
            self.tail = i
        self.sizeList += 1

    
    def remove(self,data):
        p = self.head
        Check = False
        index = 0
        while p is not None:
            if data == p.data:
                if p.next is not None:
                    if self.head is p:
                        self.head = p.next
                        self.head.previous = None
                    elif self.head is not p:
                       p.previous.next = p.next
                       p.next.previous = p.previous
                        
                elif p.next is None and p.previous is not None:
                    k = p.previous
                    k.next = None
                    self.tail = k
                elif p.next is None and p.previous is None:
                    self.head = None
                    self.tail = None
                
                Check = True
                print("removed :",data,"from index :",index)
                self.sizeList -= 1
                break
            p = p.next
            index += 1
        if Check == False:
            print("Not Found!")
                
I = input("Enter Input : ").split(',')
j = LinkedList()
for q in I:
    z = q.strip().split()
    k = 0
    if z[k] == '':
        k+=1
    if z[k] == 'A':
        j.append(z[k+1])
    elif z[k] == 'Ab':
        j.add_before(z[k+1])
    elif z[k] == 'I':
        q = z[k+1].strip().split(':')
        j.insert(int(q[0]),q[1])
    elif z[k] == 'R':
        j.remove(z[k+1])
    print("linked list : {0}\nreverse : {1}".format(j,j.str_reverse()))

            
        
