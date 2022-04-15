def OddEven(types,text,oddeve):
    lenght = len(text)
    if types == 'S' :
        for n in range(lenght) :
            if oddeve == 'Odd' and n % 2 == 0:
                print(text[n],end= '')
            elif oddeve == 'Even' and n!= 0 and n % 2 != 0:
                print(text[n],end= '')


                
    if types == 'L' :
        count = 0
        print('[',end='')
        
        for n in range(lenght):
            if count <= 4 and oddeve == 'Odd' and n == 4*count and text[1+(4*count)] == ' '  :
                print("'"+text[n]+"'",end='')
                count += 1
                if count != 0 and n != lenght-1:
                    print(',',end=' ')
                    
            elif oddeve == 'Odd' and text[1] != ' ' and text[lenght-2] != ' ':
                print("'"+text+"'",end='')
                break
                
            if oddeve == 'Even' and n == 2+(4*count) and text[3+(4*count)] == ' ' :
                print("'"+text[n]+"'",end='')
                count += 1
                if count != 0 and n != lenght-3:
                    print(',',end=' ')
            if oddeve == 'Odd' and count == 5:
                print("'"+text[lenght-1]+"'",end='')
                break
        print(']')






        
print("*** Odd Even ***")
a = input('Enter Input : ').split(',')
OddEven(a[0],a[1],a[2])
