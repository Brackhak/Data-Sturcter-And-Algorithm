
count = 0
lis = input('Enter Your List : ').split()
lenght = len(lis)
if(lenght > 2) :
    print('[',end='')

    for n1 in range(lenght) :
        for n2 in range(lenght):
            for n3 in range(lenght):
            
                if int(lis[n1]) + int(lis[n2]) + int(lis[n3]) == 0 and lis[n1] != lis[n2] and lis[n1] != lis[n3] and lis[n2] != lis[n3] and n1 < n2 and n1 < n3 and n2 < n3  :
                    if count != 0 :
                        print(', ',end='')
                    print('['+lis[n1]+', '+lis[n2]+', '+lis[n3]+']',end='')
                    count += 1
                    
            
        if int(lis[n1]) + int(lis[n2]) + int(lis[n3]) == 0 and lis[n1] == lis[n2] and lis[n1] == lis[n3] and lis[n2] == lis[n3] :
            print('['+lis[n1]+', '+lis[n2]+', '+lis[n3]+']',end ='')
            break
    print(']'   )
else :
    print('Array Input Length Must More Than 2')




