inpu = input('Enter Input : ').split(',')
Q1 = []
Q2_EN = []
Q2_ES = []
index_Q_show = 0
index_Q_VIP = 0
many_show = 0
count_empty = 0
start = 0
ending = []
VIP_List = []
check_len = 0
for n in range(len(inpu)) :
    Q1.append(inpu[n].split(' '))
    if Q1[n][0] == 'D' :
        many_show += 1
for n in range(-1,-(len(Q1)),-1) :
    if Q1[n][0] == 'EN' :
        ending.append(Q1[n][1])
        break
        
for n in range(len(Q1)) :
    #if many_show == len(Q1) :
    #    break
    if Q1[n][0] == 'EN':#and not Q1[n][1] in Q2 :
        Q2_EN.append(Q1[n][1])
    elif Q1[n][0] == 'ES' :#and not Q1[n][1] in Q2: # or Q1[n][0] == 'ES' and not Q1[n][1] in VIP_List :
        Q2_ES.insert(index_Q_VIP,Q1[n][1])
        VIP_List.append(Q1[n][1])
        index_Q_VIP += 1
    elif Q1[n][0] == 'D' :
      #  print('This D')
        if len(Q2_ES) != 0 :
            print(Q2_ES[0])
            #if Q2[index_Q_show] == ending[0] :
            #    break
            Q2_ES.pop(0)
        elif len(Q2_EN) != 0:
            print(Q2_EN[0])
            Q2_EN.pop(0)
        else :
            print('Empty')
            count_empty += 1
        
        
    