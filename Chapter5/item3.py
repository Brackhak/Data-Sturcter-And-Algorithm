class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

def createList(l=[]):
    count = 0
    head = node(l[count])
    link = head
    count += 1
    while count < len(l) :
        new_node = node(l[count])
        link.next = new_node
        link = link.next
        count += 1
        if l == [] :
            break
       #print(link)
   # while head.next != None :
      #  print(head)
      #  head = head.next
    return head
    

def printList(H):
    s = ''
    while H != None :
        #print(H.data)
        s += H.data + ' '
        H = H.next
    print(s)
    

def mergeOrderesList(p,q):
    if int(p.data) > int(q.data) :
        data = q.data
        head = node(data)
        q = q.next
    else :
        data = p.data
        head = node(data)
        p = p.next
    t = head
    while p != None or q != None :
        if p != None and q != None :
            if int(p.data) > int(q.data) :
                data = q.data
                t.next = node(data)
                q = q.next
            else :
                data = p.data
                t.next = node(data)
                p = p.next
        else :
            if p != None :
                data = p.data
                t.next = node(data)
                p = p.next
            elif q != None :
                data = q.data
                t.next = node(data)
                q = q.next
            else :
                break
        t = t.next
    return head

L1 , L2 = input("Enter 2 Lists : ").split(' ')
LL1 = createList(L1.split(','))
LL2 = createList(L2.split(','))
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)