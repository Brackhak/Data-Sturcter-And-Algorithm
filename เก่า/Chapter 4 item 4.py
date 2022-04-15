inpu = input('Enter Input : ').split(',')
inpu2 =[]
do_My = []
do_My_list = []
do_Your_list = []
do_Your = []
act_My = []
act_Your = []
locat_My =[]
locat_Your = []
act_dict = {
    "0" : "Eat",
    "1" : "Game",
    "2" : "Learn",
    "3" : "Movie"
}
locat_dict = {
    "0" : "Res.",
    "1" : "ClassR.",
    "2" : "SuperM.",
    "3" : "Home"
}
for n in range(len(inpu)) :
    inpu2.append(inpu[n].split(' '))
    do_My.append(inpu2[n][0])
    do_Your.append(inpu2[n][1])
    do_My_list.append(do_My[n].split(':'))
    do_Your_list.append(do_Your[n].split(':'))
    act_My.append(do_My_list[n][0])
    locat_My.append(do_My_list[n][1])
    act_Your.append(do_Your_list[n][0])
    locat_Your.append(do_Your_list[n][1])

print('My   Queue = ',end ='')
for n in range(len(do_My)) :
    check = do_My[n]
    if do_My[len(do_My)-1] != check :
        print(check,end='')
        print(',',end =' ')
    else :
        print(check)
print('Your Queue = ',end ='')
for n in range(len(do_Your)) :
    check = do_Your[n]
    if do_Your[len(do_Your)-1] != check :
        print(check,end='')
        print(',',end =' ')
    else :
        print(check)

print('My   Activity:Location = ',end = '')
for n in range(len(do_My)) :
    check = do_My[n]
    if do_My[len(do_My)-1] != check :
        print(act_dict[act_My[n]],end='')
        print(':',end = '')
        print(locat_dict[locat_My[n]],end = '')
        print(',',end =' ')
    else :
        print(act_dict[act_My[n]],end='')
        print(':',end = '')
        print(locat_dict[locat_My[n]])
        
print('Your Activity:Location = ',end = '')
for n in range(len(do_Your)) :
    check = do_Your[n]
    if do_Your[len(do_Your)-1] != check :
        print(act_dict[act_Your[n]],end='')
        print(':',end = '')
        print(locat_dict[locat_Your[n]],end = '')
        print(',',end =' ')
    else :
        print(act_dict[act_Your[n]],end='')
        print(':',end = '')
        print(locat_dict[locat_Your[n]])

score = 0
for n in range(len(do_My)) :
    if act_My[n] == act_Your[n] and locat_My[n] != locat_Your[n] :
        score += 1
    elif act_My[n] != act_Your[n] and locat_My[n] == locat_Your[n] :
        score += 2
    elif act_My[n] == act_Your[n] and locat_My[n] == locat_Your[n] :
        score += 4
    else :
        score -= 5

if score >= 7 :
    print('Yes! You\'re my love! : Score is',end =' ')
    print(score,end = '')
    print('.')
elif score > 0 and score < 7 :
    print('Umm.. It\'s complicated relationship! : Score is',end =' ')
    print(score,end = '')
    print('.')
else :
    print('No! We\'re just friends. : Score is',end =' ')
    print(score,end = '')
    print('.')