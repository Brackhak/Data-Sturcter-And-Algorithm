class funString :
    def __init__(self,text,choice):
        self.text = text
        self.choice = choice

    def lenstr (self):
        self.lenght = len(self.text)
        return self.lenght

    def changsize (self,n) :
        if self.text[n] >= 'a' and self.text[n] <= 'z' :
            n1 = ord(self.text[n]) - 32
            n2 = chr(n1)
            return n2
        elif self.text[n] >= 'A' and self.text[n] <= 'Z' :
            n1 = ord(self.text[n]) + 32
            n2 = chr(n1)
            return n2
        
    def reverse(self,n):
        self.lenght = len(self.text)
        return self.text[self.lenght-n-1]
            
    def delete(self,n):
        lenght = len(self.text)
        if n < lenght :
            print(self.text[n],end='')
            self.text = self.text.replace(self.text[n],'')
        return ''

text , choice = input('Enter String and Number of Function : ').split()
ans = funString(text,int( choice))

if int(choice) == 1 :
    print(ans.lenstr())
elif int(choice) == 2 :
    for n in range(len(text)) :
        print(ans.changsize(n),end='')
elif int(choice) == 3 :
    for n in range(len(text)):
        print(ans.reverse(n),end='')
elif int(choice) == 4 :
    for n in range(len(text)):
        print(ans.delete(0),end='')
      

