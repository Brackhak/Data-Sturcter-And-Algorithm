class Queue:
    def __init__(self,q = None) :
        if q == None :
            self.q = []
        else : self.q = q

    def __str__(self) :
        return str(self.q)

    def enQueue(self,value) :
        self.q.append(value)

    def deQueue(self) :
        return self.q.pop(0)

    def Size(self) :
        return len(self.q)
    
    def CheckBomb(self) :
        return self.q[0]

class Stack:
    def __init__(self,s = None) :
        if s == None :
            self.s = []
        else : self.s = s

    def __str__(self) :
        s = ""
        self.s.reverse()
        for i in self.s :
            s += str(i)
        return s

    def insert(self,value,point) :
        self.s.insert(point,value)

    def pop(self,point) :
        return self.s.pop(point)
    
    def Size(self) :
        return len(self.s)
    
    def pointer(self,point) :
        return self.s[point]


def Color_Crush(Normal,Mirror) :
    Item = Queue()
    rou_Mirror = Mirror.Size()
    ex_Mirror = 0
    ex_Normal = 0
    ex_Error = 0
    while rou_Mirror > 0 :
        for i in range(Mirror.Size()-2) :
            if Mirror.pointer(i) == Mirror.pointer(i+1) and Mirror.pointer(i) == Mirror.pointer(i+2) and Mirror.pointer(i+1) == Mirror.pointer(i+2) :
                Item.enQueue(Mirror.pop(i))
                for j in range(2) :
                    Mirror.pop(i)
                ex_Mirror += 1
                break
        rou_Mirror -= 1
    #print(Item)

    rou_Normal = Normal.Size()
    while rou_Normal > 0 :
        for i in range(Normal.Size() - 2) :
       
            if Normal.pointer(i) == Normal.pointer(i+1) and Normal.pointer(i) == Normal.pointer(i+2) and Normal.pointer(i+1) == Normal.pointer(i+2) :
                if Item.Size() > 0 :
                    if Item.CheckBomb() == Normal.pointer(i) and Item.CheckBomb() == Normal.pointer(i+1) and Item.CheckBomb() == Normal.pointer(i+2) :
                        ex_Error += 1
                        Normal.insert(Item.deQueue(),i+2)
                        for j in range(3) :
                            Normal.pop(i)
                        break
                    else :
                        Normal.insert(Item.deQueue(),i+2)
                else :
                    for j in range(3) :
                        Normal.pop(i)
                    ex_Normal += 1
                    break
        #print(Normal)
        rou_Normal -= 1 

    print("NORMAL :")
    print(Normal.Size())
    if Normal.Size() > 0 :print(Normal)
    else : print("Empty")
    print(ex_Normal,"Explosive(s) ! ! ! (NORMAL)")
    if ex_Error > 0 : print("Failed Interrupted",ex_Error,"Bomb(s)")      
    print("------------MIRROR------------")
    print(": RORRIM")
    print(Mirror.Size())
    if Mirror.Size() > 0 :print(Mirror)
    else : print("ytpmE")
    print("(RORRIM) ! ! ! (s)evisolpxE",ex_Mirror)

normal,mirror = input("Enter Input (Normal, Mirror) : ").split(' ')
normal = Stack(list(normal))
mirror = list(mirror)
mirror.reverse()
mirror = Stack(mirror)
Color_Crush(normal,mirror)