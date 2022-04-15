def mapp(text):
    list = []
    str = {}
    count = 0
    for n in text:
        if not n in str:
            str[n] = count
            count+=1
    for n in text:
        list.append(str[n])
    print(list)
text = input('Enter String : ')
mapp(text)
