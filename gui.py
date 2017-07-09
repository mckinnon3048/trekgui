import tkinter
from tkinter import *
from tkinter import messagebox
"""
to be removed, file used for understanding and demoing tkinter modules
"""

def get_data(event=NONE):
    print("String :", strVar.get())
    print("Intger :", intVar.get())
    print("Double :", dblVar.get())
    print("Boolean :", boolVar.get())

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)


root = Tk()
Tk.frame
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(TRUE)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

theCheckBut = Checkbutton(root, text ="switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)



root.mainloop()