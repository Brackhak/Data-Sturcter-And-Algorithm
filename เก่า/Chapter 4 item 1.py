Q = input('Enter Input : ').split(',')
Q2 = []
vari = []
val = []
count = 0
for n in range(len(Q)) :
    Q2.append(Q[n].split(' '))
    if Q[n][0] == 'E' :
        vari.append(Q2[n][0])
        val.append(Q2[n][1])
        print('Add',val[count],'index is',count)
        count += 1
    else :
        if len(val) != 0 :
            vari.append(Q[n][0])
            print('Pop',val[0],'size in queue is',len(val)-1)
            val.pop(0)
            count -= 1
        else :
            print('-1')
    
if len(val) != 0 :
    print('Number in Queue is : ',val)
else :
    print('Empty')
        
    