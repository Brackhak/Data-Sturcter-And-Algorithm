class Queue:
    def __init__(self,q = None) :
        if q == None :
            self.q =[]
        else : self.q = q
    
    def enQueue(self,value) :
        self.q.append(value)
    def deQueue(self) :
        return self.q.pop(0)
        

def OTA(inp):
    normal = Queue()
    vip = Queue()
    for i in inp :
        if i[0:2] == 'EN' :
            normal.enQueue(i[3:])
        elif i[0:2] == 'ES' :
            vip.enQueue(i[3:])
        elif i[0:2] == 'D' :
            if vip.q != [] :
                print(vip.deQueue())
            elif normal.q != [] :
                print(normal.deQueue())
            else :
                print("Empty")
inp = input("Enter Input : ").split(',')
OTA(inp)