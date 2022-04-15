text_check = list(input('Enter Input : '))
count = 0
while len(text_check) != 0 :
    count += 1
    for n in range(len(text_check)) :
        if(n >= len(text_check)):
            break
        for m in range(len(text_check)) :
            if text_check[n] == '(' and text_check[m] == ')' and n != m or text_check[n] == '[' and text_check[m] == ']' and n != m:
                if n > m :
                    del text_check[n]
                    del text_check[m]
                    break
                elif m > n :
                    del text_check[m]
                    del text_check[n]
                    break
    if count > 100 :
        break
if len(text_check) == 0 :
    print(len(text_check))
    print('Perfect ! ! !')
else :
    print(len(text_check))
 

