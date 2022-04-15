

# # # # from tkinter import *

# # # # root = Tk()
# # # # scrollbar = Scrollbar(root)
# # # # scrollbar.pack( side = RIGHT, fill = Y )

# # # # mylist = Listbox(root, yscrollcommand = scrollbar.set )
# # # # for line in range(100):
# # # #    mylist.insert(END, "This is line number " + str(line))

# # # # mylist.pack( side = LEFT,fill = BOTH)
# # # # scrollbar.config( command = mylist.yview )

# # # # root.mainloop()
# # # # from tkinter import *


# # # # top = Tk()

# # # # Lb1 = Listbox(top)
# # # # # Lb1.insert(1, "Python")
# # # # # Lb1.insert(2, "Perl")
# # # # Lb1.insert(3, "C")
# # # # Lb1.insert(4, "PHP")
# # # # Lb1.insert(5, "JSP")
# # # # Lb1.insert(6, "Ruby")

# # # # Lb1.pack()
# # # # top.mainloop()


# # # # from tkinter import *
# # # # root=Tk()
# # # # frame=Frame(root,width=300,height=300)
# # # # frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
# # # # canvas=Canvas(frame,bg='#123456',width=300,height=300,scrollregion=(0,0,2000,2000))
# # # # hbar=Scrollbar(frame,orient=HORIZONTAL)
# # # # hbar.pack(side=BOTTOM,fill=X)
# # # # hbar.config(command=canvas.xview)
# # # # vbar=Scrollbar(frame,orient=VERTICAL)
# # # # vbar.pack(side=RIGHT,fill=Y)
# # # # vbar.config(command=canvas.yview)
# # # # canvas.config(width=300,height=300)
# # # # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# # # # canvas.pack(side=LEFT,expand=True,fill=BOTH)
# # # # for i in range(0,100):
# # # #     label = Label(canvas,text=str(i))
# # # #     label.pack()

# # # # root.mainloop()



# # # # from tkinter import *

# # # # root = Tk()


# # # # main_frame = Frame(root)
# # # # main_frame.pack(fill = BOTH, expand=1)

# # # # my_canvas = Canvas(main_frame)
# # # # my_canvas.pack(side=LEFT, fill=BOTH, expand = 1)

# # # # my_scrollbar = Scrollbar(main_frame, orient = VERTICAL , command = my_canvas.yview)
# # # # my_scrollbar.pack(side=RIGHT,fill=Y)

# # # # my_canvas.configure(yscrollcommand=my_scrollbar.set)
# # # # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# # # # second_frame = Frame(my_canvas,bg="red")

# # # # my_canvas.create_window((0,0), window = second_frame,anchor="nw")

# # # # for i in range(0,100):
# # # #     label = Label(second_frame,text=str(i),bg="#123456",fg = "white")
# # # #     label.pack(pady=20)

# # # # root.geometry("500x400")
# # # # root.mainloop()

# # # import tkinter as tk
# # # from tkinter import *



# # # win = Tk()

# # # colors = ["Blue","Gold","Red","black"]

# # # def radCall():
# # #     radSel = radVar.get()
# # #     if radSel == 0 : win.configure(background = colors[0])
# # #     elif radSel ==1 : win.configure(background = colors[1]) 
# # #     elif radSel ==2 : win.configure(background = colors[2]) 

# # # radVar = tk.IntVar()

# # # radVar.set(99)

# # # for col in range(4):
# # #     curRad = tk.Radiobutton(win, text = colors[col],variable = radVar,value = col, command = radCall)
# # #     curRad.pack(side = LEFT)

# # # win.mainloop()

# # # # from tkinter import *
# # # # from tkinter import ttk

# # # # def problem1():
# # # #     for i in range(1,5):
# # # #         label = Label(win, text='%d.' % i)
# # # #         label.grid(column=0, row=i)
# # # #     for count, question in enumerate(questions, 1):
# # # #         radVar = IntVar()
# # # #         for i in range(1,5):
# # # #             button = ttk.Radiobutton(win, text="num%d" % i, variable=radVar, value=i, command=check)
# # # #             button.grid(row=count, column=i)
# # # #         answers.append(radVar)

# # # # def check():
# # # #     # check submitted answers against correct answers here
# # # #     for x in answers:
# # # #         print(x.get())

# # # # win = Tk()
# # # # win.title("Exam")
# # # # win.geometry('1530x300+0+690')
# # # # questions = ["num1", "num2", "num3", "num4"]
# # # # answers = []
# # # # problem1()
# # # # action = ttk.Button(win, text="check the answer", command = check)
# # # # action.grid(column=0, row=5)
# # # # win.mainloop()














# # from Tkinter import *
# # import time

# # root = Tk()
# # l = Label( root, text=time.strftime( "%d/%m/%Y %A %H:%M:%S") )
# # l.pack()
# # root.update()

# # while True:
# #     time.sleep( 1 )
# #     l[ "text" ]=time.strftime( "%d/%m/%Y %A %H:%M:%S" )
# #     root.update()
    
# # mainloop()
# import tkinter as tk 
# from tkinter import * 
# from tkinter import scrolledtext 
# from tkinter import ttk 
# # root = tk.Tk()
#  # monty = ttk.LabelFrame(root, text=' Monty Python') # Create a container whose parent container is win
# # monty.grid(column=0, row=0, padx=10, pady=10)
# # scr = scrolledtext.ScrolledText(monty, width=30, height=5, wrap=tk.WORD)
# # scr.grid(column=0, columnspan=3)
# # root.mainloop()

# # root = tk.Tk() 
# # root.grid() 
# # app = ttk.Frame(root) 
# # app.grid()

# # fram1 = tk.LabelFrame(app, text='1') 
# # txt1 = tk.Text(fram1) 
# # sl1 = Scrollbar(fram1) 
# # sl1['command'] = txt1.yview
# # # sl1.grid(row=0, column=1,sticky=S + W  )
# # # txt1.grid(row=0, column=0,sticky=S + W  )
# # # fram1.grid(row=0, column=0, sticky=S + W )
# # sl1.grid(row=0, column=1, sticky=S + W + E + N)
# # txt1.grid(row=0, column=0, sticky=S + W + E + N)
# # fram1.grid(row=0, column=0, sticky=S + W + E + N)
# # mainloop()

# # from tkinter import *

# # root = Tk()
# # root.geometry("200x200")
# # root.title("My Button Increaser")

# # global counter
# # counter = 0

# # def nClick():
# #     global counter
# #     counter += 1
# #     mButton1.config(text = counter)

# # mButton1 = Button(text = counter, command = nClick, fg = "darkgreen", bg = "white")
# # mButton1.pack()

# # root.mainloop()
# # from tkinter import *

# # def coinsCheckCollision(self):
# #     cRemove = None
# #     indexRemove = -1
# #     count = 0
# #     for c in self.frame.coins:
# #         x, y , width , height = c.getRectangle()
# #         xP = self.player.getX; yP = self.player.getY; wP = self.player.getWidth; hP = self.player.getHeight
# #         if collisionDetect(xP , x, yP  , y, wP , width, hP , height) or collisionDetect(x , xP , y , yP , width , wP , height , hP):
# #             if count not in coinsRemoved:
# #                 indexRemove = count
# #         if indexRemove != -1:
# #             if indexRemove not in coinsRemoved:
# #                 coinsRemoved.append(indexRemove)
# #         count +=1

# # def coinsUpdateAnimations(self):
# #     count = 0
# #     for c in self.frame.coins:
# #         if count not in coinsRemoved:
# #             self.img = c.getAnimation()
# #             self.img = ImageTk.PhotoImage(self.img)
# #             self.frame.coinsImages[count] = self.img
# #         else:
# #             if self.frame.coinsImages[count] is not '' :
# #                 self.frame.coinsImages[count] = ''
# #                 self.frame.canvas.delete('coinB'+str(count))
# #         what = self.frame.canvas.itemconfig('coin' + str(count), image=self.frame.coinsImages[count])
# #         count += 1
# #     self.coinsCheckCollision()
# #     self.frame.frame.after(40 , self.coinsUpdateAnimations)



# #
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # mouse-drag tester ver. 7.0
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import tkinter as tk

# GRIDCOLOR = '#7f7f7f' #same as '#%02x%02x%02x' % (127, 127, 127)

# grid_left_margin = 20
# grid_top_margin = 30
# grid_column_width = 120
# grid_row_height = 40
# BORDER_WIDTH = 8
# dragBox_width = grid_column_width - 20
# dragBox_height = grid_row_height - 10

# class DragBox(tk.Canvas):
#     def __init__(self, master=None, **kwargs):
#         super().__init__(master, **kwargs)
#         self.make_lines()
#         self._former_pos = 0,0
#         self.bind('<Button>', self.remember)
#         self.bind('<B1-Motion>', self.ondrag)
#         self.boxes = {}
#         self.active = None
#         self.callback = None

#         # add the boxes
#         self.add_box(80, 100, 'red', 'Box 1')
#         self.add_box(80, 200, 'green', 'Box 2')
#         self.add_box(200, 200, 'blue', 'Box 3')

#     def remember(self, event):
#         self._former_pos = event.x, event.y
#         self.active = None
#         for box in self.boxes:
#             x1, y1, x2, y2 = self.coords(box)
#             if x1 <= event.x <= x2 and y1 <= event.y <= y2:
#                 self.active = box
#         if self.active:
#             name = self.boxes.pop(self.active)
#             self.boxes[self.active] = name
#             self.tag_raise(self.active)

#     def add_box(self, x_pos, y_pos, color, name):
#         box = self.create_rectangle(x_pos, y_pos, x_pos+dragBox_width, y_pos+dragBox_height, outline=color)
#         self.boxes[box] = name

#     def ondrag(self, event):
#         if self.active is not None:
#             self.move(self.active, event.x-self._former_pos[0], event.y-self._former_pos[1])
#             self._former_pos = event.x, event.y
#             if self.callback:
#                 self.callback(event.x, event.y, self.boxes[self.active])

#     def make_lines(self):
#         width, height = int(self['width']), int(self['height'])
#         offset = BORDER_WIDTH//2
#         self.create_rectangle(offset, offset, width-offset, height-offset, outline=GRIDCOLOR, width=BORDER_WIDTH)
#         for row_position in range(grid_top_margin, height, grid_row_height):
#             self.create_line(0, row_position, width, row_position, fill=GRIDCOLOR)
#         for column_position in range(grid_left_margin, width, grid_column_width):
#             self.create_line(column_position, 0, column_position, height, fill=GRIDCOLOR)

# class DataFrame(tk.Frame):
#     def __init__(self, master=None, **kwargs):
#         super().__init__(master, **kwargs)

#         self.xpos = self.make_data_display('Mouse x:')
#         self.ypos = self.make_data_display('Mouse y:')
#         self.boxname = self.make_data_display('Box name:')

#     def make_data_display(self, label):
#         column, row = self.grid_size()
#         lbl = tk.Label(self, text=label)
#         lbl.grid(row=row, column=0, sticky=tk.W)
#         stringvar = tk.StringVar(value='[???]')
#         lbl = tk.Label(self, textvariable=stringvar)
#         lbl.grid(row=row, column=1, sticky=tk.W)
#         return stringvar

#     def update(self, xpos, ypos, name):
#         self.xpos.set(xpos)
#         self.ypos.set(ypos)
#         self.boxname.set(name)

# def main():
#     root = tk.Tk()
#     db = DragBox(root, bg='white', width=800, height=500)
#     db.pack(side=tk.LEFT)
#     data_display = DataFrame(root)
#     data_display.pack(expand=True)
#     db.callback = data_display.update
#     root.mainloop()

# if __name__ == "__main__":
#     main()

# # ~~~~~~~~~ the end ~~~~~~~~~



# import tkinter as tk
# from tkinter import ttk
# from tkinter import *

# root = tk.Tk()
# root.geometry("1920x1080")
# container = ttk.Frame(root)
# canvas = tk.Canvas(container,width=1870,height=1080)
# scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas,width=1900,height=1080)

# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# Goods_labelimg = PhotoImage(file="Rectangle 33.png")
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# canvas.configure(yscrollcommand=scrollbar.set)


# for i in range(100):
       
#    Goods_Label = ttk.Label(scrollable_frame,image = Goods_labelimg,borderwidth=0,relief="flat")
#    Goods_Label.pack(pady =5)
#    ttk.Label(Goods_Label, text="Sample scrolling label",font = ("Londrina Solid Black",50)).place(x=10,y=10)
#    Goods_Label.update_idletasks()

# container.pack(fill = BOTH, expand=1)
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# root.mainloop()

import tkinter as tk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # alternate ways to create the frames & append to frames dict: comment out one or the other

        for F in (StartPage, PLG):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.frames["StartPage"] = StartPage(parent=container, controller=self) 
        # self.frames["PLG"] = PLG(parent=container, controller=self)
        # self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        # self.frames["PLG"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    # alternate version of show_frame: comment out one or the other

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()

    # def show_frame(self, page_name):
        # frame = self.frames[page_name]
        # frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One", command=lambda: controller.show_frame("PLG"))
        button1.pack()        

        button2 = tk.Button(self, text="focus traversal demo only")
        button2.pack()
        button2.focus_set()

        button3 = tk.Button(self, text="another dummy button")
        button3.pack()

        lbl = tk.Label(self, text="tkraise messes up focus traversal\nwhich you can see by testing the two versions of show_frame.()\nUsing grid_remove instead of tkraise solves that,\nwhile preventing frames from being unable to resize to fit their own contents.")
        lbl.pack()

class PLG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter something below; the two buttons clear what you type.")
        label.pack(side="top", fill="x", pady=10)
        self.wentry = tk.Entry(self)
        self.wentry.pack(pady = 10)
        self.text = tk.Text(self)
        self.text.pack(pady = 10)
        restart_button = tk.Button(self, text="Restart", command=self.restart)
        restart_button.pack()
        refresh_button = tk.Button(self, text="Refresh", command=self.refresh) 
        refresh_button.pack()  

    def restart(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    def refresh(self):
        self.wentry.delete(0, "end")
        self.text.delete("1.0", "end")
        # set focus to any widget except a Text widget so focus doesn't get stuck in a Text widget when page hides
        self.wentry.focus_set()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()