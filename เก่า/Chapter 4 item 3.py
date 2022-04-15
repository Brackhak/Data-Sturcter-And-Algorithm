book,inpu = input('Enter Input : ').split('/')
book_list = book.split()
inpu_list = inpu.split(',')
E_or_D = []
check = ''
for n in range(len(inpu_list)) :
    E_or_D.append(inpu_list[n].split())
    if E_or_D[n][0] == 'E' :
        book_list.append(E_or_D[n][1])

    else :
        book_list.pop(0)
for n in range(len(book_list)) :
    check = book_list[0]
    book_list.pop(0)
    if check in book_list :
        print('Duplicate')
        break
    elif not check in book_list and len(book_list) == 1 :
        print('NO Duplicate')
        break

print(E_or_D)
