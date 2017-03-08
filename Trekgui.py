#!/usr/bin/python3
from tkinter import *
import tkinter as tk
from functools import partial

#global variables for resources/structures **currently not implimented**
manufacture = 0
research = 0
culture = 0
ascendencyToken = 1
command = 5
man_building = 1
res_buidling = 1
cult_building = 1
ships = 1

class Window(Frame):
    #defines window
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.buttons = {}
        self.resources = {}
        self.init_window()

    # draws window and menu bar
    def init_window(self):

        self.master.title("Trek counter")
        self.pack()

        menu = Menu(self.master)
        self.master.config(menu=menu)

        phase = Menu(menu)
        phase.add_command(label='Production', command=self.productionPhase)
        phase.add_command(label='Build', command=self.buildPhase)
        phase.add_command(label='Command', command=self.commandPhase)
        phase.add_command(label='Start', command=self.startConditions)
        menu.add_cascade(label='Selection', menu=phase)
        
    # increases all common resoures via add_resource function    
    def productionPhase(self):
        self.place(x=10,y=10)
        self.buttons = {}
        self.create_button("Culture")
        self.create_button("Research")
        self.create_button("Manufacture")
        
    # options for structions/ships to build via sub_resource and build_structure
    def buildPhase(self):
        ()
        
    # drains command values based on action    
    def commandPhase(self):
        ()
    
    #**needs working global variables** will reset all values to initial game conditions    
    def startConditions(self):
        ()

    #draws buttons and currently defining temporary variable values *needs changed*
    def create_button(self, name):
        self.resources[name] = 0
        self.buttons[name] = tk.Button(self)
        self.buttons[name]["text"] = name + " = 0"
        self.buttons[name]["command"] = partial(self.add_resource, name)
        self.buttons[name].pack(side="top")

    #incriment resource value
    def add_resource(self, resource):
        self.resources[resource] += 1
        self.buttons[resource]["text"] = resource + " = " + str(self.resources[resource])
   
    #subtract combinations of resources, may need multiple functions, consult rules for combinations 
    def build_structure():
        exit()
        
    #decrement resource value   
    def sub_resource():
        exit()

    #intend to show read out of all values as text on right column of window   
    def show_values():
        ()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
