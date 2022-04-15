class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def addRear(self, new):
        if self.next is None:
            self.next = new
            self.next.prev = self
        else:
            temp = self.next
            self.next.prev = new
            self.next = new
            self.next.next = temp
            self.next.prev = self

    def addFront(self, new):
        if self.prev is None:
            self.prev = new
            self.prev.next = self
        else:
            temp = self.prev
            self.prev.next = new
            self.prev = new
            self.prev.next = self
            self.prev.prev = temp

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev



class dll:
    def __init__(self):
       self.head = None
       self.tail = None

    def setHead(self,h):
        self.head = h

    def setTail(self,t):
        self.tail = t

    def add(self,new):
        temp = self.head
        exist = False
        if temp is None:
            self.setHead(new)
        else:
            if temp.next is not None:
                while temp.next is not None:
                    if new.data[0] == temp.data[0]:
                        print("This name is already existed")
                        exist = True
                        return
                    elif new.data[0] != temp.data[0]:
                        while temp is not None:
                            if new.data[0] == temp.data[0]:
                                # print("This name is already existed")
                                exist = True
                                return
                            temp = temp.next
                    if exist == False:
                        temp = self.head
                        if new.data[1] < temp.data[1]:
                            temp.addFront(new)
                            self.setHead(new)
                            return
                        elif new.data[1] == temp.data[1]:
                            while new.data[1] == temp.data[1] and temp.next is not None and temp.next.data[1] == new.data[1]:
                                temp = temp.next
                            if temp.next is None:
                                self.setTail(new)
                            temp.addRear(new)
                            return
                        elif new.data[1] > temp.data[1]:
                            if temp.next is not None:
                                while temp.next is not None and new.data[1] >= temp.next.data[1]:
                                    temp = temp.next
                                if temp.next is None:
                                    temp.addRear(new)
                                    self.setTail(new)
                                else:
                                    temp.addRear(new)
                            else:
                                temp.addRear(new)
                                self.setTail(new)
            else:
                if new.data[1] < temp.data[1]:
                    temp.addFront(new)
                    self.setHead(new)
                    self.setTail(new)
                elif new.data[1] >= temp.data[1]:
                    temp.addRear(new)
                    self.setTail(new)

    def delete(self, item):
        temp = self.head
        if temp is None:
            print("No player in the list")
        elif temp.next is None:
            if temp.data[0] == item:
                self.head = None
            # else:
            #     print("Name not found")
        elif temp.data[0] == item:
            self.head = self.head.next
            self.head.prev = None
        elif temp.data[0] != item:
            while temp is not None:
                if temp.data[0] == item:
                    break
                temp = temp.next
            # if temp is None:
            #     print("Name not found")
            if temp.next is not None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            else:
                if temp.data[0] == item:
                    temp.prev.next = None
                    self.setTail(temp)
                # else:
                #     print("Name not found")

    def update(self, item, score):
        temp = self.head
        while temp is not None:
            try:
                int(score)
            except(Exception):
                print("invalid input(s)")
                return
            if temp.data[0] == item:
                self.delete(item)
                self.add(Node([item,score]))
                return
            temp = temp.next
        if temp is None:
            print("Name not found")

    def printScore(self, order=None):
        if order is None or order == "asc":
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
        elif order == 'dsc':
            temp = self.tail
            while temp is not None:
                print(temp.data)
                temp = temp.prev

    def retrieve(self, item):
        temp = self.head
        while temp is not None:
            if temp.data[0] == item:
                return temp.data[1]
            temp = temp.next
        print("Name not found")

a = dll()
a.add(Node(['pond',10]))
a.add(Node(['gun',20]))
a.add(Node(['pam',30]))
print()
a.printScore('dsc')
print()
a.printScore('asc')
print()
a.update('gun',-20)
a.printScore('asc')
print()
a.add(Node(['a',0]))
a.printScore('asc')
print()
a.delete('pam')
a.printScore('dsc')



