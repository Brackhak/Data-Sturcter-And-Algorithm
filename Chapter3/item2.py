class Stack() :
    def __init__(self,paren = None) :
        if paren == None :
            self.paren = []
        else : self.paren = paren
    
    def __str__(self) :
        s = ''
        for i in self.paren:
            s += str(i)+''
        return s

    def push(self,i) :
        self.paren.append(i)

    def pop(self) :
        return self.paren.pop()

    def peek(self) :
        return self.paren[-1]

    def isEmpty(self) :
        return self.paren == []
    
    def size(self) :
        return len(self.paren)

def matching(stack) :
    s = Stack()
    i = 0
    error = 0

    while i < len(stack) and error == 0 :
        c = stack[i]
        if c in '{[(' :
            s.push(c)
        else :
            if c in '}])' :
                if s.size() > 0 :
                    if not match(s.pop(),c):
                        error = 1
                        break
                else :
                    error = 2
        i += 1

    if s.size() > 0 and error == 0 :
        error = 3
    return error,c,i,s    



def match(opens,closed) :
    return (opens == '(' and closed == ')') or (opens == '[' and closed ==']') or (opens == '{' and closed == '}')


inp = input("Enter expresion : ")
err,c,i,s = matching(inp)
if err == 1 :
    print(inp,'Unmatch open-close')[[]]
elif err == 2 :
    print(inp,'close paren excess')
elif err == 3 :
    print(inp,'open paren excess  ',s.size(),':',s,end="")
else :
    print(inp,'MATCH')