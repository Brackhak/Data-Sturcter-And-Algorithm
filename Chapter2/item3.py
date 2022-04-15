def new_range(a=0.0,b=1.0,c=0.0) :
    print("(",end = '')
    while a <= c :
        a = ((a * 1000) // 1) / 1000
        b = ((b * 1000) // 1) / 1000
        print(float(a),end='')
        if a+b >= c :
            break
        print(",",end=' ')
        a = a + b
    print(")") 

print("*** New Range ***")
x = input("Enter Input : ").split()
if len(x) == 1 :
    new_range(float(0),float(1),float(x[0]))
elif len(x) == 2 :
    new_range(float(x[0]),float(1),float(x[1]))
elif len(x) == 3 :
    new_range(float(x[0]),float(x[2]),float(x[1]))

