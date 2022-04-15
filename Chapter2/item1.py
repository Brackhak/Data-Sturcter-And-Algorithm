def Rshift(num,shift):
    binary_num = []
    minum_num = 8192
    type_num = 0 # 0 is positive and 1 is negative

    if num >= 0 :
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
        type_num = 1
        binary_num = [1]
        minus_num = -256
        while minus_num > num :
            minus_num *= 2
        plus = (minus_num*-1)/2
        while plus >= 1 :
            if minus_num + plus <= num :
                minus_num += plus
                plus /= 2
                binary_num.append(1)
            else :
                plus /= 2
                binary_num.append(0)

    shift = shift
    while shift != 0 and binary_num != []:
        if len(binary_num) == 1 and type_num == 1 :
            break
        else :
            binary_num.pop()
            shift -= 1
    mutiply_num = 1
    summary = 0
    while binary_num != [] :
        check = binary_num.pop()
        if check == 1 and type_num == 0: # Positive
            summary += mutiply_num
        elif check == 1 and type_num == 1: # Negative
            if len(binary_num) == 0:
                summary += mutiply_num*-1
            else :
                summary += mutiply_num
        mutiply_num *= 2

    return summary

    



n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))