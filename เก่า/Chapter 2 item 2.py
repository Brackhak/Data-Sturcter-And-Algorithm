
def length(txt):
    global count
    count += 1
    if txt[0] != None and txt[-1] == "+" and txt[1] != "+":
        txt = txt.replace("+","-")
        return(str(txt[0]) + "*" + length(txt[1:]))
    elif txt[0] != None and txt[-1] == "-" and txt[1] != "-":
        txt = txt.replace("-","+")
        return(str(txt[0]) + "~" + length(txt[1:])) 
    else :
        if txt[1] == "+" :
            return(str(txt[0]) + "*") 
        elif txt[1] == "-" :
            return(str(txt[0]) + "~")
count = 0
print(length(input("Enter Input : ") + "+"),sep="")
print(count)
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)