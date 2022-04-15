class StackCalc() :

    def __init__(self ,stack = None) :
        self.status_error = ''
        self.error = 0
        if stack == None :
            self.stack = []
        else :
            self.stack = stack
            
    def __str__(self) :
        return self.stack

    def run(self,arg) :
        for i in arg.split(' ') :
            if i == 'POP' :
                self.POP()
            elif i == 'DUP' :
                self.DUP()
            elif i >= 'a' and i <= 'z' :
                self.status_error = i
                self.error = 1
                break
            elif i >= 'A' and i <= 'Z' :
                self.status_error = i
                self.error = 1
                break
            elif i not in '+-*/' :
                self.PSH(i)
            elif i == '+' :
                self.plus()
            elif i == '-' :
                self.minus()
            elif i == '*' :
                self.mutiply()
            elif i == '/' :
                self.divide()
            
    def getValue(self) :
        if self.error == 0:
            if len(self.stack) > 0 :
                return int(self.POP())
            else :
                return "0"
        else :
            return "Invalid instruction: " + str(self.status_error)

    def PSH(self,num) :
        self.stack.append(num)

    def POP(self) :
        return self.stack.pop()
    
    def DUP(self) :
        self.PSH(self.stack[-1])
    
    def plus(self) :
        Num = int(self.POP())
        Set = int(self.POP())
        output = Num + Set
        self.PSH(output)

    def minus(self) :
        Num = int(self.POP())
        Set = int(self.POP())
        output = Num - Set
        self.PSH(output)


    def mutiply(self) :
        Num = int(self.POP())
        Set = int(self.POP())
        output = Num * Set
        self.PSH(output)

    def divide(self) :
        Num = int(self.POP())
        Set = int(self.POP())
        output = Num / Set
        self.PSH(output)
    


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())