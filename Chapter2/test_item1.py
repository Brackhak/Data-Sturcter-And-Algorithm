def Rshift(num):
    if num >= 0 :
        binary_num = []
        minum_num = 8192
        while minum_num >= 1 :
            if num - minum_num >= 0 :
                num -= minum_num
                binary_num.append(1)
                minum_num /= 2
            elif num - minum_num < 0 and 1 in binary_num :
                minum_num /= 2
                binary_num.append(0)
            else :
                minum_num /= 2
    else :
        binary_num = [1]
        minus_num = -1
        while minus_num > num :
            minus_num *= 2
        plus = minus_num*-1
        while plus >= 1 :
            if minus_num + plus <= num :
                minus_num += plus
                plus /= 2
                binary_num.append(1)
            else :
                plus /= 2
                binary_num.append(0)
    shift = shift
    while shift != 0 :
        binary_num.pop()
        shift -= 1
        
            
    
    
    return binary_num
    

    

n = input("Enter number and shiftcount : ")

print(Rshift(int(n)))
