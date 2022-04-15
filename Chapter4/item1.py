class Queue :
    def __init__(self,q = None) :
        if q == None :
            self.q = []
        else : self.q = q
        self.was_q = []

    def __str__(self) :
        s = str(self.q[0])
        for x in range(1,len(self.q)) :
            s += ', '
            s += str(self.q[x])
        return str(s) + ' : '

    def enQueue(self,i) :
        self.q.append(i)
        if self.q != [] :
            s = str(self.q[0])
            for x in range(1,len(self.q)) :
                s += ', '
                s += str(self.q[x])
            return s
    
    def deQueue(self) :        
        if self.q != [] :
            self.was_q.append(self.q.pop(0))
            s = str(self.was_q[-1]) + ' <- '
            if self.q != [] :
                s += str(self.q[0])
            else : s += 'Empty'

            for x in range(1,len(self.q)) :
                s += ', '
                s += str(self.q[x])
        else : return 'Empty'
        return s
        

    def isEmpty(self) :
        if self.Size > 0 :
            return 'NotEmpty'
        else : return 'Empty'

    def Size(self):
        return len(self.q)

def Q(inp) :
    q = Queue()
    for i in inp :
        if i[0] == 'E' :
            print(q.enQueue(i[2:]))
        else :
            print(q.deQueue())
    if q.was_q != [] :
        s = q.was_q[0]
        for i in range(1,len(q.was_q)) :
            s += ', '
            s += str(q.was_q[i])
    else : s = 'Empty'
    s += ' : '
    if q.q != [] :
        s += q.q[0]
        for i in range(1,len(q.q)) :
            s += ', '
            s += str(q.q[i])
    else : s += 'Empty'
    return s

inp = input('Enter Input : ').split(',')
print(Q(inp))
