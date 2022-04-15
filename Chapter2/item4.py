def hbd(age):
    age = age
    summary = 0
    mod_and_divide = 1
    while summary != 20 and summary != 21 :
        mod_and_divide += 1
        summary = (age // mod_and_divide) * 10 + (age % mod_and_divide)
    return "saimai is just " + str(summary) + ", in base " + str(mod_and_divide) + "!"
 
year = input("Enter year : ")
print(hbd(int(year)))