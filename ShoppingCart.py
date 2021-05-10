import tkinter
from tkinter import *
from tkinter import messagebox as MsgBoxVap

import sqlite3
from sqlite3 import Error

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ShoppingCart.json")
firebase_admin.initialize_app(cred,
{
    "databaseURL": "https://shopping-cart-9802b.firebaseio.com/"
})

FdbRefVar = db.reference("/")

SupWdwVar = Tk()

SupWdwVar.title("Shopping Cart")

# SupWdwVar.geometry("800x800")

SupWdwVar.minsize(400, 300)

SupWdwVar.configure(background="white")

HeadLbl= Label(SupWdwVar,
      text="Shopping Cart ",
      font="arial 16 bold",
      fg="black", height=1).grid(row=0,columnspan=5)

Label(SupWdwVar,
      text="",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=1, column=0, sticky=W)
Label(SupWdwVar,
      text="",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=2, column=0, sticky=W)

Label(SupWdwVar,
      text="Items",
      font="Cambria 16 bold",
      fg="black",width=10, height=1).grid(row=3, column=0)


Label(SupWdwVar,
      text="Quantity",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=3, column=1, sticky=E)

Label(SupWdwVar,
      text="Total Price",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=3, column=4, sticky=W)

Label(SupWdwVar,
      text="Price",
      font="Cambria 16 bold",
      fg="black",width=10,
       height=1).grid(row=3, column=3)

#========================ItemData===============

FdbRefVar = db.reference("/")

Itementer=Entry(SupWdwVar,
      font="Cambria 16 bold",
      fg="black")
Itementer.grid(row=4,column=0)

Itemprice = Entry(SupWdwVar,font="Cambria 16 bold",
                      fg="black")
Itemprice.grid(row=4, column=3, )


number=tkinter.IntVar()
total=tkinter.StringVar()
grandtotalprice =tkinter.IntVar()
def adding(event=None):

    number.set(number.get()+1)
    Label(SupWdwVar,
          textvariable= number,
          font="Cambria 16 bold",
          fg="black",
          anchor=E, height=1).grid(row=4, column=1)

    Itemname=Itementer.get()
    Itemcost=Itemprice.get()
    value=int(Itemcost)
    if Itemprice.get() == "":
        MsgBoxVap.showerror("Error", "Please Enter any Price")
        return

    total.set(number.get()*value)
    todata = number.get() * value



    Label(SupWdwVar,
          textvariable=total,
          font="Cambria 16 bold",
          fg="black",
          anchor=E, height=1).grid(row=4, column=4)

    def totalcalci():
        global grandtotalprice
        global Itemcost
        Itemcost = Itemprice.get()
        value = int(Itemcost)
        totalvalue = grandtotalprice.get()

        grandtotalprice.set(grandtotalprice.get()+ todata)
        FdbRefVar.child("Data").push("Entries").set({"Total price": todata, "Price": Itemcost, "Items": Itemname})
        totalbill = grandtotalprice.get()
        FdbRefVar.update({"TotalBill": totalbill})

        Label(SupWdwVar,
                          textvariable=grandtotalprice,
                          font="arial 16 bold",
                         fg="black", height=1).grid(row=7, columnspan=5)

        def fulldata():
            data=FdbRefVar.get()
            MsgBoxVap.showinfo("Success",data)

        Button(SupWdwVar, text="Detailed Bill", bg="white", fg="black",
                   command=fulldata, font="arial 16 bold").grid(row=8, columnspan=5)


    Button(SupWdwVar, text="Click for your Bill", bg="white", fg="black",
           command=totalcalci, font="arial 16 bold").grid(row=6, columnspan=5)

    return


def subing():
    number.set(number.get() - 1)

    Label(SupWdwVar,
          textvariable=number,
          font="Cambria 16 bold",
          fg="black",
          anchor=E, height=1).grid(row=4, column=1)
    Itemcost = Itemprice.get()
    value = int(Itemcost)
    if value == None:
        MsgBoxVap.showerror("Error","Please Enter any Price")
        return
    Itemname = Itementer.get()

    total.set(number.get() * value)
    todata = number.get() * value

    def totalcalci():
        global grandtotalprice
        global Itemcost
        Itemcost = Itemprice.get()
        value = int(Itemcost)
        totalvalue=grandtotalprice.get()
        grandtotalprice.set(grandtotalprice.get()+ todata)
        FdbRefVar.child("Data").push().update({"Total price": todata, "Price": Itemcost, "Items": Itemname})
        totalbill = grandtotalprice.get()
        FdbRefVar.update({"TotalBill": totalbill})

        Label(SupWdwVar,
                          textvariable=grandtotalprice,
                          font="arial 16 bold",
                          fg="black", height=1).grid(row=7, columnspan=5)
        def fulldata():
            data=FdbRefVar.get()
            MsgBoxVap.showinfo("Success",data)

        Button(SupWdwVar, text="Detailed Bill", bg="white", fg="black",
                   command=fulldata, font="arial 16 bold").grid(row=8, columnspan=5)

    Button(SupWdwVar, text="Click for your Bill", bg="white", fg="black",
           command=totalcalci, font="arial 16 bold").grid(row=6, columnspan=5)



    Label(SupWdwVar,
          textvariable=total,
          font="Cambria 16 bold",
          fg="black",
          anchor=E, height=1).grid(row=4, column=4)

Button(SupWdwVar ,text="-", bg="white", fg="black",
       command=subing, font="arial 13 bold").grid(row=4, column=1,sticky=W)
Button(SupWdwVar ,text="+", bg="white", fg="black",
       command=adding, font="arial 13 bold").grid(row=4, column=1,sticky=E)

#=========================ItemData===========================
Label(SupWdwVar,
      text="",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=5, column=0, sticky=W)
Label(SupWdwVar,
      text="",
      font="Cambria 16 bold",
      fg="black",
      anchor=E, height=1).grid(row=5, column=0, sticky=W)







SupWdwVar.mainloop()


