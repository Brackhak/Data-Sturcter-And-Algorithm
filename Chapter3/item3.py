class Stack():

    def __init__(self, ls = None):
        if ls == None :
            self.stack = []
        else :
            self.stack = ls
    def push(self,i):
        self.stack.append(i)
        
    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if self.stack != [] :
            return "Not Empty"
        else :
            return "Empty"

    def size(self):
        return len(self.stack)

def postFixeval(st):
    s = Stack()
    for i in st :
        if i not in '+-*/' :
            s.push(i)
        elif i in '+' :
            Num = float(s.pop())
            Set = float(s.pop())
            summ = Set + Num
            s.push(summ)
        elif i in '-' :
            Num = float(s.pop())
            Set = float(s.pop())
            summ = (Set) - (Num)
            s.push(summ)
        elif i in '*' :
            Num = float(s.pop())
            Set = float(s.pop())
            summ = (Set) * (Num)
            s.push(summ)
        else :
            Num = float(s.pop())
            Set = float(s.pop())
            summ = (Set) / (Num)
            s.push(summ)
    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
postFixeval(token)


print("Answer : ",'{:.2f}'.format(postFixeval(token)))