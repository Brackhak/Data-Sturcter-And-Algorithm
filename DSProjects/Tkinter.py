# import tkinter as tk
# from tkinter import Tk, Canvas, Frame, BOTH
# from tkinter import *
# root = tk.Tk()
# root.geometry("1920x1080")
# bg = PhotoImage(file="newbg.png")
# pixelVirtual = tk.PhotoImage(width=1, height=1)
# usericn = PhotoImage(file="Admin.png")
# passicn = PhotoImage(file="Lock.png")

# def on_click1(event):
#     if Username.get() == "USERNAME" :
#         event.widget.delete(0, tk.END)
        


# def on_click2(event):
#     if Password.get() == "PASSWORD" :
#         Password.config(show="*")
#         event.widget.delete(0, tk.END)
    

# def off_click1(event):
#     if Username.get() == "" :
#         event.widget.insert(0, "USERNAME")
#         return False
#     else:
#         return True

    

# def off_click2(event):
#     if Password.get() == "" :
#         Password.config(show="")
#         event.widget.insert(0, "PASSWORD")
#         return False
#     else:
#         return True

# def character_limit(entry_text):
#     if len(entry_text.get()) > 0:
#         entry_text.set(entry_text.get()[:14])

# def submit():
    
#     name=Usernamedef.get()
#     password=Passworddef.get()
    
#     l = ['Rapeepat 1234','Jhon 5678','Jimmy 5555']
#     correctname =[]
#     correctpass = []
#     print("The name is : " + name)
#     print("The password is : " + password)

#     Usernamedef.set("USERNAME")
#     Passworddef.set("PASSWORD")
#     Password.config(show="")
#     Wrongtext = tk.StringVar()
#     WronngLabel = Label(root,font = ("Londrina Solid Black",24),textvariable=Wrongtext,fg = "#C04B4B",bg ="#FFFFFF",width=45,height=1)
    
#     for i in l:
#         i = i.split(" ")
#         correctname.append(i[0])
#         correctpass.append(i[1])
#     if  name == "USERNAME" and  password == "PASSWORD":
        
#         Wrongtext.set("*Please enter your Username and Password")

#     elif name == "USERNAME" and password != "PASSWORD":
#         Wrongtext.set("*Please enter your Username")

#     elif name != "USERNAME" and password == "PASSWORD":
#         Wrongtext.set("*Please enter your Password")

#     elif name in correctname :
#         if password == correctpass[correctname.index(name)]:
#             Wrongtext.set("Welcome")
#         else:
#             Wrongtext.set("*Username or Password incorrect")
#     else :
#         Wrongtext.set("*Username or Password incorrect")
#     WronngLabel.place(x=960,y=976,anchor = "center")





# my_label =Label(root, image=bg)
# my_label.place(x=0, y=0)


# Font_tuple = ("Londrina Solid Black",64)
# my_text = Label(root,image=pixelVirtual, text="Admin Login", fg="white",bg="#849D8A", width=645, height=140,compound="c")
# my_text.pack(pady=429)
# my_text.configure(font = Font_tuple)

# LoginRec = Frame(root,bg="white",width=651,height=440)
# LoginRec.place(x=634,y=573)


# line = Frame(root,bg="#849D8A",width=520,height=2)
# line.place(x=706,y=712)

# Usernamedef = tk.StringVar()
# Usernamedef.set("USERNAME")
# Username = Entry(root,bd=0,textvariable=Usernamedef)
# Username.bind("<Button-1>", on_click1)
# Username.bind("<Key>", on_click1)
# Username.bind("<Leave>", off_click1)
# Username.place(x=877,y=610,width=400)
# Usernamedef.trace("w", lambda *args: character_limit(Usernamedef))



# Passworddef = tk.StringVar()
# Passworddef.set("PASSWORD")
# Password = Entry(root,bd=0,textvariable=Passworddef)
# Password.bind("<Button-1>", on_click2)
# Password.bind("<Key>", on_click2)
# Password.bind("<Leave>", off_click2)
# Password.place(x=877,y=750,width=400)
# Passworddef.trace("w", lambda *args: character_limit(Passworddef))

# LoginBtn = Button(root,image=pixelVirtual,text= "Login",font = ("Londrina Solid Black",64) ,width=647, height=100,compound="c", fg="white",bg="#849D8A",borderwidth=0,
# command = submit)
# LoginBtn.place(x=634,y=840)

# usericn_label = Label(root, image=usericn, width=63,height=77,borderwidth=0)
# usericn_label.place(x=740, y=595)

# passicn_label = Label(root, image=passicn, width=63,height=77,borderwidth=0)
# passicn_label.place(x=740, y=735)

# Username.configure(font = ("Londrina Solid Black",36),fg ="#A5ABC7")
# Password.configure(font = ("Londrina Solid Black",36),fg ="#A5ABC7")




# root.mainloop()


# from tkinter import *
# root = Tk()
# e = Entry(highlightthickness=2)
# e.config(highlightbackground = "red", highlightcolor= "red")
# e.pack()
# root.mainloop()

# from Tkinter import *

# root = Tk()
# topframe = Frame(root, width = 300, height = 900)
# topframe.pack()

# frame = Frame(root, width = 202, height = 32, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
# l = Entry(frame, borderwidth=0, relief="flat", highlightcolor="white")
# l.place(width=200, height=30)
# frame.pack
# frame.pack()
# frame.place(x = 50, y = 30)

# import tkinter 
from tkinter import *
  
# Create Tk object 
window = Tk() 
  
# Set the window title 
window.title('GFG') 
  
# Create a Frame for border
border_color = Frame(window, background="red")
  
# Label Widget inside the Frame
label = Label(border_color, text="This is a Label widget", bd=1)
  
# Place the widgets with border Frame
label.pack(padx=1, pady=1)
border_color.pack(padx=1, pady=1)
  
window.mainloop()