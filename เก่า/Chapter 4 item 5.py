inpu_red , inpu_blue = input('Enter Input (Red, Blue) : ').split(' ')
red_list = []
blue_list = []
freez_bomb = []
freez_bomb_reverse = []
count_freezbomb = 0
count_redbomb = 0
count_Explosive = 0
count_Explosive_Fail = 0
count_Explosive_Freez = 0
stop_bomb = 0
for n in range(len(inpu_red)) :
    red_list.append(inpu_red[n])
for n in range(len(inpu_blue)) :
    blue_list.append(inpu_blue[n])


for n in range(0,-(len(blue_list)-1),-1) :
    if count_freezbomb >= -(len(blue_list)-2) and blue_list[count_freezbomb] == blue_list[count_freezbomb-1] and blue_list[count_freezbomb] == blue_list[count_freezbomb-2] and blue_list[count_freezbomb-1] == blue_list[count_freezbomb-2] :
        freez_bomb.append(blue_list[count_freezbomb])
        for m in range(3) :
            del blue_list[count_freezbomb]
        count_freezbomb -= 0
        count_Explosive_Freez +=    1
        
    else :
        count_freezbomb -= 1
      #  for m in range(3) :
       #     blue_list.pop(n)


for n in range(1000) :
    if count_redbomb >= len(red_list)+20 :
        count_redbomb = 0
    if count_redbomb < len(red_list)-2 and red_list[count_redbomb] == red_list[count_redbomb+1] and red_list[count_redbomb] == red_list[count_redbomb+2] and red_list[count_redbomb+1] == red_list[count_redbomb+2] :
        if len(freez_bomb) > 0 :
            if red_list[count_redbomb] == freez_bomb[0] :
                for m in range(2) :
                    del red_list[count_redbomb]
                freez_bomb.pop(0)
                count_Explosive_Fail += 1
                count_redbomb += 1
            
            else :
                red_list.insert(count_redbomb+2,freez_bomb[0])
                freez_bomb.pop(0)
                count_redbomb += 4
                stop_bomb += 1
        else :
            for m in range(3) :
                del red_list[count_redbomb]
            count_redbomb -= 1
            count_Explosive += 1

    else :
        count_redbomb += 1
print('Red Team :')
print(len(red_list))
if len(red_list) > 0 :
    for n in range(len(red_list)) :
        print(red_list[len(red_list)-n-1],end = '')
    print('')
else :
    print('Empty')
print(count_Explosive,'Explosive(s) ! ! ! (HEAT)')
if count_Explosive_Fail > 0 :
    print('Blue Team Made (a) Mistake(s)',count_Explosive_Fail,'Bomb(s)')
print('----------TENETTENET----------')
print(': maeT eulB')
print(len(blue_list))
if len(blue_list) > 0 :
    for n in range(len(blue_list)) :
        print(blue_list[n],end = '')
    print('')
else :
    print('ytpmE')

print('(EZEERF) ! ! ! (s)evisolpxE',count_Explosive_Freez)