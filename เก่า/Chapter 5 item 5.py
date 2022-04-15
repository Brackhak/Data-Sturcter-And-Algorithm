print('******** Parking Lot ********')
max_car , car , a_or_d , where_car = input('Enter max of car,car in soi,operation : ').split(' ')
list_car = car.split(',')
list_car_b = []
if a_or_d == 'arrive' :
    if int(max_car) > len(list_car) :
        if not where_car in list_car :
            list_car.append(where_car)
            print('car',where_car,'arrive! : Add Car',where_car)
        else :
            print('car',where_car,'already in soi')
    else :
        print('car',where_car,'cannot arrive : Soi Full')


elif a_or_d == 'depart' :
    if car != '0' and int(max_car) >= len(list_car) :
        if where_car in list_car :
            for n in range(len(list_car)) :
                if where_car != list_car[len(list_car)-1] :
                    list_car_b.append(list_car[len(list_car)-1])
                    list_car.pop()

                else :
                    list_car.pop()
                    break
            for n in range(len(list_car_b)) :
                list_car.append(list_car_b[len(list_car_b)-1])
                list_car_b.pop()
            print('car',where_car,'depart ! : Car',where_car,'was remove')
        else :
            print('car',where_car,'cannot depart : Dont Have Car',where_car)
    else :
        print('car',where_car,'cannot depart : Soi Empty')




show_car = []
for n in list_car :
    if n != '0' :
        show_car.append(int(n))
print(show_car)

    