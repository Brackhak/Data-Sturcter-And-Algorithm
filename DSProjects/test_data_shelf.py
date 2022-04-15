dict_price = {
            "111":"20" , "112":"10" , "113":"15" , "114":"25" , "115":"10" , "116":"15" , "117":"30" , "118":"15"
            ,"121":"17" , "122":"26" , "123":"19" , "124":"35" , "125":"11" , "126":"9" , "127":"7" , "128":"10"
            ,"131":"15" , "132":"17" , "133":"20" , "134":"35"
            ,"211":"15" , "212":"25" , "213":"15" , "214":"10"
        }

class queue :
    def __init__(self,q = []) :
        self.q = q
        self.count = 0

    def __str__(self) :
        return str(self.q)

    def enQueue(self,id_shelf) :
        self.q.append(id_shelf)
        self.count += 1

    def deQueue(self) :
        if self.count > 0 :
            pop = self.q.pop[0]
            return pop 
        else :
            return "Empty"
        
    def resetQueue(self) :
        self.q = []

    def list_name(self) :
        name = []
        count_while = 0
        while count_while != self.count :
            name.append(self.q[count_while][0])
            count_while += 1
        return name

    def list_exp(self) :
        exp = []
        count_while = 0
        while count_while != self.count :
            exp.append(self.q[count_while][1])
            count_while += 1
        return exp

    def return_size(self) :
        return self.count

    def bubble_sort_ByPrice(self) :
        for i in range(self.return_size()) :
            for j in range(self.return_size()-1) :
                before = int(dict_price[str(self.q[j][0])])
                after = int(dict_price[str(self.q[j+1][0])])
                if before >= after :
                    save = self.q[j]
                    self.q[j] = self.q[j+1]
                    self.q[j+1] = save
        return self.q

    def Add_Amount(self,id_shelf) :
        count = 0
        while count != self.return_size() :
            if self.q[count][0] == id_shelf :
                self.q[count][1] += 1
            count +=1 
            

q = queue()
q.resetQueue()
f = open("Shelf_data.txt" , 'r')
while(True) :
    s = f.readline()
    if s == '' :
        break        
    s = s.split(',')
    exp = s[1]
    s[0] = int(s[0])
    s[1] = exp[0:-1]
    q.enQueue(s)
print(q)
print(q.list_name())


list_cart = queue()
pack = [115 , 0]
list_cart.enQueue(pack)
list_id = list_cart.list_name()
inp = input("Input ID : ")
if not int(inp) in list_id :
    pack = [int(inp) , 0]
    list_cart.enQueue(pack)
    list_cart.Add_Amount(int(inp))
else :
    list_cart.Add_Amount(int(inp))
print(list_cart)