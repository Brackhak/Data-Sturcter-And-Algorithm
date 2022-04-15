class funString():

    def __init__(self,string = ""):

        self.str = string

    def __str__(self):
        return "String is " + str(self.str)

    def size(self) :
        self.size  = 0
        for i in self.str :
            self.size += 1
        return self.size

    def changeSize(self):
        new_chang_str = ''
        for i in self.str :
            if ord(i) >= 65 and ord(i) <= 90 :
                i = chr(ord(i) + 32)
            elif ord(i) >= 97 and ord(i) <= 122 :
                i = chr(ord(i) - 32)
            new_chang_str += i
        return new_chang_str

    def reverse(self):
        sizee = self.size()
        reversed_str = ''
        for i in range(1,sizee+1) :
            reversed_str += self.str[i*-1]
        return reversed_str

    def deleteSame(self):
        new_str = ''
        for i in self.str :
            if i not in new_str :
                new_str += i
        return new_str

        
str1,str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())