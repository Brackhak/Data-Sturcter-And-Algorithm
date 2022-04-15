color_list = list(input('Enter Input : ').split(' '))
end_check = 0
combo_check = 0
#print(len(color_list))
while end_check != 1:
    for n in range(len(color_list)) :
        if n == len(color_list)-2 or len(color_list) <= 1 :
            end_check = 1
            break
        elif color_list[n] == color_list[n+1] and color_list[n] == color_list[n+2]  :
            #print(color_list[n],color_list[n+1],color_list[n+2])
            combo_check += 1
            if len(color_list) == 3 :
                end_check = 1
            for del_repeat in range(3) :
                del color_list[n]
            break

print(len(color_list))
for n in range(len(color_list)):
    print(color_list[len(color_list)-1-n],end='')
if len(color_list) != 0 :
    print('')
if combo_check > 1 :
    if len(color_list) == 0 :
        print('Empty')
    print('Combo :',combo_check,'! ! !')
elif len(color_list) == 0 :
    print('Empty')
