def add(value):
    list_stack.append(value)
    return "Add = " + str(value) + " and Size = " + str(len(list_stack))

def pop():
    if len(list_stack) > 0 :
        pop_out = list_stack.pop()
        return "Pop = " + str(pop_out) + " and Index = " + str(len(list_stack))
    else :
        return str(-1)

def stack():
    string = "Value in Stack = "
    for i in list_stack :
        string += str(i) + " "
    if len(list_stack) > 0 :
        return string
    else :
        return "Value in Stack = Empty"


list_stack = []
inp = input("Enter Input : ").split(',')
for i in inp :
    if i[0] == "A" :
        print(add(int(i[2:])))
    else :
        print(pop())
print(stack())
