class Stack_Calc :
    def __init__(self):
        self.start = 1

    def run(self,cal_list):
        self.number_list = []
        self.sum = 0
        self.cal_list = list(cal_list.split(' '))
        self.break_check = 0
        stack1 , stack2 = 0,0
        sum = 0
        for n in range(len(self.cal_list)) : 
            if self.cal_list[n] >= 'a' and  self.cal_list[n] <= 'z' :
                print('Invalid instruction:',self.cal_list[n])
                self.break_check = 1
                break       
            if self.cal_list[n] != 'DUP' and self.cal_list[n] != 'POP' and self.cal_list[n] != 'PSH' and self.cal_list[n] != '+'  and self.cal_list[n] != '-'  and self.cal_list[n] != '*'  and self.cal_list[n] != '/' and int(self.cal_list[n]) > 0:                
                self.number_list.append(self.cal_list[n])
            elif self.cal_list[n] == 'DUP' :
                self.number_list.append(self.number_list[len(self.number_list)-1])
            elif self.cal_list[n] == 'POP' :
                self.number_list.pop()

            elif self.cal_list[n] == '+' :
                stack1 = self.number_list[len(self.number_list)-1]
                stack2 = self.number_list[len(self.number_list)-2]
                self.number_list.pop()
                self.number_list.pop()
                sum = int(stack1) + int(stack2)
                self.number_list.append(int(sum))
                
            elif self.cal_list[n] == '-' :
                stack1 = self.number_list[len(self.number_list)-1]
                stack2 = self.number_list[len(self.number_list)-2]
                self.number_list.pop()
                self.number_list.pop()
                sum = int(stack1) - int(stack2)
                self.number_list.append(int(sum))

            elif self.cal_list[n] == '*' :
                stack1 = self.number_list[len(self.number_list)-1]
                stack2 = self.number_list[len(self.number_list)-2]
                self.number_list.pop()
                self.number_list.pop()
                sum = int(stack1) * int(stack2)
                self.number_list.append(int(sum))

            elif self.cal_list[n] == '/' :
                stack1 = self.number_list[len(self.number_list)-1]
                stack2 = self.number_list[len(self.number_list)-2]
                self.number_list.pop()
                self.number_list.pop()
                sum = int(stack1) / int(stack2)
                self.number_list.append(int(sum))
        
    def getValue(self) :
        if self.break_check == 0 and len(self.number_list) != 0 :
            return (self.number_list[len(self.number_list)-1])
        elif len(self.number_list) == 0 and self.break_check == 0 :
            return int(0)
        else :
            return str('')

    


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = Stack_Calc()
machine.run(arg)
print(machine.getValue())