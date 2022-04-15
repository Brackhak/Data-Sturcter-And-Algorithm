list_dish = list((input('Enter Input : ')).split(','))
count = 0
while count != 1 :
    for n in range(len(list_dish)) :
        if n == len(list_dish)-1 :
            count = 1
            break
        kg_under , hz_under = list_dish[n].split(' ')
        kg_top , hz_top = list_dish[n+1].split(' ')
        if int(kg_under) < int(kg_top) :
            del list_dish[n]
            print(hz_under)
            break
        #print(list_dish)
