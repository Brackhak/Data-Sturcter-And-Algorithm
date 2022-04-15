class Stack :
    def __init__(self,binary = None ) :
        if binary == None :
            self.binary = []
        else :
            self.binary = binary
    
    def __str__(self) :
        self.binary.reverse()
        s = ''
        for i in self.binary :
            s += str(i)
        return s

    def push(self,i) :
        self.binary.append(i)

    ### Enter Your Code Here ###

def dec2bin(decnum):
    remain = 0
    s = Stack()
    while decnum > 0 :
        remain = decnum % 2
        decnum = decnum // 2
        s.push(remain)
    return s.__str__()

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))