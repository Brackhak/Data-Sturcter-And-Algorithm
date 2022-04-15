def GCD(n1 , n2) :
    global dividsor
    dividsor -= 1
    #print(n1 , "mod" , n2 , "is" , dividsor )
    if n1 % dividsor == 0 and n2 % dividsor == 0 :
        if n1_copy < 0 and n2_copy < 0 :
            if n1_copy <= n2_copy :
                return "The gcd of "+ str(n1_copy) + " and " + str(n2_copy) + " is : " +str(dividsor)
            else :
                return "The gcd of "+ str(n2_copy) + " and " + str(n1_copy) + " is : " +str(dividsor)          
        if n1_copy >= n2_copy : 
            return "The gcd of "+ str(n1_copy) + " and " + str(n2_copy) + " is : " +str(dividsor)
        elif n2_copy >= n1_copy:
            return "The gcd of "+ str(n2_copy) + " and " + str(n1_copy) + " is : " +str(dividsor)
    elif n1 % dividsor != 0 or n2 % dividsor != 0 :
        return GCD(n1,n2)
    
dividsor = 0
n1,n2 = input('Enter Input : ').split()
n1 = int(n1)
n2 = int(n2)
n1_copy = n1
n2_copy = n2
if n1 == 0 and n2 == 0 :
    print("Error! must be not all zero.")
elif abs(n1) >= abs(n2) : 
    dividsor = abs(n1) + 1
    print(GCD(abs(n1),abs(n2)))
elif abs(n2) > abs(n1) :
    dividsor = abs(n2) + 1
    print(GCD(abs(n1),abs(n2)))
    



