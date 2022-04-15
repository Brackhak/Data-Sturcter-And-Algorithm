dict_name = {
            "111" : "Coke" ,
            "112" : "Pepsi" ,
            "113" : "Fanta" ,
            "114" : "Est"
        }

class Node :
    def __init__(self,id_stock = None, exp = None) :
        self.id_stock = id_stock
        self.exp = exp
        self.next =None
        self.previous = None

class linkedlist :
    def __init__(self) :
        self.head = None
        self.tail = None

    def __str__(self) :
        if self.head == None :
            return "Empty"
        else :
            All_data,current = str(self.head.id_stock) + ',' + str(self.head.exp) + '\n' , self.head
            while current.next != None :
                current = current.next
                All_data += str(current.id_stock) + ',' + str(current.exp) + '\n'
            return All_data

    def append(self,id_stock,exp) :
        data = Node(int(id_stock),exp)
        if self.head == None :
            self.head = data
            self.tail = self.head
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = data
            t.next.previous = t
            self.tail = t.next
        
    def insert(self,id_stock,exp) :
        data = Node(id_stock,exp)
        t = self.head
        if t.next == None :
            t.next = data
        while t.next != None :
            if int(id_stock) > int(t.id_stock) and int(id_stock) <= int(t.next.id_stock) :
                p = t.next
                t.next = data
                data.next = p
                break
            t = t.next
        if t.next == None :
            t.next = data


    def list_name(self) :
        name = []
        if self.head == None :
            return None
        else :
            t = self.head
            while t != None :
                name.append(str(t.id_stock))
                t = t.next
            return name
    
    def size(self) :
        t = self.head
        count = 0
        while t != None :
            t = t.next
            count += 1
        return count

    def return_id(self,num) :
        if num == 0 :
            return self.head.id_stock
        else :
            count = 0
            t = self.head
            while t != None :
                if num == count :
                    return t.id_stock
                t = t.next
                count += 1
    
    def return_exp(self,num) :
        if num == 0 :
            return self.head.exp
        else :
            count = 0
            t = self.head
            while t != None :
                if num == count :
                    return t.exp
                t = t.next
                count += 1

    def bubble_sort(self):
        t = self.head
        while t.next != None :
            t2 = self.head
            while t2.next != None :
                if t2.id_stock >= t2.next.id_stock :
                    t2.id_stock , t2.next.id_stock = t2.next.id_stock , t2.id_stock
                    t2.exp , t2.next.exp = t2.next.exp , t2.exp
                t2 = t2.next
            t = t.next

    def append_and_sort_by_exp(self,id_stock,exp) :
        exp_for_calculate = exp.split('/')
        #print(exp[2],exp[1],exp[0])
        calculate_exp = (int(exp_for_calculate[2]) + (int(exp_for_calculate[1]) / 100) + (int(exp_for_calculate[0]) / 10000))//0.0001
        #print(str(calculate_exp) + '\n')
        data = Node(id_stock,exp)
        if self.head == None :
            self.head = data
            self.tail =self.head
        else :
            t = self.head
            #print(t.exp)
            if t.next == None :
                exp_node = t.exp.split('/')
                calculate_exp_node = (int(exp_node[2]) + (int(exp_node[1]) / 100) + (int(exp_node[0]) / 10000))//0.0001
               #print("Exp node is " + str(calculate_exp_node))
                if id_stock >= self.head.id_stock :
                    if calculate_exp >= calculate_exp_node :
                        t.next = data
                        t.next.previous = t
                        self.tail = t.next
                    else :
                        self.head = data
                        self.head.next = t
                        self.head.next.previous = self.head
                        self.tail = self.head.next
                else :
                    self.head = data
                    self.head.next = t
                    self.head.next.previous = self.head
                    self.tail = self.head.next
            else :
                print("While loop!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                #print(self.list_name())
                t = self.head
                while t.next != None :
                    exp_node = t.exp.split('/')
                    calculate_exp_node = (int(exp_node[2]) + (int(exp_node[1]) / 100) + (int(exp_node[0]) / 10000))//0.0001
                    if int(id_stock)//100 <= int(t.id_stock)//100 :
                        if int(id_stock)//100 < int(t.id_stock)//100 :
                            p = t
                            t.previous.next = data
                            t2 = t.previous.next
                            t2.previous = t.previous
                            t2.next = p
                            t2.next.previous = t2
                            break
                        elif int(id_stock)//100 == int(t.id_stock)//100 :
                            if calculate_exp < calculate_exp_node :
                                if t == self.head :
                                    self.head = data
                                    self.head.next = t
                                    t.previous = self.head
                                    break
                                else :
                                    p = t
                                    t.previous.next = data
                                    t2 = t.previous.next
                                    t2.previous = t.previous
                                    t2.next = t
                                    break
                            else :
                                p = t.next
                                t.next = data
                                t.next.previous = t
                                t.next.next = p
                                break
                    else :
                        if t.next == None :
                            t.next = data
                            break
                        else :
                            t = t.next
                            if t.next == None :
                                if id_stock < t.id_stock :
                                    p = t
                                    t.previous.next = data
                                    t2 = t.previous.next
                                    t2.next = p
                                    t2.previous = t.previous
                                    t2.next.previous = t2
                                    self.tail = t2.next
                                    break
                                else :
                                    if calculate_exp < calculate_exp_node :
                                        p = t
                                        t = data
                                        t.next = p
                                        break
                                    else :
                                        t.next = data
                                        break
                            
                

if __name__ == "__main__" :
    f = open("Stock_data.txt","r");
    stock = linkedlist()
    while(True) :
        s = f.readline()
        if s == '' :
            break        
        s = s.split(',')
        exp = str(s[1])
        print(stock)
        stock.append_and_sort_by_exp(s[0],exp[0:-1])
    f.close()

print(stock)
#stock.insert(13205,'14/09/2588')
#stock.bubble_sort()
#p = stock.list_name()
#print(p)

#f = open("Stock_data.txt" , "w+")
#f.write(str(stock.return_id(0)) + ',' + str(stock.return_exp(0)) + '\n' )
#f.close()
#f = open("Stock_data.txt" , 'a')
#for i in range(1,stock.size()) :
#    f.write(str(stock.return_id(i)) + ',' + str(stock.return_exp(i)) + '\n')
#f.close()
#print(stock)
