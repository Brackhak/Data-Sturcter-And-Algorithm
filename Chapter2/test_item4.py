year = int(input("Enter year : "))

summary = 0
mod_and_divide = 1
while summary != 20 and summary != 21 :
    mod_and_divide += 1
    summary = (year // mod_and_divide) * 10 + (year % mod_and_divide)
    
print(summary)
print(mod_and_divide)
