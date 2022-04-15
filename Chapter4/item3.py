class Queue :
    def __init__(self,q = None) :
        if q == None :
            self.q = []
        else : self.q = q

    def __str__(self) :
        return str(self.q)

    def Size(self) :
        return len(self.q)

    def pointer(self,point) :
        return self.q[point]

    def replac(self,value,point) :
        self.q[point] = value

def encodemsg(q1 , q2) :
    count = 0
    for i in range(q1.Size()) :
        a = q1.pointer(i)
        if count > q2.Size() -1  :
            count = 0
        for j in range(int(q2.pointer(count))) :
            a = chr(ord(a) + 1)
            if ord(a) > ord('z') :
                a = chr(ord(a) - 26)
            elif ord(a) > ord('Z') and ord(a) < ord('a') :
                a = chr(ord(a) - 26)
        q1.replac(a,i)
        count += 1
    print("Encode message is : " ,q1)

def decodemsg(q1,q2) :
    count = 0
    for i in range(q1.Size()) :
        a = q1.pointer(i)
        if count > q2.Size() -1  :
            count = 0
        for j in range(int(q2.pointer(count))) :
            a = chr(ord(a) - 1)
            if ord(a) < ord('A') :
                a = chr(ord(a) + 26)
            elif ord(a) > ord('Z') and ord(a) < ord('a') :
                a = chr(ord(a) + 26)
        q1.replac(a,i)
        count += 1
    print("Decode message is : " ,q1)

string , number = list(input("Enter String and Code : ").split(','))
string  = list(string)
number = list(number)
for i in string  :
    if ' ' in string :
        string.remove(' ')
    
q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1,q2)
decodemsg(q1,q2)