from os import read
import tkinter as tk               
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
from tkinter import font
from typing import Sized
import qrcode
import ctypes
#from typing_extensions import TypeAlias
from PIL import Image, ImageTk
from tkinter.font import Font

import os
Font_tuple1 = ("Londrina Solid Black",64)
Font_tuple2 = ("Londrina Solid",90)

NAME = ["Coke", "Pepsi", "Fanta", "Est", "Mirinda", "Sprite", "7up", "Lipton"]
IMG = {"Coke" : "img/Coke.png", "Pepsi" : "img/Pepsi.png","Fanta":"Fanta.png","Est":  "Est.png","Mirinda": "Mirinda.png", "Sprite" : "Sprite.png", "7up" : "7up.png","Lipton" : "Lipton.png"}
AMOUNTS = {"Coke" : 0,"Pepsi" : 1,"Fanta" : 2,"Est": 3, "Mirinda": 4,"Sprite": 5,"7up" : 6,"Lipton" : 7}

dict_img = {
            "111":"img/Coke.png" , "112":"img/Pepsi.png" , "113":"img/Fanta.png" , "114":"img/Est.png" , "115":"img/Sprite.png" , "116":"img/7up.png" , "117":"img/Mirinda.png" , "118":"img/BigCola.png"
            ,"121":"img/Crystal.png" , "122":"img/Singha.png" , "123":"img/Namthip.png" , "124":"img/Nestle.png" , "125":"img/Chang.png" , "126":"img/Purra.png" , "127":"img/Aura.png" , "128":"img/Sprinkle.png"
            ,"131":"img/Nescafe.png" , "132":"img/Birdy.png" , "133":"img/Carabao.png" , "134":"img/Arabus.png"
            ,"211":"img/Lay.png" , "212":"img/Tasto.png" , "213":"img/SnackJack.png" , "214":"img/Hanami.png" , "215":"img/Cornae.png" , "216":"img/Oreo.png" , "217":"img/Potae.png"
            ,"221":"img/Kitkat.png" , "222":"img/M&M.png" , "223":"img/Ferrero.png" , "224":"Meiji.png"
        }
dict_name = {
            "111":"Coke" ,"112":"Pepsi" ,"113":"Fanta" ,"114":"Est" ,"115":"Sprite" ,"116":"7up" ,"117":"Mirinda" , "118":"BigCola"
            ,"121":"Crystal" , "122":"Singha" , "123":"Namthip" , "124":"Nestle" , "125":"Chang" , "126":"Purra" , "127":"Aura" , "128":"Sprinkle"
            ,"131":"Nescafe" , "132":"Birdy" , "133":"Carabao" , "134":"Arabus"
            ,"211":"Lay" , "212":"Tasto" , "213":"SnackJack" , "214":"Hanami","215":"Cornae" , "216":"Oreo" , "217":"Potae"
            ,"221":"Kitkat" , "222":"M&M" , "223":"Ferrero" , "224":"Meiji"
        }
dict_price = {
            "111":"10" , "112":"12" , "113":"15" , "114":"14" , "115":"18" , "116":"20" , "117":"21" , "118":"25"
            ,"121":"7" , "122":"8" , "123":"10" , "124":"11" , "125":"7" , "126":"15" , "127":"18" , "128":"9"
            ,"131":"15" , "132":"20" , "133":"10" , "134":"30" , "215":"15" , "216":"5" , "217":"30"
            ,"211":"20" , "212":"25" , "213":"15" , "214":"10"
            ,"221":"30" , "222":"25" , "223":"50" , "224":"42"
        }



class SampleApp(tk.Tk): #ส่วนที่เอาไว้เปลี่ยนหน้า

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1920x1080")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Firstpage,Secondpage,Firstpage3,Cartpage,CheckoutPage,Admin_Login_Page,Firstpage2,Stock_Page,Firstpage4,Shelf_Page,Add_Shelf_Page,Admin_Management_Page,Add_Stock_Page,Contactpage,Aboutpage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        
        self.show_frame("Firstpage")
        #self.show_frame("Add_Shelf_Page")
        


class Firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.start_bth = PhotoImage(file='Group 8.png')
        self.bg = PhotoImage(file="page1-01 2.png")
        bg = Label(self, image=self.bg)
        bg.place(x=0, y=0)
        str = Label(self, text="Grocery", bg="#E09292", fg="White", font=self.Myfont(130))
        str.place(x=120, y=220)
        str1 = Label(self, text="Store", bg="#E09292", fg="White", font=self.Myfont(130))
        str1.place(x=120, y=400)
        str2 = Label(self, text="Self Check Out ", bg="#E09292", fg="White", font=self.Myfont(60))
        str2.place(x=120, y=620)
        butstart = Button(self, image=self.start_bth, bg="#E09292", borderwidth=0,
                          command=lambda: controller.show_frame("Secondpage"))
        butstart.place(x=125, y=720)
        butabout = Button(self, text="About", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,
                          command=lambda: controller.show_frame("Aboutpage"))
        butabout.place(x=1400, y=55)
        butcon = Button(self, text="Contact", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,
                        command=lambda: controller.show_frame("Contactpage"))
        butcon.place(x=1600, y=55)
        butadmin = Button(self, text="Admin", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,
                          command=lambda: controller.show_frame("Admin_Login_Page"))
        butadmin.place(x=134, y=60)

    def Myfont(self, sizefont):
        self.myfont = Font(family="Londrina Solid", size=sizefont)
        return self.myfont


class Secondpage(tk.Frame):


    def Myfont(self, sizefont):
        self.myfont = Font(family="Londrina Solid", size=sizefont)
        return self.myfont

    def click_total(self, e):
        TOTAL = True
        print("total")
        print(TOTAL)

    def reset_page(self) :
        
        self.refresh(self.parent,self.controller)
        self.controller.show_frame("Secondpage")

    def refresh(self,parent, controller):

        self.q = queue()
        self.q.resetQueue()
        f = open("Shelf_data.txt" , 'r')
        while(True) :
            s = f.readline()
            if s == '' :
                break        
            s = s.split(',')
            s[0] = int(s[0])
            if s[0] in self.q.list_name() :
                self.q.Add_Amount(s[0])
            else :
                self.q.enQueue([s[0] , 1])
        #print(self.q)
        f.close()

        self.bgimage = PhotoImage(file="Group 11.png")
        self.bg = Label(self, image=self.bgimage)
        self.bg.pack(fill=BOTH, expand=1)

        # header
        self.headerimg = PhotoImage(file="Group 11.png")
        self.header = Label(self, image=self.headerimg, bg="black", height=314, width=1920)
        self.header.place(x=0, y=0)

        self.btnback = Button(self.header, text="back", bg="#ECC5BE", fg="White", borderwidth=0,
                              command=lambda: controller.show_frame("Firstpage"), font=self.Myfont(50))
        self.btnback.place(x=48, y=36)
        self.btncartimage = PhotoImage(file="shopping-cart-empty-side-view 1.png")
        self.btncart = Button(self.header, image=self.btncartimage, bg="#ECC5BE", borderwidth=0,
                              command=lambda: controller.show_frame("Cartpage") )
        self.btncart.place(x=1743, y=42, width=107, height=107)

        btntotal = Button(self.header, text="Total", bg="#ECC5BE", fg="#849D8A", borderwidth=0, font=self.Myfont(50))
        # btntotal.bind("<Button-1>", self.click_total)
        btntotal.place(x=16, y=198, width=320, height=105)
        btntotal.bind("<Button-1>", self.click_total)
        # sorttype
        btnty = Button(self.header, text="Type", bg="#ECC5BE", fg="#849D8A", borderwidth=0, font=self.Myfont(50))
        btnty.place(x=348, y=198, width=415, height=105)
        btnty.bind('<Button-1>', self.click_tydown)
        btnty.place(x=348, y=198, width=415, height=105)
        btnty.bind('<Button-1>', self.click_tydown)
        # sortprice
        btnpr = Button(self.header, text="Price", bg="#ECC5BE", fg="#849D8A", borderwidth=0, font=self.Myfont(50))
        btnpr.place(x=779, y=198, width=425, height=105)
        btnpr.bind('<Button-1>', self.click_prdown)

        self.bgentry = PhotoImage(file="Group 10.png")
        self.my_entry = Entry(self.header, font=self.Myfont(40))
        self.my_entry.place(x=494, y=42, width=794, height=99)
        self.btn_entry = Button(self.header, image=self.bgentry, bg="#ECC5BE", borderwidth=0)
        self.btn_entry.place(x=1381, y=20)
        self.btn_entry.bind("<Button-1>", self.click_search)

        self.xofinfo = 36
        self.xofName = 68
        self.xofbtn = 418
        self.pricetotal = 0
        self.pricepcr = {}
        self.cart = queue()
        self.infoimage = PhotoImage(file="bginfogoods.png")
        self.btnaddimage = PhotoImage(file="btnaddreal.png")

        # content

        self.List_Goods = tk.Canvas(self.bg, bg="White", highlightthickness=0, bd=0)
        self.List_Goods.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.List_Goods.xview_moveto(1)
        self.List_Goods.update()

        self.my_scrollbar = tk.Scrollbar(self, orient=HORIZONTAL, command=self.List_Goods.xview, width=20)
        self.my_scrollbar.pack(side=BOTTOM, fill=X)

        self.btnreset = Button(self.header, text="Reset", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.reset_page()])
        self.btnreset.place(x=20, y=13)
        self.btndestroy = Button(self.header, text="Destroy", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.bg.pack_forget(),self.my_scrollbar.pack_forget(),self.List_Goods.pack_forget()])
        self.btndestroy.place(x=20, y=43)

        self.List_Goods.configure(xscrollcommand=self.my_scrollbar.set)

        self.second_frame = tk.Frame(self.List_Goods, bg="White")
        self.second_frame.bind('<Configure>',
                               lambda e: self.List_Goods.configure(scrollregion=self.List_Goods.bbox("all")))
        self.List_Goods.create_window((40, 360), window=self.second_frame, anchor="nw")
        self.second_frame.update()

        self.Goodsimg = []
        for i in range(self.q.return_size()):
             self.Goodsimg.append("")

        for i in range(self.q.return_size()) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(self.q.return_id(i))])


        # content
        for i in range(0, self.q.return_size()):
            info = Label(self.second_frame, image=self.infoimage, width=535, height=636)
            info.pack(side=LEFT, padx=50, pady=0)
            Goods_img = tk.Label(info,image=self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=31,y =18)
            Name = Label(info, text=dict_name[str(self.q.return_id(i))], bg="#ECC5BE", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=30, y=380)
            Prices = Label(info, text=str(dict_price[str(self.q.return_id(i))]) + "   Bath", bg="#E09292", fg="White", font=self.Myfont(50))
            Prices.place(x=30, y=520)
            btnadd = Button(info, image=self.btnaddimage, bg="#E09292", borderwidth=0, text=str(self.q.return_id(i)))
            btnadd.place(x=380, y=497)
            btnadd.bind("<Button-1>", self.on_click)


    def __init__(self, parent, controller):
        
        self.parent = parent
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.q = queue()
        self.q.resetQueue()
        f = open("Shelf_data.txt" , 'r')
        while(True) :
            s = f.readline()
            if s == '' :
                break        
            s = s.split(',')
            s[0] = int(s[0])
            if s[0] in self.q.list_name() :
                self.q.Add_Amount(s[0])
            else :
                self.q.enQueue([s[0] , 1])
        #print(self.q)
        f.close()

        self.bgimage = PhotoImage(file="Group 11.png")
        self.bg = Label(self, image=self.bgimage)
        self.bg.pack(fill=BOTH, expand=1)

        # header
        self.headerimg = PhotoImage(file="Group 11.png")
        self.header = Label(self, image=self.headerimg, bg="black", height=314, width=1920)
        self.header.place(x=0, y=0)

        self.btnback = Button(self.header, text="back", bg="#ECC5BE", fg="White", borderwidth=0,
                              command=lambda: controller.show_frame("Firstpage"), font=self.Myfont(50))
        self.btnback.place(x=48, y=36)
        self.btncartimage = PhotoImage(file="shopping-cart-empty-side-view 1.png")
        self.btncart = Button(self.header, image=self.btncartimage, bg="#ECC5BE", borderwidth=0,
                              command=lambda: controller.show_frame("Cartpage") )
        self.btncart.place(x=1743, y=42, width=107, height=107)

        btntotal = Button(self.header, text="Total", bg="#ECC5BE", fg="#849D8A", borderwidth=0, font=self.Myfont(50))
        # btntotal.bind("<Button-1>", self.click_total)
        btntotal.place(x=16, y=198, width=320, height=105)
        btntotal.bind("<Button-1>", self.click_total)
        # sorttype
        btnty = Button(self.header, text="Type", bg="#ECC5BE", fg="#849D8A", borderwidth=0, font=self.Myfont(50))
        btnty.place(x=348, y=198, width=415, height=105)
        btnty.bind('<Button-1>', self.click_tydown)
        btnty.place(x=348, y=198, width=415, height=105)
        btnty.bind('<Button-1>', self.click_tydown)
        # sortprice
        btnpr = Button(self.header, text="Price", bg="#ECC5BE", fg="#849D8A", borderwidth=0, font=self.Myfont(50))
        btnpr.place(x=779, y=198, width=425, height=105)
        btnpr.bind('<Button-1>', self.click_prdown)

        self.bgentry = PhotoImage(file="Group 10.png")
        self.my_entry = Entry(self.header, font=self.Myfont(40))
        self.my_entry.place(x=494, y=42, width=794, height=99)
        self.btn_entry = Button(self.header, image=self.bgentry, bg="#ECC5BE", borderwidth=0)
        self.btn_entry.place(x=1381, y=20)
        self.btn_entry.bind("<Button-1>", self.click_search)

        self.xofinfo = 36
        self.xofName = 68
        self.xofbtn = 418
        self.pricetotal = 0
        self.pricepcr = {}
        self.cart = queue()
        self.infoimage = PhotoImage(file="bginfogoods.png")
        self.btnaddimage = PhotoImage(file="btnaddreal.png")

        # content

        self.List_Goods = tk.Canvas(self.bg, bg="White", highlightthickness=0, bd=0)
        self.List_Goods.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.List_Goods.xview_moveto(1)
        self.List_Goods.update()

        self.my_scrollbar = tk.Scrollbar(self, orient=HORIZONTAL, command=self.List_Goods.xview, width=20)
        self.my_scrollbar.pack(side=BOTTOM, fill=X)

        self.btnreset = Button(self.header, text="Reset", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.reset_page()])
        self.btnreset.place(x=20, y=13)
        self.btndestroy = Button(self.header, text="Destroy", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.bg.pack_forget(),self.my_scrollbar.pack_forget(),self.List_Goods.pack_forget()])
        self.btndestroy.place(x=20, y=43)

        self.List_Goods.configure(xscrollcommand=self.my_scrollbar.set)

        self.second_frame = tk.Frame(self.List_Goods, bg="White")
        self.second_frame.bind('<Configure>',
                               lambda e: self.List_Goods.configure(scrollregion=self.List_Goods.bbox("all")))
        self.List_Goods.create_window((40, 360), window=self.second_frame, anchor="nw")
        self.second_frame.update()

        self.Goodsimg = []
        for i in range(self.q.return_size()):
             self.Goodsimg.append("")

        for i in range(self.q.return_size()) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(self.q.return_id(i))])


        # content
        for i in range(0, self.q.return_size()):
            info = Label(self.second_frame, image=self.infoimage, width=535, height=636)
            info.pack(side=LEFT, padx=50, pady=0)
            Goods_img = tk.Label(info,image=self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=31,y =18)
            Name = Label(info, text=dict_name[str(self.q.return_id(i))], bg="#ECC5BE", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=30, y=380)
            Prices = Label(info, text=str(dict_price[str(self.q.return_id(i))]) + "   Bath", bg="#E09292", fg="White", font=self.Myfont(50))
            Prices.place(x=30, y=520)
            btnadd = Button(info, image=self.btnaddimage, bg="#E09292", borderwidth=0, text=str(self.q.return_id(i)))
            btnadd.place(x=380, y=497)
            btnadd.bind("<Button-1>", self.on_click)
        # render
        # self.header.place(x=0,y=0)
        # self.content.grid(column=0,row=1)

    def on_click(self, e):
        self.selected = e.widget["text"]
        list_id = list_cart.list_name()
        if not self.selected in list_id :
            pack = [self.selected , 0]
            list_cart.enQueue(pack)
        #print(self.selected)
        if not self.selected in self.pricepcr.keys():
            self.pricepcr[self.selected] = 0
        list_cart.Add_Amount(self.selected)

        self.pricepcr[self.selected] = list_cart.return_amount(self.selected) * int(dict_price[str(self.selected)])
        self.pricetotal = sum(self.pricepcr.values())
        Price = Label(self.header, text=str(self.pricetotal) + "    Bath", bg="#ECC5BE", fg="#849D8A",font=self.Myfont(40))
        Price.place(x=1681, y=217)
        #print(list_cart)
        #print(self.pricetotal)

    def click_tydown(self, e):
        self.hide_all_frame()
        sorted_type = self.q.bubble_sort_ByType()
        print(sorted_type)
        self.Goodsimg = []
        for i in range(len(sorted_type)):
             self.Goodsimg.append("")
        for i in range(len(sorted_type)) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(sorted_type[i][0])])

        for i in range(len(sorted_type)):
            info = Label(self.second_frame, image=self.infoimage, width=535, height=636)
            info.pack(side=LEFT, padx=50, pady=0)
            Goods_img = tk.Label(info,image=self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=31,y =18)
            Name = Label(info, text=dict_name[str(sorted_type[i][0])] , bg="#ECC5BE", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=30, y=380)
            Prices = Label(info, text=dict_price[str(sorted_type[i][0])] + "   Bath", bg="#E09292", fg="White",
                           font=self.Myfont(50))
            Prices.place(x=30, y=520)
            btnadd = Button(info, image=self.btnaddimage, bg="#E09292", borderwidth=0, text=sorted_type[i][0])
            btnadd.place(x=380, y=497)
            btnadd.bind("<Button-1>", self.on_click) 


    def click_prdown(self, e):
        self.hide_all_frame()
        sorted_price = self.q.bubble_sort_ByPrice()
        self.Goodsimg = []
        for i in range(len(sorted_price)):
             self.Goodsimg.append("")
        for i in range(len(sorted_price)) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(sorted_price[i][0])])
        
        #print(sorted_price)
        for i in range(len(sorted_price)):
            info = Label(self.second_frame, image=self.infoimage, width=535, height=636)
            info.pack(side=LEFT, padx=50, pady=0)
            Goods_img = tk.Label(info,image=self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=31,y =18)
            Name = Label(info, text=dict_name[str(sorted_price[i][0])] , bg="#ECC5BE", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=30, y=380)
            Prices = Label(info, text=dict_price[str(sorted_price[i][0])] + "   Bath", bg="#E09292", fg="White",
                           font=self.Myfont(50))
            Prices.place(x=30, y=520)
            btnadd = Button(info, image=self.btnaddimage, bg="#E09292", borderwidth=0, text=sorted_price[i][0])
            btnadd.place(x=380, y=497)
            btnadd.bind("<Button-1>", self.on_click) 

    def click_total(self, e):
        self.hide_all_frame()
        sorted_total = self.q.bubble_sort_ByTotal()
        self.Goodsimg = []
        for i in range(self.q.return_size()):
            self.Goodsimg.append("")
        for i in range(self.q.return_size()) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(self.q.return_id(i))])

        print("sort by total")
        print(sorted_total)
        for i in range(len(sorted_total)):
            info = Label(self.second_frame, image=self.infoimage, width=535, height=636)
            info.pack(side=LEFT, padx=50, pady=0)
            Goods_img = tk.Label(info,image=self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=31,y =18)
            Name = Label(info, text=dict_name[str(sorted_total[i][0])], bg="#ECC5BE", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=30, y=380)
            Prices = Label(info, text=dict_price[str(sorted_total[i][0])] + "   Bath", bg="#E09292", fg="White", font=self.Myfont(50))
            Prices.place(x=30, y=520)
            btnadd = Button(info, image=self.btnaddimage, bg="#E09292", borderwidth=0, text=sorted_total[i][0])
            btnadd.place(x=380, y=497)
            btnadd.bind("<Button-1>", self.on_click)


    def hide_all_frame(self):
        for widget in self.second_frame.winfo_children():
            widget.destroy()
        self.second_frame.pack_forget()
        self.second_frame.place_forget()


    def click_search(self, e):
        self.hide_all_frame()
        typed = self.my_entry.get()
        print(typed)
        count = 0
        for i in range(self.q.return_size()):
            if typed.lower() in dict_name[str(self.q.return_id(i))].lower():
                info = Label(self.second_frame, image=self.infoimage, width=535, height=636)
                info.pack(side=LEFT, padx=50, pady=0)
                Name = Label(info, text=dict_name[str(self.q.return_id(i))], bg="#ECC5BE", fg="#849D8A", font=self.Myfont(50))
                Name.place(x=30, y=380)
                Prices = Label(info, text=str(dict_price[str(self.q.return_id(i))]) + "   Bath", bg="#E09292", fg="White",
                                   font=self.Myfont(50))
                Prices.place(x=30, y=520)
                btnadd = Button(info, image=self.btnaddimage, bg="#E09292", borderwidth=0, text=str(self.q.return_id(i)))
                btnadd.place(x=380, y=497)
                btnadd.bind("<Button-1>", self.on_click)


class Cartpage(tk.Frame):

    def Updates(self,event):
    
            event.widget.update_idletasks()
            event.widget.update()

    def reset_page(self) :
        
        self.refresh(self.parent,self.controller)
        self.controller.show_frame("Cartpage")
        

    def refresh(self,parent, controller):

        # list_cart.enQueue(["112",12])

        self.bg = Label(self)
        self.bg.pack(pady=140,fill=BOTH, expand=1)
        # header
        self.headerimg = PhotoImage(file="bgcart.png")
        self.header = Label(self, image=self.headerimg,height =130)
        self.header.place(x=0, y=0)
        #
        self.btnback = Button(self.header, text="back", bg="#ECC5BE", fg="White", borderwidth=0,
                              command=lambda: controller.show_frame("Secondpage"), font=self.Myfont(50))
        self.btnback.place(x=48, y=13)
        self.recdown = PhotoImage(file="Rectangle 25.png")
        self.test=Label(self, image=self.recdown,height =130)
        self.test.place(x=0, y=900)
        self.totalprice = Label(self,text="SubTotal : ",bg="#ECC5BE", font=self.Myfont(50),fg="#849D8A")
        self.totalprice.place(x=400,y=920)
        self.buttcheckout =PhotoImage(file="Group 13.png")

        self.btncheckout = Button(self,image = self.buttcheckout,bg="#ECC5BE",bd=0,command=lambda: controller.show_frame("CheckoutPage"))
        self.btncheckout.place(x=1270,y=900)
        

        self.List_Goods = tk.Canvas(self.bg, bg="White", highlightthickness=0, bd=0)
        self.List_Goods.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.List_Goods.yview_moveto(1)
        self.List_Goods.update()

        self.my_scrollbar = tk.Scrollbar(self.bg, orient=VERTICAL, command=self.List_Goods.yview, width=20)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        self.btnreset = Button(self.header, text="Reset", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.reset_page(),self.total_price()])
        self.btnreset.place(x=20, y=13)
        self.btndestroy = Button(self.header, text="Destroy", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.bg.pack_forget(),self.my_scrollbar.pack_forget(),self.List_Goods.pack_forget()])
        self.btndestroy.place(x=20, y=43)

        self.List_Goods.configure(yscrollcommand=self.my_scrollbar.set)

        self.second_frame = tk.Frame(self.List_Goods, bg="White")
        self.second_frame.bind('<Configure>',
                               lambda e: self.List_Goods.configure(scrollregion=self.List_Goods.bbox("all")))
        self.List_Goods.create_window((40, 0), window=self.second_frame, anchor="nw")
        self.second_frame.update()

        self.infoimage = PhotoImage(file="Rectangle 52.png")
        self.frameimageadd = PhotoImage(file="Rectangle 29_0.png")
        self.bgimagegoods = PhotoImage(file="Rectangle 23.png")

        self.integer = []
        for i in range(0,list_cart.return_size()):
            set_int = list_cart.return_amount(list_cart.return_id(i))
            self.integer.append(IntVar())
            self.integer[i].set(set_int)

        self.price = tk.IntVar()
        self.price.set(0)
        self.Updates
        
        self.Goodsimg = []
        for i in range(list_cart.return_size()):
             self.Goodsimg.append("")

        for i in range(list_cart.return_size()) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(list_cart.return_id(i))])

        for i in range(0, list_cart.return_size()):
            info = Label(self.second_frame, image=self.infoimage, width=1920, height=254)
            info.pack(pady=15)
            Name = Label(info, text=dict_name[str(list_cart.return_id(i))], bg="White", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=815, y=15)
            imagegoods = Label(info,image = self.Goodsimg[i],bg="White")
            imagegoods.place(x=150,y=0)
            Prices = Label(info, text=str(dict_price[str(list_cart.return_id(i))]) + "   Bath", bg="White", fg="#849D8A", font=self.Myfont(50))
            Prices.place(x=815, y=100)
            frameimageadd = Label(info, image=self.frameimageadd ,bg = "White")
            frameimageadd.place(x=1368,y=15)
            self.entry0 = tk.Entry(info, textvariable=str(self.integer[i]),justify="center", width=4,font=self.Myfont(50),bd=0)
            self.entry0.place(x=1525,y=55)
            self.btnadd = tk.Button(info, text='+', bg="white",width=3,font=self.Myfont(45),bd=0,command=self.plus_one)
            self.btnadd.place(x=1400,y=35)
            self.btnminus = tk.Button(info, text='-', bg="white", width=3, font=self.Myfont(45), bd=0,command=self.take_one)
            self.btnminus.place(x=1670, y=35)
            self.Updates
        self.entry1 = tk.Entry(self, textvariable=str(self.price), justify="center", width=4,
                                   font=self.Myfont(50), bd=0,bg="#ECC5BE",fg="#849D8A")
        self.entry1.place(x=700,y=920)
        self.bath = Label(self,text="Bath",bg="#ECC5BE", font=self.Myfont(50),fg="#849D8A")
        self.bath.place(x=900,y=920)
    
    

    def __init__(self,parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self,parent)
        self.bg = Label(self)
        self.bg.pack(pady=140,fill=BOTH, expand=1)
        # header
        self.headerimg = PhotoImage(file="bgcart.png")
        self.header = Label(self, image=self.headerimg,height =130)
        self.header.place(x=0, y=0)
        #
        self.btnback = Button(self.header, text="back", bg="#ECC5BE", fg="White", borderwidth=0,
                              command=lambda: controller.show_frame("Secondpage"), font=self.Myfont(50))
        self.btnback.place(x=48, y=13)
        self.recdown = PhotoImage(file="Rectangle 25.png")
        self.test=Label(self, image=self.recdown,height =130)
        self.test.place(x=0, y=900)
        self.totalprice = Label(self,text="SubTotal : ",bg="#ECC5BE", font=self.Myfont(50),fg="#849D8A")
        self.totalprice.place(x=400,y=920)
        self.buttcheckout =PhotoImage(file="Group 13.png")

        self.btncheckout = Button(self,image = self.buttcheckout,bg="#ECC5BE",bd=0,command=lambda: controller.show_frame("CheckoutPage"))
        self.btncheckout.place(x=1270,y=900)
        

        self.List_Goods = tk.Canvas(self.bg, bg="White", highlightthickness=0, bd=0)
        self.List_Goods.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.List_Goods.yview_moveto(1)
        self.List_Goods.update()

        self.my_scrollbar = tk.Scrollbar(self.bg, orient=VERTICAL, command=self.List_Goods.yview, width=20)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.btnreset = Button(self.header, text="Reset", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.reset_page(),self.total_price()])
        self.btnreset.place(x=20, y=43)
        
        self.btndestroy = Button(self.header, text="Destroy", bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.bg.pack_forget(),self.my_scrollbar.pack_forget(),self.List_Goods.pack_forget()])
        self.btndestroy.place(x=20, y=13)

        self.List_Goods.configure(yscrollcommand=self.my_scrollbar.set)

        self.second_frame = tk.Frame(self.List_Goods, bg="White")
        self.second_frame.bind('<Configure>',
                               lambda e: self.List_Goods.configure(scrollregion=self.List_Goods.bbox("all")))
        self.List_Goods.create_window((40, 0), window=self.second_frame, anchor="nw")
        self.second_frame.update()

        self.infoimage = PhotoImage(file="Rectangle 52.png")
        self.frameimageadd = PhotoImage(file="Rectangle 29_0.png")
        self.bgimagegoods = PhotoImage(file="Rectangle 23.png")

        self.integer = []
        for i in range(0,list_cart.return_size()):
            set_int = list_cart.return_amount(list_cart.return_id(i))
            self.integer.append(IntVar())
            self.integer[i].set(set_int)

        self.price = tk.IntVar()
        self.price.set(0)

        self.Goodsimg = []
        for i in range(list_cart.return_size()):
             self.Goodsimg.append("")

        for i in range(list_cart.return_size()) :
            self.Goodsimg[i] = PhotoImage(file= dict_img[str(list_cart.return_id(i))])
        
        for i in range(0, list_cart.return_size()):
            info = Label(self.second_frame, image=self.infoimage, width=1920, height=254)
            info.pack(pady=15)
            Name = Label(info, text=dict_name[str(list_cart.return_id(i))], bg="White", fg="#849D8A", font=self.Myfont(50))
            Name.place(x=815, y=15)
            imagegoods = Label(info,image = self.Goodsimg[i],bg="White")
            imagegoods.place(x=277,y=0)
            Prices = Label(info, text=str(dict_price[str(list_cart.return_id(i))]) + "   Bath", bg="White", fg="#849D8A", font=self.Myfont(50))
            Prices.place(x=815, y=100)
            frameimageadd = Label(info, image=self.frameimageadd ,bg = "White")
            frameimageadd.place(x=1368,y=15)
            self.entry0 = tk.Entry(info, textvariable=str(self.integer[i]),justify="center", width=4,font=self.Myfont(50),bd=0)
            self.entry0.place(x=1525,y=55)
            self.btnadd = tk.Button(info, text='+', bg="white",width=3,font=self.Myfont(45),bd=0,command=self.plus_one)
            self.btnadd.place(x=1400,y=35)
            self.btnminus = tk.Button(info, text='-', bg="white", width=3, font=self.Myfont(45), bd=0,command=self.take_one)
            self.btnminus.place(x=1670, y=35)

        self.entry1 = tk.Entry(self, textvariable=str(self.price), justify="center", width=4,
                                   font=self.Myfont(50), bd=0,bg="#ECC5BE",fg="#849D8A")
        self.entry1.place(x=700,y=920)
        self.bath = Label(self,text="Bath",bg="#ECC5BE", font=self.Myfont(50),fg="#849D8A")
        self.bath.place(x=900,y=920)
        

    def total_price(self):
        self.pricepcr = 0
        print("This is Total Price !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for i in range(0,list_cart.return_size()) :
            self.pricepcr += list_cart.return_amount(list_cart.return_id(i)) * int(dict_price[str(list_cart.return_id(i))])
            #print(list_cart)
            #print(self.pricepcr)
        self.price.set(self.pricepcr)
        
    

    def plus_one(self):
        x =  self.integer.get() + 1
        self.integer.set(x)

    def take_one(self):
        if self.integer.get() > 0:
            x =  self.integer.get() - 1
            self.integer.set(x)

    def Myfont(self, sizefont):
        self.myfont = Font(family="Londrina Solid", size=sizefont)
        return self.myfont

class CheckoutPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.label = tk.Label(self,text="Checkpage")

        self.rectop = PhotoImage(file="Group 15.png")
        self.header = Label(self, image=self.rectop)
        self.header.place(x=0, y=0)

        self.bgqrcode = PhotoImage(file="Rectangle 54.png")
        self.bgqr = Label(self, image=self.bgqrcode)
        self.bgqr.place(x=560, y=261)

        self.bgrecdown = PhotoImage(file="Rectangle 32.png")
        self.recdown = Label(self, image=self.bgrecdown)
        self.recdown.place(x=0, y=840)

        self.bgbtncomplete = PhotoImage(file="Group 14.png")
        self.btncomplete = Button(self, image=self.bgbtncomplete,bd=0,bg="#ECC5BE",command=lambda: controller.show_frame("Firstpage"))
        self.btncomplete.place(x=617, y=860)

        self.btnreset = Button(self.header, text="Generate QR Code" , font=("Courier", 25), bg="#ECC5BE", fg="White", borderwidth=0 , command= lambda : [self.text_qr()])
        self.btnreset.place(x=20, y=13)

        

    def text_qr(self) :
        #print("This is QR")
        input_text = list_cart.Text_for_QR()
        #print(input_text)
        self.qr = Label(self)
        self.qr.place(x=710, y=280)
        input_text = list_cart.Text_for_QR()
        #print("This is QR")
        #print(input_text)
        self.delete_shelf()
        self.img = self.create_qrcode(input_text).resize((500, 500))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.qr.configure(image=self.imgTk)
        self.qr.image = self.imgTk
        
    def delete_shelf(self) :
        self.q = queue()
        self.q.resetQueue()
        f = open("Shelf_data.txt" , 'r')
        while(True) :
            s = f.readline()
            if s == '' :
                break        
            s = s.split(',')
            s[0] = int(s[0])
            exp = s[1]
            s[1] = exp[0:-1]
            self.q.enQueue([s[0] , s[1]])
        print(self.q)
        for i in range(list_cart.return_size()) :
            print(list_cart)
            print(list_cart.return_id(i) , list_cart.return_amount(list_cart.return_id(i)))
            for j in range(list_cart.return_amount(list_cart.return_id(i))) :
                self.q.search_and_delete(list_cart.return_id(i))
        #print(self.q)
        print("This is Delete Shelf")
        print(self.q)
        f.close()
        self.new_write()

    def new_write(self) :
        f = open("Shelf_data.txt" , "w+")
        #print(str(self.return_id(0)) + 'kuyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        f.write(str(self.q.return_id(0)) + ',' + str(self.q.return_exp(0)) + '\n' )
        f.close()
        f = open("Shelf_data.txt" , 'a')
        for i in range(1,self.q.return_size()-1) :
            print(str(self.q.return_id(i)) + " " + str(self.q.return_exp(i)))
            f.write(str(self.q.return_id(i)) + ',' + str(self.q.return_exp(i)) + '\n')
        f.close()

    def create_qrcode(self,text):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img


class Contactpage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.label = tk.Label(self,text="Infopage")
        self.bgimage = PhotoImage(file="Contact-01.png")
        self.bg = Label(self, image=self.bgimage)
        self.bg.place(x=0,y=0)
        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self.bg, image = self.backimg,bg="#ff9292",borderwidth=0,command=lambda: controller.show_frame("Firstpage"))
        Back_Btn.place(x=70,y=40)

class Aboutpage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.label = tk.Label(self,text="Aboutpage")
        self.bgimage = PhotoImage(file="About-01.png")
        self.bg = Label(self, image=self.bgimage)
        self.bg.place(x=0,y=0)
        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self.bg, image = self.backimg,bg="#ff9292",borderwidth=0,command=lambda: controller.show_frame("Firstpage"))
        Back_Btn.place(x=70,y=40)

class Firstpage2(tk.Frame): # หน้า buffer
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.start_bth = PhotoImage(file='Group 8.png')
        self.bg = PhotoImage(file = "page1-01 2.png")
        bg = Label(self, image=self.bg)
        bg.place(x=0, y=0)
        str = Label(self, text="Grocery", bg="#E09292", fg="White", font=self.Myfont(130))
        str.place(x=120, y=220)
        str1 = Label(self, text="Store", bg="#E09292", fg="White", font=self.Myfont(130))
        str1.place(x=120, y=400)
        str2 = Label(self, text="Self Check Out ", bg="#E09292", fg="White", font=self.Myfont(60))
        str2.place(x=120, y=620)
        butstart = Button(self, image=self.start_bth, bg="#E09292", borderwidth=0,command=lambda: controller.show_frame("Secondpage"))
        butstart.place(x=125, y=720)
        butabout = Button(self, text="About", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,command=lambda: controller.show_frame("Aboutpage"))
        butabout.place(x=1400, y=55)
        butcon = Button(self, text="Contact", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,command=lambda: controller.show_frame("Infopage"))
        butcon.place(x=1600, y=55)
        butadmin = Button(self, text="Admin", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,command=lambda: controller.show_frame("Admin_Login_Page"))
        butadmin.place(x=134, y=60)


    def Myfont(self,sizefont):
        self.myfont = Font(family="Londrina Solid", size=sizefont)
        return self.myfont

class Firstpage3(tk.Frame): # หน้า buffer
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.start_bth = PhotoImage(file='Group 8.png')
        self.bg = PhotoImage(file = "page1-01 2.png")
        bg = Label(self, image=self.bg)
        bg.place(x=0, y=0)
        str = Label(self, text="Grocery", bg="#E09292", fg="White", font=self.Myfont(130))
        str.place(x=120, y=220)
        str1 = Label(self, text="Store", bg="#E09292", fg="White", font=self.Myfont(130))
        str1.place(x=120, y=400)
        str2 = Label(self, text="Self Check Out ", bg="#E09292", fg="White", font=self.Myfont(60))
        str2.place(x=120, y=620)
        butstart = Button(self, image=self.start_bth, bg="#E09292", borderwidth=0,command=lambda: controller.show_frame("Secondpage"))
        butstart.place(x=125, y=720)
        butabout = Button(self, text="About", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,command=lambda: controller.show_frame("Aboutpage"))
        butabout.place(x=1400, y=55)
        butcon = Button(self, text="Contact", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,command=lambda: controller.show_frame("Infopage"))
        butcon.place(x=1600, y=55)
        butadmin = Button(self, text="Admin", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,command=lambda: controller.show_frame("Admin_Login_Page"))
        butadmin.place(x=134, y=60)


    def Myfont(self,sizefont):
        self.myfont = Font(family="Londrina Solid", size=sizefont)
        return self.myfont

class Firstpage4(tk.Frame): # หน้า buffer
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.start_bth = PhotoImage(file='Group 8.png')
        self.bg = PhotoImage(file="page1-01 2.png")
        bg = Label(self, image=self.bg)
        bg.place(x=0, y=0)
        str = Label(self, text="Grocery", bg="#E09292", fg="White", font=self.Myfont(130))
        str.place(x=120, y=220)
        str1 = Label(self, text="Store", bg="#E09292", fg="White", font=self.Myfont(130))
        str1.place(x=120, y=400)
        str2 = Label(self, text="Self Check Out ", bg="#E09292", fg="White", font=self.Myfont(60))
        str2.place(x=120, y=620)
        butstart = Button(self, image=self.start_bth, bg="#E09292", borderwidth=0,
                          command=lambda: controller.show_frame("Secondpage"))
        butstart.place(x=125, y=720)
        butabout = Button(self, text="About", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,
                          command=lambda: controller.show_frame("Aboutpage"))
        butabout.place(x=1400, y=55)
        butcon = Button(self, text="Contact", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,
                        command=lambda: controller.show_frame("Infopage"))
        butcon.place(x=1600, y=55)
        butadmin = Button(self, text="Admin", fg="#849D8A", bg="#ECC5BE", font=self.Myfont(30), borderwidth=0,
                          command=lambda: controller.show_frame("Admin_Login_Page"))
        butadmin.place(x=134, y=60)

    def Myfont(self, sizefont):
        self.myfont = Font(family="Londrina Solid", size=sizefont)
        return self.myfont





    


class Admin_Login_Page(tk.Frame): # หน้า log in

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg = PhotoImage(file="newbg.png")
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.usericn = PhotoImage(file="Admin.png")
        self.passicn = PhotoImage(file="Lock.png")
        label = tk.Label(self, image= self.bg )
        label.place(x=0, y=0)

        my_text = tk.Label(self,image=self.pixelVirtual, text="Admin Login", fg="white",bg="#849D8A", width=645, height=140,compound="c")
        my_text.pack(pady=429)
        my_text.configure(font = Font_tuple1)
 
        LoginRec = Frame(self,bg="white",width=651,height=440)
        LoginRec.place(x=634,y=573)

        line = Frame(self,bg="#849D8A",width=520,height=2)
        line.place(x=706,y=712)

        self.Usernamedef = tk.StringVar()
        self.Usernamedef.set("USERNAME")
        Username = Entry(self,bd=0,textvariable=self.Usernamedef)
        Username.bind("<Button-1>", self.on_click1)
        Username.bind("<Key>", self.on_click1)
        Username.bind("<Leave>",self.off_click1)
        Username.place(x=867,y=610,width=400)
        self.Usernamedef.trace("w", lambda *args: self.character_limit(self.Usernamedef))
        Username.configure(font = ("Londrina Solid Black",36),fg ="#A5ABC7")

        self.Passworddef = tk.StringVar()
        self.Passworddef.set("PASSWORD")
        Password = Entry(self,bd=0,textvariable=self.Passworddef)
        Password.bind("<Button-1>", self.on_click2)
        Password.bind("<Key>", self.on_click2)
        # Password.bind("<Key>", Password.config(show="*"))
        Password.bind("<Leave>",self.off_click2)
        Password.place(x=867,y=750,width=400)
        
        self.Passworddef.trace("w", lambda *args: self.character_limit(self.Passworddef))
        Password.configure(font = ("Londrina Solid Black",36),fg ="#A5ABC7")

        LoginBtn = Button(self,image=self.pixelVirtual,text= "Login",font = ("Londrina Solid Black",64) ,width=647, height=100,compound="c", fg="white",bg="#849D8A",borderwidth=0,
        command = self.submit)
        LoginBtn.place(x=634,y=840)

        usericn_label = Label(self, image=self.usericn, width=63,height=77,borderwidth=0,bg = "white",)
        usericn_label.place(x=740, y=595)

        passicn_label = Label(self, image=self.passicn, width=63,height=77,borderwidth=0,bg = "white")
        passicn_label.place(x=740, y=735)

        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Firstpage"),width = 150)
        Back_Btn.place(x=70,y=40)

        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("Admin_Management_Page"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("Stock_Page"))
        # button1.place(x=500, y=700)
        # button2.place(x=500, y=500)
    
    def on_click1(self,event):
        if self.Usernamedef.get() == "USERNAME" :
            event.widget.delete(0, tk.END)
        


    def on_click2(self,event):
        
        if self.Passworddef.get() == "PASSWORD" :
            event.widget.delete(0, tk.END)
        
        
    def off_click1(self,event):
        if self.Usernamedef.get() == "" :
            event.widget.insert(0, "USERNAME")

        

    def off_click2(self,event):
        if self.Passworddef.get() == "" :
            event.widget.insert(0, "PASSWORD")
        

    def character_limit(self,entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[:14])

    def submit(self):
        self.name = self.Usernamedef.get()
        self.password = self.Passworddef.get()
        
        self.correctname =[]
        self.correctpass = []
        #print("The name is : " + self.name)
        #print("The password is : " + self.password)

        self.Usernamedef.set("USERNAME")
        self.Passworddef.set("PASSWORD")
        # Password.config(show="")
        self.Wrongtext = tk.StringVar()
        WronngLabel = Label(self,font = ("Londrina Solid Black",24),textvariable=self.Wrongtext,fg = "#C04B4B",bg ="#FFFFFF",width=45,height=1)
        
        self.l = [] 
        f = open('Admin_data.txt' , 'r')
        while True:
            s = f.readline()
            if s == '' :
                break
            self.l.append(s[0:-1])
            print(self.l)
        f.close() 
        for i in self.l:
            i = i.split(" ")
            self.correctname.append(i[0])
            self.correctpass.append(i[1])
        if  self.name == "USERNAME" and  self.password == "PASSWORD":
            
            self.Wrongtext.set("*Please enter your Username and Password")

        elif self.name == "USERNAME" and self.password != "PASSWORD":
            self.Wrongtext.set("*Please enter your Username")

        elif self.name != "USERNAME" and self.password == "PASSWORD":
            self.Wrongtext.set("*Please enter your Password")

        elif self.name in self.correctname :
            if self.password == self.correctpass[self.correctname.index(self.name)]:
                self.Wrongtext.set("Welcome")
                read_file()
                self.controller.show_frame("Admin_Management_Page")
            else:
                self.Wrongtext.set("*Username or Password incorrect")
        else :
            self.Wrongtext.set("*Username or Password incorrect")
        WronngLabel.place(x=960,y=976,anchor = "center")

class Admin_Login_Page2(tk.Frame): # หน้า buffer ไม่ต้องสนใจ

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bg = PhotoImage(file="newbg.png")
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.usericn = PhotoImage(file="Admin.png")
        self.passicn = PhotoImage(file="Lock.png")
        label = tk.Label(self, image= self.bg )
        label.place(x=0, y=0)

        my_text = tk.Label(self,image=self.pixelVirtual, text="Admin Login", fg="white",bg="#849D8A", width=645, height=140,compound="c")
        my_text.pack(pady=429)
        my_text.configure(font = Font_tuple1)
 
        LoginRec = Frame(self,bg="white",width=651,height=440)
        LoginRec.place(x=634,y=573)

        line = Frame(self,bg="#849D8A",width=520,height=2)
        line.place(x=706,y=712)

        self.Usernamedef = tk.StringVar()
        self.Usernamedef.set("USERNAME")
        Username = Entry(self,bd=0,textvariable=self.Usernamedef)
        Username.bind("<Button-1>", self.on_click1)
        Username.bind("<Key>", self.on_click1)
        Username.bind("<Leave>",self.off_click1)
        Username.place(x=867,y=610,width=400)
        self.Usernamedef.trace("w", lambda *args: self.character_limit(self.Usernamedef))
        Username.configure(font = ("Londrina Solid Black",36),fg ="#A5ABC7")

        self.Passworddef = tk.StringVar()
        self.Passworddef.set("PASSWORD")
        Password = Entry(self,bd=0,textvariable=self.Passworddef)
        Password.bind("<Button-1>", self.on_click2)
        Password.bind("<Key>", self.on_click2)
        # Password.bind("<Key>", Password.config(show="*"))
        Password.bind("<Leave>",self.off_click2)
        Password.place(x=867,y=750,width=400)
        
        self.Passworddef.trace("w", lambda *args: self.character_limit(self.Passworddef))
        Password.configure(font = ("Londrina Solid Black",36),fg ="#A5ABC7")

        LoginBtn = Button(self,image=self.pixelVirtual,text= "Login",font = ("Londrina Solid Black",64) ,width=647, height=100,compound="c", fg="white",bg="#849D8A",borderwidth=0,
        command = self.submit)
        LoginBtn.place(x=634,y=840)

        usericn_label = Label(self, image=self.usericn, width=63,height=77,borderwidth=0,bg = "white",)
        usericn_label.place(x=740, y=595)

        passicn_label = Label(self, image=self.passicn, width=63,height=77,borderwidth=0,bg = "white")
        passicn_label.place(x=740, y=735)

        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("Admin_Management_Page"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("Stock_Page"))
        # button1.place(x=500, y=700)
        # button2.place(x=500, y=500)
    
    def on_click1(self,event):
        if self.Usernamedef.get() == "USERNAME" :
            event.widget.delete(0, tk.END)
        


    def on_click2(self,event):
        
        if self.Passworddef.get() == "PASSWORD" :
            event.widget.delete(0, tk.END)
        
        
    def off_click1(self,event):
        if self.Usernamedef.get() == "" :
            event.widget.insert(0, "USERNAME")

        

    def off_click2(self,event):
        if self.Passworddef.get() == "" :
            event.widget.insert(0, "PASSWORD")
        

    def character_limit(self,entry_text):
        if len(self.entry_text.get()) > 0:
            self.entry_text.set(self.entry_text.get()[:14])

    def submit(self):
        
        self.name = self.Usernamedef.get()
        self.password = self.Passworddef.get()
        
        self.l = ['Rapeepat 1234','Jhon 5678','Jimmy 5555']
        self.correctname =[]
        self.correctpass = []
        #print("The name is : " + self.name)
        #print("The password is : " + self.password)

        self.Usernamedef.set("USERNAME")
        self.Passworddef.set("PASSWORD")
        # Password.config(show="")
        self.Wrongtext = tk.StringVar()
        WronngLabel = Label(self,font = ("Londrina Solid Black",24),textvariable=self.Wrongtext,fg = "#C04B4B",bg ="#FFFFFF",width=45,height=1)
        
        for i in self.l:
            i = i.split(" ")
            self.correctname.append(i[0])
            self.correctpass.append(i[1])
        if  self.name == "USERNAME" and  self.password == "PASSWORD":
            
            self.Wrongtext.set("*Please enter your Username and Password")

        elif self.name == "USERNAME" and self.password != "PASSWORD":
            self.Wrongtext.set("*Please enter your Username")

        elif self.name != "USERNAME" and self.password == "PASSWORD":
            self.Wrongtext.set("*Please enter your Password")

        elif self.name in self.correctname :
            if self.password == self.correctpass[self.correctname.index(self.name)]:
                self.Wrongtext.set("Welcome")
                self.controller.show_frame("Admin_Management_Page")
            else:
                self.Wrongtext.set("*Username or Password incorrect")
        else :
            self.Wrongtext.set("*Username or Password incorrect")
        WronngLabel.place(x=960,y=976,anchor = "center")

class Admin_Management_Page(tk.Frame): # หน้า Management

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        bg = tk.Frame(self, bg = "#D6CEA7",width = "1920",height="1080")
        bg.place(x=0,y=0)

        Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="210")
        Header_Bar.pack()

        border_color = tk.Frame(self, background="#4C6A53",bd = 5)
        Header_Label = tk.Label(border_color,bd = 5  ,bg = "#849D8A", text= "Admin Management", fg = "#FFFFFF",width = 18)
        Header_Label.configure(font = Font_tuple2)
        Header_Label.pack(padx=1,pady=1)
        border_color.place(x=124,y=22)

        self.stockimg = PhotoImage(file="stock-01 1.png")
        self.shelfimg = PhotoImage(file="shelf-01 1.png")
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)

        Stock_Frame = tk.Label(self, image = self.stockimg,bg ="#D6CEA7")
        Stock_Frame.place(x =300,y =250)

        Shelf_Frame = tk.Label(self, image = self.shelfimg,bg ="#D6CEA7")
        Shelf_Frame.place(x = 1150,y =270)

        Stock_Btn = tk.Button(self, text ="Stock",font = ("Londrina Solid Black",64),image=self.pixelVirtual,width = 369, height = 110,fg ="#FFFFFF", bg ="#849D8A",compound="c",borderwidth=0,command=lambda: controller.show_frame("Stock_Page"))
        Stock_Btn.place(x=410,y=887)

        Shelf_Btn = tk.Button(self, text ="Shelf",font = ("Londrina Solid Black",64),image=self.pixelVirtual,width = 369, height = 110,fg ="#FFFFFF", bg ="#849D8A",compound="c",borderwidth=0,command=lambda: controller.show_frame("Shelf_Page"))
        Shelf_Btn.place(x=1220,y=887)

        Logout_Btn = tk.Button(self, text ="Log Out", font = ("Londrina Solid Black",36), image=self.pixelVirtual,width = 200, height = 60,fg ="#FFFFFF", bg ="#849D8A",compound="c",borderwidth=0,command=lambda: controller.show_frame("Admin_Login_Page"))
        Logout_Btn.place(x=1695,y=973)


class Node :
    def __init__(self,id_stock = None, exp = None) :
        self.id_stock = id_stock
        self.exp = exp
        self.next =None

class linkedlist :
    def __init__(self) :
        self.head = None
        self.tail = None
    
    def __str__(self) :
        if self.head == None :
            return "Empty"
        else :
            All_data,current = str(self.head.id_stock) + ' ' + str(self.head.exp) + ' ' , self.head
            while current.next != None :
                current = current.next
                All_data += str(current.id_stock) + ' '  + str(current.exp) + ' '
            return All_data
    
    def print_linkedlist(self) :
        if self.head == None :
            return "Empty"
        else :
            All_data,current = str(self.head.id_stock) + ' ' + str(self.head.exp) + ' ' , self.head
            while current.next != None :
                current = current.next
                All_data += str(current.id_stock) + ' '  + str(current.exp) + ' '
        print(All_data)
    
    def append(self,id_stock,exp) :
        data = Node(id_stock,exp)
        if self.head == None :
            self.head = data
            self.tail = data
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = data
            self.tail = t.next

    def insert(self,id_stock,exp) :
        data = Node(id_stock,exp)
        t = self.head
        #print("Linkedlist Insert!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if t.next == None :
            t.next = data
        while t.next != None :
            if int(id_stock) > int(t.id_stock) and int(id_stock) <= int(t.next.id_stock) :
                p = t.next
                t.next = data
                data.next = p
                break
            t = t.next
        if t.next == None :
            t.next = data

    def search_and_delete(self,item) :
        t = self.head
        if self.head == None :
            return "Not Found"
        while t != None :
            if int(t.id_stock) == int(item) :
                if t == self.head :
                    self.head = t.next
                    break
                elif t == self.tail :
                    t.previous.next = None
                    self.tail = t.previous
                    break
                else :
                    t.previous.next = t.next
                    t.next.previous = t.previous
                    break
            t = t.next
        return "Not Found"


    def size(self) :
        t = self.head
        count = 0
        while t != None :
            t = t.next
            count += 1
        return count

    def list_id(self) :
        id_stock = []
        if self.head == None :
            #return None
            return id_stock
        else :
            t = self.head
            while t != None :
                id_stock.append(int(t.id_stock))
                t = t.next
            return id_stock

    def list_name(self) :
        name = []
        if self.head == None :
            #return None
            return name
        else :
            t = self.head
            while t != None :
                name.append(dict_name[str(int(t.id_stock) // 100)])
                t = t.next
            return name
    
    def list_price(self) :
        price = []
        
        if self.head == None :
            #return None
            return price    
        else :
            t = self.head
            while t != None :
                price.append(dict_price[str(int(t.id_stock) // 100)])
                t = t.next
            return price

    def list_img(self) :
        img = []
        
        if self.head == None :
            #return None
            return img
        else :
            t = self.head
            while t != None :
                img.append(dict_img[str(int(t.id_stock) // 100)])
                t = t.next
            return img

    def list_Exp(self) :
        Exp = []
        if self.head == None :
            #return None
            return Exp
        else :
            t = self.head
            while t != None :
                Exp.append(t.exp)
                t = t.next
            return Exp

    def return_id(self,num) :
        if num == 0 and self.head != None :
                return self.head.id_stock
        elif num == -1:
            return self.tail.id_stock
        else :
            count = 0
            t = self.head
            while t != None :
                if num == count :
                    return t.id_stock
                t = t.next
                count += 1

    def return_exp(self,num) :
        if num == 0 and self.head != None:
            return self.head.exp
        else :
            count = 0
            t = self.head
            while t != None :
                if num == count :
                    return t.exp
                t = t.next
                count += 1
        
    def bubble_sort(self):
        t = self.head
        while t.next != None :
            t2 = self.head
            while t2.next != None :
                if t2.id_stock >= t2.next.id_stock :
                    t2.id_stock , t2.next.id_stock = t2.next.id_stock , t2.id_stock
                    t2.exp , t2.next.exp = t2.next.exp , t2.exp
                t2 = t2.next
            t = t.next
        return self.head

    def append_and_sort_by_exp(self,id_stock,exp) :
        exp_for_calculate = exp.split('/')
        #print(exp[2],exp[1],exp[0])
        calculate_exp = (int(exp_for_calculate[2]) + (int(exp_for_calculate[1]) / 100) + (int(exp_for_calculate[0]) / 10000))//0.0001
        #print(str(calculate_exp) + '\n')
        data = Node(id_stock,exp)
        if self.head == None :
            self.head = data
            self.tail =self.head
        else :
            t = self.head
            #print(t.exp)
            if t.next == None :
                exp_node = t.exp.split('/')
                calculate_exp_node = (int(exp_node[2]) + (int(exp_node[1]) / 100) + (int(exp_node[0]) / 10000))//0.0001
               #print("Exp node is " + str(calculate_exp_node))
                if int(id_stock) >= int(self.head.id_stock) :
                    if calculate_exp >= calculate_exp_node :
                        t.next = data
                        t.next.previous = t
                        self.tail = t.next
                    else :
                        self.head = data
                        self.head.next = t
                        self.head.next.previous = self.head
                        self.tail = self.head.next
                else :
                    self.head = data
                    self.head.next = t
                    self.head.next.previous = self.head
                    self.tail = self.head.next
            else :
                #print("While loop!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                #print(self.list_name())
                t = self.head
                while t.next != None :
                    exp_node = t.exp.split('/')
                    calculate_exp_node = (int(exp_node[2]) + (int(exp_node[1]) / 100) + (int(exp_node[0]) / 10000))//0.0001
                    if int(id_stock)//100 <= int(t.id_stock)//100 :
                        if int(id_stock)//100 < int(t.id_stock)//100 :
                            p = t
                            if t == self.head :
                                self.head = data
                                self.head.next = t
                                t2 = self.head.next
                                t2.previous = self.head
                                break
                            else :
                                t.previous.next = data
                                t2 = t.previous.next
                                t2.previous = t.previous
                                t2.next = p
                                t2.next.previous = t2
                                break
                        elif int(id_stock)//100 == int(t.id_stock)//100 :
                            if calculate_exp < calculate_exp_node :
                                if t == self.head :
                                    self.head = data
                                    self.head.next = t
                                    t.previous = self.head
                                    break
                                else :
                                    p = t
                                    t.previous.next = data
                                    t2 = t.previous.next
                                    t2.previous = t.previous
                                    t2.next = t
                                    break
                            else :
                                p = t.next
                                t.next = data
                                t.next.previous = t
                                t.next.next = p
                                break
                    else :
                        if t.next == None :
                            t.next = data
                            t.next.previous = t
                            self.tail = t.next
                            break
                        else :
                            t = t.next
                            if t.next == None :
                                if int(id_stock) < int(t.id_stock) :
                                    p = t
                                    t.previous.next = data
                                    t2 = t.previous.next
                                    t2.next = p
                                    t2.previous = t.previous
                                    t2.next.previous = t2
                                    self.tail = t2.next
                                    break
                                else :
                                    if calculate_exp < calculate_exp_node :
                                        p = t
                                        t.previous.next = data
                                        t2 = t.previous.next
                                        t2.previous = t.previous
                                        t2.next = p
                                        break
                                    else :
                                        t.next = data
                                        t.next.previous = t
                                        break

    def write_file_shelf(self) :
        f = open("Shelf_data.txt" , "w+")
        #print(str(self.return_id(0)) + 'kuyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        f.write(str(int(self.return_id(0)) // 100) + ',' + str(self.return_exp(0)) + '\n' )
        f.close()
        f = open("Shelf_data.txt" , 'a')
        for i in range(1,self.size()) :
            f.write(str(int(self.return_id(i)) // 100) + ',' + str(self.return_exp(i)) + '\n')
        f.close()
        print(self)
    
    def write_file_stock(self) :
        f = open("Stock_data.txt" , "w+")
        f.write(str(self.return_id(0)) + ',' + str(self.return_exp(0)) + '\n' )
        f.close()
        f = open("Stock_data.txt" , 'a')
        for i in range(1,self.size()) :
            f.write(str(self.return_id(i)) + ',' + str(self.return_exp(i)) + '\n')
        f.close()
        print(self)

    def clear(self) :
        self.head = None
        self.tail = None

class queue :
    def __init__(self,q = []) :
        self.q = q
        self.count = 0

    def __str__(self) :
        return str(self.q)

    def enQueue(self,id_shelf) :
        self.q.append(id_shelf)
        self.count += 1

    def deQueue(self) :
        if self.count > 0 :
            pop = self.q.pop[0]
            return pop 
        else :
            return "Empty"
        
    def resetQueue(self) :
        self.q = []

    def list_name(self) :
        name = []
        count_while = 0
        while count_while != self.count :
            name.append(self.q[count_while][0])
            count_while += 1
        return name

    def list_exp(self) :
        exp = []
        count_while = 0
        while count_while != self.count :
            exp.append(self.q[count_while][1])
            count_while += 1
        return exp

    def return_id(self,i) :
        return int(self.q[i][0])
    
    def return_exp(self,i):
        return self.q[i][1]

    def return_size(self) :
        return self.count

    def return_amount(self,id_shelf) :
        count = 0
        while count != self.return_size() :
            if str(self.q[count][0]) == str(id_shelf) :
                return int(self.q[count][1])
            count +=1 

    def bubble_sort_ByPrice(self) :
        print("Bubble_sort_ByPrice")
        for i in range(self.return_size()) :
           # print("this is i = " + str(i) + '\n')
            for j in range(self.return_size()-1) :
               # print("this is j = " + str(j) + '\n')
                before = int(dict_price[str(self.q[j][0])])
                after = int(dict_price[str(self.q[j+1][0])])
                if before >= after :
                    save = self.q[j]
                    self.q[j] = self.q[j+1]
                    self.q[j+1] = save
        return self.q

    def bubble_sort_ByType(self) :
        for i in range(self.return_size()) :
            #print("Work i")
            for j in range(self.return_size() - 1) :
                #print("Work j")
                before = int(self.q[j][0])
                after = int(self.q[j+1][0])
                if before >= after :
                    #print("IF Work")
                    save = self.q[j]
                    self.q[j] = self.q[j+1]
                    self.q[j+1] = save
        return self.q
    
    def bubble_sort_ByTotal(self) :
        for i in range(self.return_size()) :
            #print("Work i")
            for j in range(self.return_size() - 1) :
                #print("Work j")
                before = int(self.q[j][1])
                after = int(self.q[j+1][1])
                if before >= after :
                    #print("IF Work")
                    save = self.q[j]
                    self.q[j] = self.q[j+1]
                    self.q[j+1] = save
        return self.q

    def Add_Amount(self,id_shelf) :
        count = 0
        while count != self.return_size() :
            if self.q[count][0] == id_shelf :
                self.q[count][1] += 1
            count +=1 

    def Text_for_QR(self) :
        if self.return_size() > 0 :
            string = str(self.q[0][0]) + ":" + str(self.q[0][1])
            if self.return_size() > 1 :
                for i in range(1,self.return_size()) :
                    string += ","+str(self.q[i][0]) + ":" + str(self.q[i][1]) 
            return string
        else :
            return "Empty"
    
    def search_and_delete(self,id_shelf) :
        count = 0
        while count != self.return_size() :
            if self.return_id(count) == id_shelf :
                self.q.pop(count)
                self.count -= 1
                return self.q
            count += 1
        return self.q

class Stack :
    def __init__(self,s = []) :
        self.s = s

    def __str__(self) :
        return self.s

    def push(self,data) :
        self.s.append(data)
    
    def pop(self) :
        self.s.pop()

    def peek(self) :
        return self.s[-1]
global list_cart
list_cart = queue()

global stock
stock = linkedlist()

class read_file :
    def __init__(self) :
        #print("Read File!!")
        stock.clear()
        f = open("Stock_data.txt" , 'r')
        while(True) :
            s = f.readline()
            if s == '' :
                break
            s = s.split(',')
            #print(s[0])
            exp = s[1]
            stock.append(s[0],exp[0:-1])
            #print(stock)
        f.close()


class Stock_Page(tk.Frame): # หน้า Stock

    def restart(self):
        self.refresh(self.parent,self.controller)
        print("restart")
        self.controller.show_frame("Stock_Page")
        

    def refresh(self,parent, controller):
    
        
        self.bg = tk.Frame(self, bg = "#849D8A",width = "1920",height="1080")
        self.bg.pack(fill = BOTH, expand=1)

        Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="210")
        Header_Bar.place(x=0,y=0)

        restartBtn = Button(Header_Bar, text="Destroy", command= lambda : [self.my_scrollbar.pack_forget(),self.bg.pack_forget(),List_Goods.pack_forget()],bg ="#849D8A",fg="White",relief="flat")
        restartBtn.place(x = 10, y=5)
        refreshBtn = Button(Header_Bar, text="Restart", command= lambda : self.restart(),bg ="#849D8A",fg="White",relief="flat")
        refreshBtn.place(x = 10, y=40)

        List_Goods = tk.Canvas(self.bg,bg="#D6CEA7",highlightthickness = 0,bd =0)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)

        List_Goods.xview_moveto(1)
        List_Goods.update()

        self.my_scrollbar = tk.Scrollbar(self, orient = HORIZONTAL , command = List_Goods.xview,width=20)
        self.my_scrollbar.pack(side=BOTTOM,fill=X)
        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        List_Goods.configure(xscrollcommand=self.my_scrollbar.set)

        self.second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        self.second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((60,365), window = self.second_frame,anchor="nw")
        self.second_frame.update()

        self.selectimg = PhotoImage(file="selection00.png")
        Selct_Label = tk.Label(self.bg, image = self.selectimg,borderwidth=0,bg ="#D6CEA7")
        Selct_Label.place(x=0,y=190)

        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Admin_Management_Page"))
        Back_Btn.place(x=70,y=40)

        self.roundrecimg =  PhotoImage(file="AddStock.png")
        AddStock_Btn = tk.Button(self, image = self.roundrecimg,text = "Add Stock",borderwidth=0,bg="#849D8A",command=lambda: controller.show_frame("Add_Stock_Page"))
        AddStock_Btn.place(x=1500,y=50)

        j = 0

        self.Arrow_Downimg = PhotoImage(file="arrow-down-sign-to-navigate 2.png")

        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 5  ,bg = "#849D8A", text= "Stock", fg = "#FFFFFF",width = 18)
        Header_Label.configure(font = Font_tuple2)
        Header_Label.place(x=960,y=110,anchor="center")

        Types_Frame = tk.Frame(List_Goods,width=450,height=700,bg = "#849D8A")
        Types_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Types_Btn.place(x = 640,y = 23)

        Exp_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Exp_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Exp_Btn.place(x = 1090,y = 23)
        Exp_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessExp_Btn.pack(padx=19,pady = 2)

        LesstoMoreExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Less than to \n More than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreExp_Btn.pack(padx=19,pady = 12)

        ValidExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Valid Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ValidExp_Btn.pack(padx=19,pady = 2)

        ExpireExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Expired Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ExpireExp_Btn.pack(padx=19,pady = 12)

        Amounts_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Amounts_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Amounts_Btn.place(x = 1725,y = 23)
        Amounts_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessAmount_Btn.pack(padx=19,pady = 2)

        LesstoMoreAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Less than to \n more than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreAmount_Btn.pack(padx=19,pady = 12)

        ZeroAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Show Zero \n Amounts", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ZeroAmount_Btn.pack(padx=19,pady = 2)


        Total_Btn = tk.Button(self.bg,image = self.pixelVirtual,text="Total", width=311,height = 100,font = ("Londrina Solid Black",55),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        Total_Btn.place(x=16,y = 210)

        Prices_Header = tk.Label(self.bg,text="Price",font = ("Londrina Solid Black",55),width=10,fg= "#849D8A",bg="#D6CEA7")
        Prices_Header.place(x=1300,y = 213)
    
        #------------------------------ Data ----------------------------------------------------------
        
        
        read_file()
        print("Restart Stock Page!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.Name = stock.list_name()
        self.Price = stock.list_price()
        self.Img = stock.list_img()
        self.Exp = stock.list_Exp()
        #self.Name = ["Coke","Pepsi","Fanta","Est","Mirinda","Sprite","7up","Lipton"]  
        #self.Img = ["Coke.png","Pepsi.png","Fanta.png","Est.png","Mirinda.png","Sprite.png","7up.png","Lipton.png"]     # รูปสินค้า
        #self.Price = [0,1]
        #self.Exp = ["12/12/2010","12/12/2011"]

        #------------------------------------------------------------------------------------------------

        List_Goods.xview_moveto(1)
        List_Goods.update()
        self.second_frame.update()
        
        self.Goods_labelimg = PhotoImage(file="Rectangle 14 .png")
        self.Goods_infoimg = PhotoImage(file="Rectangle 21.png")
        
        # Goods_Label = tk.Label(self.second_frame,image = self.Goods_labelimg,width=535,height=636)
        # Goods_info = tk.Label(Goods_Label,image= self.Goods_infoimg,borderwidth=0)
        
        self.Goodsimg = []
        for i in range(stock.size()):
             self.Goodsimg.append("")

        for i in range(stock.size()) :
            self.Goodsimg[i] = PhotoImage(file= self.Img[i])
    
        print(self.Name)
        for j in range(0,stock.size()):

                List_Goods.update()
                self.second_frame.update() 
                List_Goods.update()
                self.second_frame.update()
                List_Goods.update()
                self.my_scrollbar.bind('<Button-1>' ,self.Updates)

                self.Goods_Label = tk.Label(self.second_frame,image = self.Goods_labelimg,width=535,height=636)
                self.Goods_Label.pack(side =LEFT, padx = 50, pady =0)
                # Goods_Label.pack(side = TOP,pady =400)
                self.Goods_Label.update()
                List_Goods.update()
                self.second_frame.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    

                Goods_img = tk.Label(self.Goods_Label,image= self.Goodsimg[j],borderwidth=0,bg="#FFFFFF")
                # Goods_img.pack(padx=20, pady = 20)
                Goods_img.place(x=32,y=32)
                self.Goods_Label.update()
                List_Goods.update()
                self.second_frame.update()
                List_Goods.xview_moveto(1)
                
                Names_label = tk.Label(self.Goods_Label,text= dict_name[str(int(stock.return_id(j))//100)],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A")
                # Names_label.pack()
                Names_label.place(x=10,y=340)
                self.Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Goods_info = tk.Label(self.Goods_Label,image= self.Goods_infoimg,borderwidth=0)
                # Goods_info.pack(pady=20)
                Goods_info.place(x=-2,y=418)
                self.Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Price_Label = tk.Label(self.Goods_Label,text="Price :      " + dict_price[str(int(stock.return_id(j))//100)],font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Amounts_label.pack(padx = 120,anchor="w")
                Price_Label.place(x=32,y=440)
                self.Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Exp_label = tk.Label(self.Goods_Label,text="Exp : " +  stock.return_exp(j) ,font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Exp_label.pack()
                Exp_label.place(x=32,y=530)
                self.Goods_Label.update()
                # k = k+500
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update() 
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()

                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        List_Goods.xview_moveto(1)
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        List_Goods.update()
        self.second_frame.update()
        List_Goods.xview_moveto(1)
        List_Goods.update()
        self.second_frame.update()
        Goods_info.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

    




    def __init__(self, parent, controller):

        self.NewName=[]
        self.NewImg =[]
        self.cnt = 0
        
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.bg = tk.Frame(self, bg = "#849D8A",width = "1920",height="1080")
        self.bg.pack(fill = BOTH, expand=1)

        Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="210")
        Header_Bar.place(x=0,y=0)

        List_Goods = tk.Canvas(self.bg,bg="#D6CEA7",highlightthickness = 0,bd =0)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)

        List_Goods.xview_moveto(1)
        List_Goods.update()

        self.my_scrollbar = tk.Scrollbar(self, orient = HORIZONTAL , command = List_Goods.xview,width=20)
        self.my_scrollbar.pack(side=BOTTOM,fill=X)
        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        List_Goods.configure(xscrollcommand=self.my_scrollbar.set)

        self.second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        self.second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((60,365), window = self.second_frame,anchor="nw")
        self.second_frame.update()

        self.selectimg = PhotoImage(file="selection00.png")
        Selct_Label = tk.Label(self.bg, image = self.selectimg,borderwidth=0,bg ="#D6CEA7")
        Selct_Label.place(x=0,y=190)

        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Admin_Management_Page"))
        Back_Btn.place(x=70,y=40)

        self.roundrecimg =  PhotoImage(file="AddStock.png")
        AddStock_Btn = tk.Button(self, image = self.roundrecimg,text = "Add Stock",borderwidth=0,bg="#849D8A",command=lambda: controller.show_frame("Add_Stock_Page"))
        AddStock_Btn.place(x=1500,y=50)

        j = 0

        self.Arrow_Downimg = PhotoImage(file="arrow-down-sign-to-navigate 2.png")

        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 5  ,bg = "#849D8A", text= "Stock", fg = "#FFFFFF",width = 18)
        Header_Label.configure(font = Font_tuple2)
        Header_Label.place(x=960,y=110,anchor="center")

        Types_Frame = tk.Frame(List_Goods,width=450,height=700,bg = "#849D8A")
        Types_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0,command=lambda:[self.sort_type()])
        Types_Btn.place(x = 640,y = 23)

        Exp_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Exp_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Exp_Btn.place(x = 1090,y = 23)
        Exp_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessExp_Btn.pack(padx=19,pady = 2)

        LesstoMoreExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Less than to \n More than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreExp_Btn.pack(padx=19,pady = 12)

        ValidExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Valid Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ValidExp_Btn.pack(padx=19,pady = 2)

        ExpireExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Expired Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ExpireExp_Btn.pack(padx=19,pady = 12)

        Amounts_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Amounts_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Amounts_Btn.place(x = 1725,y = 23)
        Amounts_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessAmount_Btn.pack(padx=19,pady = 2)

        LesstoMoreAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Less than to \n more than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreAmount_Btn.pack(padx=19,pady = 12)

        ZeroAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Show Zero \n Amounts", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ZeroAmount_Btn.pack(padx=19,pady = 2)


        Total_Btn = tk.Button(self.bg,image = self.pixelVirtual,text="Total", width=311,height = 100,font = ("Londrina Solid Black",55),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        Total_Btn.place(x=16,y = 210)

        Prices_Header = tk.Label(self.bg,text="Price",font = ("Londrina Solid Black",55),width=10,fg= "#849D8A",bg="#D6CEA7")
        Prices_Header.place(x=1300,y = 213)
    
        #------------------------------ Data ----------------------------------------------------------
        read_file()
        #print("Stock Page!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.Name = stock.list_name()
        self.Price = stock.list_price()
        self.Img = stock.list_img()
        self.Exp = stock.list_Exp()
        #self.Name = ["Coke","Pepsi","Fanta","Est","Mirinda","Sprite","7up","Lipton"]  
        #self.Img = ["Coke.png","Pepsi.png","Fanta.png","Est.png","Mirinda.png","Sprite.png","7up.png","Lipton.png"]     # รูปสินค้า
        #self.Price = [0,1]
        #self.Exp = ["12/12/2010","12/12/2011"]

        #------------------------------------------------------------------------------------------------


        List_Goods.xview_moveto(1)
        List_Goods.update()
        self.second_frame.update()
        
        self.Goods_labelimg = PhotoImage(file="Rectangle 14 .png")
        self.Goods_infoimg = PhotoImage(file="Rectangle 21.png")
        
        # Goods_Label = tk.Label(self.second_frame,image = self.Goods_labelimg,width=535,height=636)
        # Goods_info = tk.Label(Goods_Label,image= self.Goods_infoimg,borderwidth=0)
        
        self.Goodsimg = []
        for i in range(len(self.Img)):
             self.Goodsimg.append("")

        for i in range(len(self.Img)) :
            self.Goodsimg[i] = PhotoImage(file= self.Img[i])
       
       
        for j in range(0,len(self.Name)):

                ctypes.windll.shcore.SetProcessDpiAwareness(True)

                List_Goods.update()
                self.second_frame.update() 
                List_Goods.update()
                self.second_frame.update()
                List_Goods.update()
                self.my_scrollbar.bind('<Button-1>' ,self.Updates)

                self.Goods_Label = tk.Label(self.second_frame,image = self.Goods_labelimg,width=535,height=636)
                self.Goods_Label.pack(side =LEFT, padx = 50, pady =0)
                # Goods_Label.pack(side = TOP,pady =400)
                self.Goods_Label.update()
                List_Goods.update()
                self.second_frame.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    

                Goods_img = tk.Label(self.Goods_Label,image= self.Goodsimg[j],borderwidth=0,bg="#FFFFFF")
                # Goods_img.pack(padx=20, pady = 20)
                Goods_img.place(x=32,y=32)
                self.Goods_Label.update()
                List_Goods.update()
                self.second_frame.update()
                List_Goods.xview_moveto(1)
                
                Names_label = tk.Label(self.Goods_Label,text= self.Name[j],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A")
                # Names_label.pack()
                Names_label.place(x=10,y=340)
                self.Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Goods_info = tk.Label(self.Goods_Label,image= self.Goods_infoimg,borderwidth=0)
                # Goods_info.pack(pady=20)
                Goods_info.place(x=-2,y=418)
                self.Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Price_Label = tk.Label(self.Goods_Label,text="Price :      " + str(self.Price[j]),font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Amounts_label.pack(padx = 120,anchor="w")
                Price_Label.place(x=32,y=440)
                self.Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Exp_label = tk.Label(self.Goods_Label,text="Exp : " +  self.Exp[j] ,font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Exp_label.pack()
                Exp_label.place(x=32,y=530)
                self.Goods_Label.update()
                # k = k+500
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update() 
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                self.second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()
                self.Goods_Label.update()

                self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        List_Goods.xview_moveto(1)
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        self.Goods_Label.update()
        List_Goods.update()
        self.second_frame.update()
        List_Goods.xview_moveto(1)
        List_Goods.update()
        self.second_frame.update()
        Goods_info.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        self.my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        restartBtn = Button(Header_Bar, text="Destroy", command= lambda : [self.my_scrollbar.pack_forget(),self.bg.pack_forget(),List_Goods.pack_forget()],bg ="#849D8A",fg="White",relief="flat")
        restartBtn.place(x = 10, y=5)
        refreshBtn = Button(Header_Bar, text="Restart", command= lambda : self.restart(),bg ="#849D8A",fg="White",relief="flat")
        refreshBtn.place(x = 10, y=40)

    def sort_type(self) :
        print(stock)
        stock.bubble_sort()
       #stock.print_linkedlist()
        sort_type_id = stock.list_id()
        sort_type_exp = stock.list_Exp()
        print(sort_type_id)
        print(sort_type_exp)
        self.Goodsimg = []
       # for i in range(stock.size()):
             #self.Goodsimg.append("")
       # for i in range(stock.size()) :
            #self.Goodsimg[i] = PhotoImage(file= dict_img[str(int(stock.return_id(i))//100)])

        #for i in range(len(sorted_type)):
            

    #def sort_exp(self) :


    def hide_button(self,event,witget):
        event.widget.place_forget()
        

    def Updates(self,event):

            event.widget.update_idletasks()
            event.widget.update()

class Add_Stock_Page(tk.Frame): #หน้า Add Stock

    def Updates(self,event):
        
            event.widget.update_idletasks()
            event.widget.update()

    # def restart(self):
    #     self.refresh(self.parent,self.controller)
    #     print("restart")
    #     self.controller.show_frame("Add_Stock_Page")

    # def refresh(self,parent, controller):
       
    def __init__(self, parent, controller):
        
        self.Updates
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="216")
        Header_Bar.pack(fill = X)
        
        bg = tk.Frame(self, bg = "#D6CEA7",width = "1920",height="1080")
    
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 5  ,bg = "#849D8A", text= "Add Stock", fg = "#FFFFFF",width = 18,font = ("Londrina Solid",90))
        Header_Label.place(x=960,y=100,anchor="center")




        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Stock_Page"))
        Back_Btn.place(x=70,y=40)

        List_Goods = tk.Canvas(bg,bg="#D6CEA7",highlightthickness = 0,bd =0,width=1870,height=1080)
        my_scrollbar = tk.Scrollbar(bg, orient = VERTICAL , command = List_Goods.yview,width=20)
        self.second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        self.second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((38,0), window = self.second_frame,anchor="nw")
        List_Goods.configure(yscrollcommand=my_scrollbar.set)
        # second_frame.update()
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        self.Goods_labelimg = PhotoImage(file="Rectangle 33.png")
        self.Goodsimg = PhotoImage(file="Rectangle 26.png")
        self.Addimg = PhotoImage(file="Rectangle 29.png")

        # List_Goods.update_idletasks()
       

        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
         #------------------------------ Data ----------------------------------------------------------
        
        # self.ID = [11101,11101,11101,11101,11101,11101,11101,11101]
        # self.Exp = ["12/12/2010","12/12/2011","12/12/2012","12/12/2013","12/12/2014","12/12/2015","12/12/2016","12/12/2017"]
        # self.Price = [100,100,100,100,100,100,100,100]
        # self.Amounts = []
    
        # for i in range(len(self.ID)):
        #     self.Amounts.append("")
        #     List_Goods.yview_moveto(1)
            

        # for i in range(len(self.ID)):
        self.Amounts = IntVar()
        self.Amounts.set(0)
     
            
        
        #-----------------------------------------------------------------------------------------------
      
        List_Goods.yview_moveto(1)
        # for i in range(8): 

        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    

        Goods_Label = tk.Label(self.second_frame,image = self.Goods_labelimg,borderwidth=0,relief="flat")
        Goods_Label.pack(pady =120)

        Add_Btn = tk.Button(self.second_frame,text = "Add Items",font = ("Londrina Solid Black",50),width=15,fg="#FFFFFF",bg="#849D8A",command=lambda: controller.show_frame("Stock_Page") & self.confirm() ) #,command=lambda:self.confirm()
        Add_Btn.pack(pady =80)
           

        Goods_img = tk.Label(Goods_Label,image= self.Goodsimg,borderwidth=0,bg="#FFFFFF",relief="flat")
        # Goods_img.place(x=65,y =25)
           

        ID_label = tk.Label(Goods_Label,text= "ID",font = ("Londrina Solid Black",65),bg="#FFFFFF",fg="#849D8A",relief="flat")
        ID_label.place(x=130,y=85)

        self.IDvar = tk.IntVar()
        self.IDvar.set("")
        ID_Entry = Entry(Goods_Label,bd=5,textvariable=self.IDvar)
        ID_Entry.place(x=230,y=85,width=260)
        ID_Entry.configure(font = ("Londrina Solid Black",65),fg ="#849D8A")


        # self.Pricevar = tk.IntVar()
        # self.Pricevar.set("")
        # Price_Entry = Entry(Goods_Label,bd=5,textvariable=self.Pricevar)
        # Price_Entry.place(x=630,y=85,width=180)
        # Price_label = tk.Label(Goods_Label,text= "Price",font = ("Londrina Solid Black",65),bg="#FFFFFF",fg="#849D8A",relief="flat")
        # Price_label.place(x=430,y=85)
        # Price_Entry.configure(font = ("Londrina Solid Black",65),fg ="#849D8A")


        Exp_label = tk.Label(Goods_Label,text= "Exp.",font = ("Londrina Solid Black",65),bg="#FFFFFF",fg="#849D8A",relief="flat")
        Exp_label.place(x=600,y=85)

        self.Expvar = tk.StringVar()
        self.Expvar.set("")
        Expvar_Entry = Entry(Goods_Label,bd=5,textvariable=self.Expvar)
        Expvar_Entry.place(x=760,y=85,width=420)
        Expvar_Entry.configure(font = ("Londrina Solid Black",65),fg ="#849D8A")


          

        Add_Label = tk.Label(Goods_Label,image = self.Addimg,bg="#FFFFFF",relief="flat")
        Add_Label.place(x=1290,y=55)
           


            
        Amounts_Label = tk.Label(Add_Label ,font= ("Londrina Solid Black",50),bg = "#FFFFFF",fg = "#849D8A",width = 10,relief="flat")
        Amounts_Label.config(textvariable = self.Amounts)
        Amounts_Label.place(x=223,y=70,anchor="c")
           
        List_Goods.yview_moveto(1)
          

        Add_Btn = tk.Button(Add_Label,text = "+",image= self.pixelVirtual,bg="#FFFFFF",fg="#849D8A",width =35,height=40,font= ("Londrina Solid Black",50),compound="c",borderwidth=0,command = lambda : self.Add(),relief="flat")
        Add_Btn.place(x=60,y=50)
        List_Goods.yview_moveto(1)
           
        

        Del_Btn = tk.Button(Add_Label,text = "-",image= self.pixelVirtual,bg="#FFFFFF",fg="#849D8A",width =35,height=40,font= ("Londrina Solid Black",50),compound="c",borderwidth=0,command = lambda :  self.Del(),relief="flat")
        Del_Btn.place(x=345,y=50)   
        List_Goods.yview_moveto(1)

        bg.pack(fill = BOTH, expand=1)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)
        # my_scrollbar.pack(side=RIGHT,fill=Y)



    def Add(self):    # แก้ของ shelf อีกทีนะ กูก๋อปจาด stock
        x = self.Amounts.get()+1
        self.Amounts.set(x)

    def Del (self):
        if self.Amounts.get() > 0:
            x = self.Amounts.get()-1
            self.Amounts.set(x)

    def confirm(self) :
        id_stock = self.IDvar.get()
        exp = self.Expvar.get()
        stock.append(int(id_stock),str(exp))
        f = open("Stock_data.txt","a+")
        f.write(str(id_stock) + ',' + str(exp) + '\n')
        f.close()
        

f = open("Shelf_data.txt","r");
shelf = linkedlist()
while(True) :
    s = f.readline()
    if s == '' :
        break        
    s = s.split(',')
    exp = str(s[1])
    #print(exp)
    shelf.append_and_sort_by_exp(int(s[0]) *100,exp[0:-1])
f.close()

class Shelf_Page(tk.Frame): # หน้า Shelf
    def restart(self) :
        self.refresh(self.parent,self.controller)
        print("restart")
        self.controller.show_frame("Shelf_Page")

    def refresh(self,parent, controller):
        bg = tk.Frame(self, bg = "#849D8A",width = "1920",height="1080")
        bg.pack(fill = BOTH, expand=1)

        Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="210")
        Header_Bar.place(x=0,y=0)

        List_Goods = tk.Canvas(bg,bg="#D6CEA7",highlightthickness = 0,bd =0)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)

        List_Goods.xview_moveto(1)
        List_Goods.update()

        my_scrollbar = tk.Scrollbar(self, orient = HORIZONTAL , command = List_Goods.xview,width=20)
        my_scrollbar.pack(side=BOTTOM,fill=X)
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        restartBtn = Button(Header_Bar, text="Destroy", command= lambda : [my_scrollbar.pack_forget(),bg.pack_forget(),List_Goods.pack_forget()],bg ="#849D8A",fg="White",relief="flat")
        restartBtn.place(x = 10, y=5)
        refreshBtn = Button(Header_Bar, text="Restart", command= lambda : self.restart(),bg ="#849D8A",fg="White",relief="flat")
        refreshBtn.place(x = 10, y=40)

        List_Goods.configure(xscrollcommand=my_scrollbar.set)

        second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((60,365), window = second_frame,anchor="nw")
        second_frame.update()

        self.selectimg = PhotoImage(file="selection00.png")
        Selct_Label = tk.Label(bg, image = self.selectimg,borderwidth=0,bg ="#D6CEA7")
        Selct_Label.place(x=0,y=190)

        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Admin_Management_Page"))
        Back_Btn.place(x=70,y=40)

        self.roundrecimg =  PhotoImage(file="Add Shelf.png")
        AddShelf_Btn = tk.Button(self, image = self.roundrecimg,text = "Add Shelf",borderwidth=0,bg="#849D8A",command=lambda: controller.show_frame("Add_Shelf_Page"))
        AddShelf_Btn.place(x=1500,y=50)

        j = 0

        self.Arrow_Downimg = PhotoImage(file="arrow-down-sign-to-navigate 2.png")

        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 5  ,bg = "#849D8A", text= "Shelf", fg = "#FFFFFF",width = 18)
        Header_Label.configure(font = Font_tuple2)
        Header_Label.place(x=960,y=110,anchor="center")

        Types_Frame = tk.Frame(List_Goods,width=450,height=700,bg = "#849D8A")
        Types_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Types_Btn.place(x = 640,y = 23)

        Exp_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Exp_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Exp_Btn.place(x = 1090,y = 23)
        Exp_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessExp_Btn.pack(padx=19,pady = 2)

        LesstoMoreExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Less than to \n More than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreExp_Btn.pack(padx=19,pady = 12)

        ValidExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Valid Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ValidExp_Btn.pack(padx=19,pady = 2)

        ExpireExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Expired Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ExpireExp_Btn.pack(padx=19,pady = 12)

        Amounts_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Amounts_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Amounts_Btn.place(x = 1725,y = 23)
        Amounts_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessAmount_Btn.pack(padx=19,pady = 2)

        LesstoMoreAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Less than to \n more than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreAmount_Btn.pack(padx=19,pady = 12)

        ZeroAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Show Zero \n Amounts", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ZeroAmount_Btn.pack(padx=19,pady = 2)


        Total_Btn = tk.Button(bg,image = self.pixelVirtual,text="Total", width=311,height = 100,font = ("Londrina Solid Black",55),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        Total_Btn.place(x=16,y = 210)

        Prices_Header = tk.Label(bg,text="Price",font = ("Londrina Solid Black",55),width=10,fg= "#849D8A",bg="#D6CEA7")
        Prices_Header.place(x=1300,y = 213)

        

       


    


        #------------------------------ Data ----------------------------------------------------------


        self.Name = shelf.list_name()
        self.Img = shelf.list_img()     # รูปสินค้า
        self.Amounts = shelf.list_price()
        self.Exp = shelf.list_Exp()
    

        #------------------------------------------------------------------------------------------------


        List_Goods.xview_moveto(1)
        List_Goods.update()
        second_frame.update()
        
        self.Goods_labelimg = PhotoImage(file="Rectangle 14 .png")
        self.Goods_infoimg = PhotoImage(file="Rectangle 21.png")
        
        Goods_Label = tk.Label(second_frame,image = self.Goods_labelimg,width=535,height=636)
        Goods_info = tk.Label(Goods_Label,image= self.Goods_infoimg,borderwidth=0)
        
        self.Goodsimg = []
        for i in range(len(self.Img)):
             self.Goodsimg.append("")

        for i in range(len(self.Img)) :
            self.Goodsimg[i] = PhotoImage(file= self.Img[i])
       
       
        for j in range(0,len(self.Name)):

                ctypes.windll.shcore.SetProcessDpiAwareness(True)

                List_Goods.update()
                second_frame.update() 
                List_Goods.update()
                second_frame.update()
                List_Goods.update()
                my_scrollbar.bind('<Button-1>' ,self.Updates)

                Goods_Label = tk.Label(second_frame,image = self.Goods_labelimg,width=535,height=636)
                Goods_Label.pack(side =LEFT, padx = 50, pady =0)
                # Goods_Label.pack(side = TOP,pady =400)
                Goods_Label.update()
                List_Goods.update()
                second_frame.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    

                Goods_img = tk.Label(Goods_Label,image= self.Goodsimg[j],borderwidth=0,bg="#FFFFFF")
                # Goods_img.pack(padx=20, pady = 20)
                Goods_img.place(x=32,y=32)
                Goods_Label.update()
                List_Goods.update()
                second_frame.update()
                List_Goods.xview_moveto(1)
                
                Names_label = tk.Label(Goods_Label,text= self.Name[j],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",width=17)
                # Names_label.pack()
                Names_label.place(x=100,y=368,anchor="c")
                Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Goods_info = tk.Label(Goods_Label,image= self.Goods_infoimg,borderwidth=0)
                # Goods_info.pack(pady=20)
                Goods_info.place(x=-2,y=418)
                Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Price_Label = tk.Label(Goods_Label,text="Price :        " + str(self.Amounts[j]),font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Amounts_label.pack(padx = 120,anchor="w")
                Price_Label.place(x=32,y=440)
                Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Exp_label = tk.Label(Goods_Label,text="Exp : " +  self.Exp[j] ,font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Exp_label.pack()
                Exp_label.place(x=32,y=530)
                Goods_Label.update()
                # k = k+500
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update() 
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()

                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        List_Goods.xview_moveto(1)
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        List_Goods.update()
        second_frame.update()
        List_Goods.xview_moveto(1)
        List_Goods.update()
        second_frame.update()
        Goods_info.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)


    def __init__(self, parent, controller):

        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        bg = tk.Frame(self, bg = "#849D8A",width = "1920",height="1080")
        bg.pack(fill = BOTH, expand=1)

        Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="210")
        Header_Bar.place(x=0,y=0)

        List_Goods = tk.Canvas(bg,bg="#D6CEA7",highlightthickness = 0,bd =0)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)

        List_Goods.xview_moveto(1)
        List_Goods.update()

        my_scrollbar = tk.Scrollbar(self, orient = HORIZONTAL , command = List_Goods.xview,width=20)
        my_scrollbar.pack(side=BOTTOM,fill=X)
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        restartBtn = Button(Header_Bar, text="Destroy", command= lambda : [my_scrollbar.pack_forget(),bg.pack_forget(),List_Goods.pack_forget()],bg ="#849D8A",fg="White",relief="flat")
        restartBtn.place(x = 10, y=5)
        refreshBtn = Button(Header_Bar, text="Restart", command= lambda : self.restart(),bg ="#849D8A",fg="White",relief="flat")
        refreshBtn.place(x = 10, y=40)

        List_Goods.configure(xscrollcommand=my_scrollbar.set)

        second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((60,365), window = second_frame,anchor="nw")
        second_frame.update()

        self.selectimg = PhotoImage(file="selection00.png")
        Selct_Label = tk.Label(bg, image = self.selectimg,borderwidth=0,bg ="#D6CEA7")
        Selct_Label.place(x=0,y=190)

        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Admin_Management_Page"))
        Back_Btn.place(x=70,y=40)

        self.roundrecimg =  PhotoImage(file="Add Shelf.png")
        AddShelf_Btn = tk.Button(self, image = self.roundrecimg,text = "Add Shelf",borderwidth=0,bg="#849D8A",command=lambda: controller.show_frame("Add_Shelf_Page"))
        AddShelf_Btn.place(x=1500,y=50)

        j = 0

        self.Arrow_Downimg = PhotoImage(file="arrow-down-sign-to-navigate 2.png")

        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 5  ,bg = "#849D8A", text= "Shelf", fg = "#FFFFFF",width = 18)
        Header_Label.configure(font = Font_tuple2)
        Header_Label.place(x=960,y=110,anchor="center")

        Types_Frame = tk.Frame(List_Goods,width=450,height=700,bg = "#849D8A")
        Types_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Types_Btn.place(x = 640,y = 23)

        Exp_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Exp_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Exp_Btn.place(x = 1090,y = 23)
        Exp_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessExp_Btn.pack(padx=19,pady = 2)

        LesstoMoreExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Less than to \n More than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreExp_Btn.pack(padx=19,pady = 12)

        ValidExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Valid Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ValidExp_Btn.pack(padx=19,pady = 2)

        ExpireExp_Btn = tk.Button(Exp_Frame,image = self.pixelVirtual,text="Show Expired Exp", width=415,height = 100,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ExpireExp_Btn.pack(padx=19,pady = 12)

        Amounts_Frame = tk.Frame(List_Goods,width=455,height=700,bg = "#849D8A")
        Amounts_Btn = tk.Button(Selct_Label,image = self.Arrow_Downimg,bg = "#D6CEA7",borderwidth=0)
        Amounts_Btn.place(x = 1725,y = 23)
        Amounts_Frame.bind('<Leave>',lambda event, widget=Exp_Frame: self.hide_button(event,  Exp_Frame))

        MoretoLessAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="More than to \n less than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        MoretoLessAmount_Btn.pack(padx=19,pady = 2)

        LesstoMoreAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Less than to \n more than", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        LesstoMoreAmount_Btn.pack(padx=19,pady = 12)

        ZeroAmount_Btn = tk.Button(Amounts_Frame,image = self.pixelVirtual,text="Show Zero \n Amounts", width=415,height = 200,font = ("Londrina Solid Black",44),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        ZeroAmount_Btn.pack(padx=19,pady = 2)


        Total_Btn = tk.Button(bg,image = self.pixelVirtual,text="Total", width=311,height = 100,font = ("Londrina Solid Black",55),compound="c",bg="#D6CEA7",fg="#849D8A",borderwidth=0)
        Total_Btn.place(x=16,y = 210)

        Prices_Header = tk.Label(bg,text="Price",font = ("Londrina Solid Black",55),width=10,fg= "#849D8A",bg="#D6CEA7")
        Prices_Header.place(x=1300,y = 213)

        

       


    


        #------------------------------ Data ----------------------------------------------------------


        self.Name = shelf.list_name()
        self.Img = shelf.list_img()     # รูปสินค้า
        self.Amounts = shelf.list_price()
        self.Exp = shelf.list_Exp()
    

        #------------------------------------------------------------------------------------------------


        List_Goods.xview_moveto(1)
        List_Goods.update()
        second_frame.update()
        
        self.Goods_labelimg = PhotoImage(file="Rectangle 14 .png")
        self.Goods_infoimg = PhotoImage(file="Rectangle 21.png")
        
        Goods_Label = tk.Label(second_frame,image = self.Goods_labelimg,width=535,height=636)
        Goods_info = tk.Label(Goods_Label,image= self.Goods_infoimg,borderwidth=0)
        
        self.Goodsimg = []
        for i in range(len(self.Img)):
             self.Goodsimg.append("")

        for i in range(len(self.Img)) :
            self.Goodsimg[i] = PhotoImage(file= self.Img[i])
       
       
        for j in range(0,len(self.Name)):

                ctypes.windll.shcore.SetProcessDpiAwareness(True)

                List_Goods.update()
                second_frame.update() 
                List_Goods.update()
                second_frame.update()
                List_Goods.update()
                my_scrollbar.bind('<Button-1>' ,self.Updates)

                Goods_Label = tk.Label(second_frame,image = self.Goods_labelimg,width=535,height=636)
                Goods_Label.pack(side =LEFT, padx = 50, pady =0)
                # Goods_Label.pack(side = TOP,pady =400)
                Goods_Label.update()
                List_Goods.update()
                second_frame.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    

                Goods_img = tk.Label(Goods_Label,image= self.Goodsimg[j],borderwidth=0,bg="#FFFFFF")
                # Goods_img.pack(padx=20, pady = 20)
                Goods_img.place(x=32,y=32)
                Goods_Label.update()
                List_Goods.update()
                second_frame.update()
                List_Goods.xview_moveto(1)
                
                Names_label = tk.Label(Goods_Label,text= self.Name[j],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",width=17)
                # Names_label.pack()
                Names_label.place(x=100,y=368,anchor="c")
                Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Goods_info = tk.Label(Goods_Label,image= self.Goods_infoimg,borderwidth=0)
                # Goods_info.pack(pady=20)
                Goods_info.place(x=-2,y=418)
                Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Price_Label = tk.Label(Goods_Label,text="Price :        " + str(self.Amounts[j]),font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Amounts_label.pack(padx = 120,anchor="w")
                Price_Label.place(x=32,y=440)
                Goods_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
    
                Exp_label = tk.Label(Goods_Label,text="Exp : " +  self.Exp[j] ,font = ("Londrina Solid Black",50),bg="#849D8A",fg="#FFFFFF")
                # Exp_label.pack()
                Exp_label.place(x=32,y=530)
                Goods_Label.update()
                # k = k+500
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update() 
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                List_Goods.xview_moveto(1)
                List_Goods.update()
                second_frame.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Goods_info.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Exp_label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Price_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()
                Goods_Label.update()

                my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)

        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        List_Goods.xview_moveto(1)
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        Goods_Label.update()
        List_Goods.update()
        second_frame.update()
        List_Goods.xview_moveto(1)
        List_Goods.update()
        second_frame.update()
        Goods_info.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Exp_label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        Price_Label.update()
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)


    
    def hide_button(self,event,witget):
        event.widget.place_forget()
        

    def Updates(self,event):

            event.widget.update_idletasks()
            event.widget.update()


class Add_Shelf_Page(tk.Frame): #หน้า Add Shelf

    def restart(self) :
        self.refresh(self.parent,self.controller)
        print("restart")
        self.controller.show_frame("Add_Shelf_Page")
    
    def refresh(self,parent, controller):

        # Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="216")
        # Header_Bar.pack(fill = X)
        
        bg = tk.Frame(self, bg = "#D6CEA7",width = "1920",height="1080")
    
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 0  ,bg = "#849D8A", text= "Add Shelf", fg = "#FFFFFF",width = 18,font = ("Londrina Solid",85))
        Header_Label.place(x=960,y=70,anchor="center")

        ID_Label = tk.Label(self ,bg = "#849D8A", text= "ID", fg = "#FFFFFF",font = ("Londrina Solid",45))
        ID_Label.place(x=750,y=165,anchor="center")

        Price_Label = tk.Label(self ,bg = "#849D8A", text= "Price", fg = "#FFFFFF",font = ("Londrina Solid",45))
        Price_Label.place(x=1100,y=165,anchor="center")

        Exp_Label = tk.Label(self ,bg = "#849D8A", text= "Exp.", fg = "#FFFFFF",font = ("Londrina Solid",45))
        Exp_Label.place(x=1540,y=165,anchor="center")

        # Amt_Label = tk.Label(self ,bg = "#849D8A", text= "Amount", fg = "#FFFFFF",font = ("Londrina Solid",45))
        # Amt_Label.place(x=1600,y=165,anchor="center")




        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Shelf_Page"))
        Back_Btn.place(x=70,y=40)

        List_Goods = tk.Canvas(bg,bg="#D6CEA7",highlightthickness = 0,bd =0,width=1870,height=1080)
        my_scrollbar = tk.Scrollbar(bg, orient = VERTICAL , command = List_Goods.yview,width=20)

        restartBtn = Button(self.Header_Bar, text="Destroy", command= lambda : [my_scrollbar.pack_forget(),bg.pack_forget(),List_Goods.pack_forget()],bg ="#849D8A",fg="White",relief="flat")
        restartBtn.place(x = 10, y=5)
        refreshBtn = Button(self.Header_Bar, text="Restart", command= lambda : self.restart(),bg ="#849D8A",fg="White",relief="flat")
        refreshBtn.place(x = 10, y=40)

        second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((24,0), window = second_frame,anchor="nw")
        List_Goods.configure(yscrollcommand=my_scrollbar.set)
        # second_frame.update()
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        self.Goods_labelimg = PhotoImage(file="Rectangle 33.png")
        self.Goodsimg = PhotoImage(file="Rectangle 26.png")
        self.Addimg = PhotoImage(file="Rectangle 29.png")

        # List_Goods.update_idletasks()
       

        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
         #------------------------------ Data ----------------------------------------------------------
        f = open("Stock_data.txt" , 'r')
        self.stock_to_shelf = linkedlist()
        while True :
            s = f.readline()
            if s == '' :
                break
            s = s.split(',')
            exp = s[1]
            #print(self.stock_to_shelf)
            self.stock_to_shelf.append_and_sort_by_exp(s[0],exp[0:-1])
        self.ID = self.stock_to_shelf.list_id()
        self.Exp = self.stock_to_shelf.list_Exp()
        self.Price = self.stock_to_shelf.list_price()
        self.Img = self.stock_to_shelf.list_img()
        print(self.Img)
        self.Amounts = []
    
        for i in range(len(self.ID)):
            self.Amounts.append("")
            List_Goods.yview_moveto(1)
            

        for i in range(len(self.ID)):
            self.Amounts[i] = IntVar()
            self.Amounts[i].set(0)
            List_Goods.yview_moveto(1)            
        self.Goodsimg = []
        for i in range(len(self.Img)):
            self.Goodsimg.append("")

        for i in range(len(self.Img)) :
            self.Goodsimg[i] = PhotoImage(file= self.Img[i])
        #-----------------------------------------------------------------------------------------------
      
        List_Goods.yview_moveto(1)
        for i in range(self.stock_to_shelf.size()): 

            ctypes.windll.shcore.SetProcessDpiAwareness(True)
            List_Goods.yview_moveto(1)

            Goods_Label = tk.Label(second_frame,image = self.Goods_labelimg,borderwidth=0,relief="flat")
            Goods_Label.pack(pady =5)
           

            Goods_img = tk.Label(Goods_Label,image= self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=75,y =25)
           
           

            ID_label = tk.Label(Goods_Label,text= self.ID[i],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",relief="flat")
            ID_label.place(x=650,y=95)

            Price_label = tk.Label(Goods_Label,text= self.Price[i],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",relief="flat")
            Price_label.place(x=1040,y=95)


            Exp_label = tk.Label(Goods_Label,text= self.Exp[i],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",relief="flat")
            Exp_label.place(x=1520,y=136,anchor="c")
          

            # Add_Label = tk.Label(Goods_Label,image = self.Addimg,bg="#FFFFFF",relief="flat")
            # Add_Label.place(x=1350,y=55)
           
            List_Goods.yview_moveto(1)

            
            # Amounts_Label = tk.Label(Add_Label ,font= ("Londrina Solid Black",60),bg = "#FFFFFF",fg = "#849D8A",width = 10,relief="flat")
            # Amounts_Label.config(textvariable = str(self.Amounts[i]))
            # Amounts_Label.place(x=223,y=70,anchor="c")
           
            List_Goods.yview_moveto(1)
          

            # Add_Btn = tk.Button(Add_Label,text = "Add item",image= self.pixelVirtual,bg="#FFFFFF",fg="#849D8A",height= 70,font= ("Londrina Solid Black",60),compound="c",borderwidth=0,relief="flat")
            # Add_Btn.place(x=60,y=35)
            List_Goods.yview_moveto(1)
            Goods_Label.bind('<Button-1>',lambda event, widget=Goods_Label, i=i: self.hide_button(event,  Goods_Label, i))
    
            # Del_Btn = tk.Button(Add_Label,text = "-",image= self.pixelVirtual,bg="#FFFFFF",fg="#849D8A",width =35,height=40,font= ("Londrina Solid Black",60),compound="c",borderwidth=0,command = lambda i=i :  self.Del(i),relief="flat")
            # Del_Btn.place(x=345,y=50)   
            # List_Goods.yview_moveto(1)

        bg.pack(fill = BOTH, expand=1)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)
        my_scrollbar.pack(side=RIGHT,fill=Y)

    

    def Updates(self,event):
        
            event.widget.update_idletasks()
            event.widget.update()
 

    def __init__(self, parent, controller):
        
        self.Updates
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Header_Bar = tk.Frame(self, bg = "#849D8A",width = "1920",height="216")
        self.Header_Bar.pack(fill = X)
        
        bg = tk.Frame(self, bg = "#D6CEA7",width = "1920",height="1080")
    
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        Header_Label = tk.Label(self,bd = 0  ,bg = "#849D8A", text= "Add Shelf", fg = "#FFFFFF",width = 18,font = ("Londrina Solid",85))
        Header_Label.place(x=960,y=70,anchor="center")

        ID_Label = tk.Label(self ,bg = "#849D8A", text= "ID", fg = "#FFFFFF",font = ("Londrina Solid",45))
        ID_Label.place(x=750,y=165,anchor="center")

        Price_Label = tk.Label(self ,bg = "#849D8A", text= "Price", fg = "#FFFFFF",font = ("Londrina Solid",45))
        Price_Label.place(x=1100,y=165,anchor="center")

        Exp_Label = tk.Label(self ,bg = "#849D8A", text= "Exp.", fg = "#FFFFFF",font = ("Londrina Solid",45))
        Exp_Label.place(x=1540,y=165,anchor="center")

        # Amt_Label = tk.Label(self ,bg = "#849D8A", text= "Amount", fg = "#FFFFFF",font = ("Londrina Solid",45))
        # Amt_Label.place(x=1600,y=165,anchor="center")




        self.backimg = PhotoImage(file="right-arrow 2.png")
        Back_Btn = tk.Button(self, image = self.backimg,bg="#849D8A",borderwidth=0,command=lambda: controller.show_frame("Shelf_Page"))
        Back_Btn.place(x=70,y=40)

        List_Goods = tk.Canvas(bg,bg="#D6CEA7",highlightthickness = 0,bd =0,width=1870,height=1080)
        my_scrollbar = tk.Scrollbar(bg, orient = VERTICAL , command = List_Goods.yview,width=20)

        restartBtn = Button(self.Header_Bar, text="Destroy", command= lambda : [my_scrollbar.pack_forget(),bg.pack_forget(),List_Goods.pack_forget()],bg ="#849D8A",fg="White",relief="flat")
        restartBtn.place(x = 10, y=5)
        refreshBtn = Button(self.Header_Bar, text="Restart", command= lambda : self.restart(),bg ="#849D8A",fg="White",relief="flat")
        refreshBtn.place(x = 10, y=40)

        second_frame = tk.Frame(List_Goods,bg="#D6CEA7")
        second_frame.bind('<Configure>', lambda e: List_Goods.configure(scrollregion = List_Goods.bbox("all")))
        List_Goods.create_window((24,0), window = second_frame,anchor="nw")
        List_Goods.configure(yscrollcommand=my_scrollbar.set)
        # second_frame.update()
        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
        self.Goods_labelimg = PhotoImage(file="Rectangle 33.png")
        #self.Goodsimg = PhotoImage(file="Rectangle 26.png")
        self.Addimg = PhotoImage(file="Rectangle 29.png")

        # List_Goods.update_idletasks()
       

        my_scrollbar.bind('<ButtonRelease-1>' ,self.Updates)
         #------------------------------ Data ----------------------------------------------------------
        f = open("Stock_data.txt" , 'r')
        self.stock_to_shelf = linkedlist()
        while True :
            s = f.readline()
            if s == '' :
                break
            s = s.split(',')
            exp = s[1]
            #print(self.stock_to_shelf)
            self.stock_to_shelf.append_and_sort_by_exp(s[0],exp[0:-1])
        self.ID = self.stock_to_shelf.list_id()
        self.Exp = self.stock_to_shelf.list_Exp()
        self.Price = self.stock_to_shelf.list_price()
        self.Img = self.stock_to_shelf.list_img()
        self.Amounts = []
    
        for i in range(len(self.ID)):
            self.Amounts.append("")
            List_Goods.yview_moveto(1)
            

        for i in range(len(self.ID)):
            self.Amounts[i] = IntVar()
            self.Amounts[i].set(0)
            List_Goods.yview_moveto(1)            
        self.Goodsimg = []
        for i in range(len(self.Img)):
            self.Goodsimg.append("")

        for i in range(len(self.Img)) :
            self.Goodsimg[i] = PhotoImage(file= self.Img[i])
        #-----------------------------------------------------------------------------------------------
      
        List_Goods.yview_moveto(1)
        for i in range(self.stock_to_shelf.size()): 

            ctypes.windll.shcore.SetProcessDpiAwareness(True)
            List_Goods.yview_moveto(1)

            Goods_Label = tk.Label(second_frame,image = self.Goods_labelimg,borderwidth=0,relief="flat")
            Goods_Label.pack(pady =5)
           
            Goods_img = tk.Label(Goods_Label,image=self.Goodsimg[i],borderwidth=0,bg="#FFFFFF",relief="flat")
            Goods_img.place(x=75,y =25)
           
           

            ID_label = tk.Label(Goods_Label,text= self.ID[i],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",relief="flat")
            ID_label.place(x=650,y=95)

            Price_label = tk.Label(Goods_Label,text= self.Price[i],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",relief="flat")
            Price_label.place(x=1040,y=95)


            Exp_label = tk.Label(Goods_Label,text= self.Exp[i],font = ("Londrina Solid Black",50),bg="#FFFFFF",fg="#849D8A",relief="flat")
            Exp_label.place(x=1520,y=136,anchor="c")
          

            # Add_Label = tk.Label(Goods_Label,image = self.Addimg,bg="#FFFFFF",relief="flat")
            # Add_Label.place(x=1350,y=55)
           
            List_Goods.yview_moveto(1)

            
            # Amounts_Label = tk.Label(Add_Label ,font= ("Londrina Solid Black",60),bg = "#FFFFFF",fg = "#849D8A",width = 10,relief="flat")
            # Amounts_Label.config(textvariable = str(self.Amounts[i]))
            # Amounts_Label.place(x=223,y=70,anchor="c")
           
            List_Goods.yview_moveto(1)
          

            # Add_Btn = tk.Button(Add_Label,text = "Add item",image= self.pixelVirtual,bg="#FFFFFF",fg="#849D8A",height= 70,font= ("Londrina Solid Black",60),compound="c",borderwidth=0,relief="flat")
            # Add_Btn.place(x=60,y=35)
            List_Goods.yview_moveto(1)
            Goods_Label.bind('<Button-1>',lambda event, widget=Goods_Label, i=i: self.hide_button(event,  Goods_Label, i))
    
            # Del_Btn = tk.Button(Add_Label,text = "-",image= self.pixelVirtual,bg="#FFFFFF",fg="#849D8A",width =35,height=40,font= ("Londrina Solid Black",60),compound="c",borderwidth=0,command = lambda i=i :  self.Del(i),relief="flat")
            # Del_Btn.place(x=345,y=50)   
            # List_Goods.yview_moveto(1)

        bg.pack(fill = BOTH, expand=1)
        List_Goods.pack(side=LEFT, fill=BOTH, expand = 1)
        my_scrollbar.pack(side=RIGHT,fill=Y)

    def hide_button(self,event,witget,i):
        event.widget.pack_forget()
        #print(self.ID[i])
        self.stock_to_shelf.search_and_delete(self.ID[i])
        #print(self.stock_to_shelf)
        self.stock_to_shelf.write_file_stock()

        shelf.append_and_sort_by_exp(int(self.ID[i]) , self.Exp[i])
        #print(self.shelf)
        shelf.write_file_shelf()
        

    # def Add(self,i):
    #     x = self.Amounts[i].get()+1
    #     self.Amounts[i].set(x)

    # def Del (self,i):
    #     if self.Amounts[i].get() > 0:
    #         x = self.Amounts[i].get()-1
    #         self.Amounts[i].set(x)



        
def file_size():
    size = os.path.getsize("Stock_data.txt")
    return int(size)
                 
        

if __name__ == "__main__":

    Addmin_UI = SampleApp()
    Addmin_UI.title("Self CheckOut App")
    Addmin_UI.geometry("1920x1080")
    Addmin_UI.mainloop()

