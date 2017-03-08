#!/usr/bin/python3
from tkinter import *
import tkinter as tk
from functools import partial

global manufacture 
global research 
global culture
global ascendencyToken 
global command

class Window(Frame):
    #draws window
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.buttons = {}
        self.resources = {}
        self.init_window()

    def init_window(self):

        self.master.title("Trek counter")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        phase = Menu(menu)
        phase.add_command(label='Production', command=self.productionPhase)
        phase.add_command(label='Build', command=self.buildPhase)
        phase.add_command(label='Command', command=self.commandPhase)
        phase.add_command(label='Start', command=self.startConditions)
        menu.add_cascade(label='Selection', menu=phase)
        
        
    def productionPhase(self):
        self.place(x=10,y=10)
        self.buttons = {}
        self.create_button("Culture")
        self.create_button("Research")
        self.create_button("Manufacture")
        
              
    def buildPhase(self):
        ()
        
    def commandPhase(self):
        ()
        
    def startConditions(self):
        ()

    def create_button(self, name):
        self.resources[name] = 0
        self.buttons[name] = tk.Button(self)
        self.buttons[name]["text"] = name + " = 0"
        self.buttons[name]["command"] = partial(self.add_resource, name)
        self.buttons[name].pack(side="top")

    def add_resource(self, resource):
        self.resources[resource] += 1
        self.buttons[resource]["text"] = resource + " = " + str(self.resources[resource])
        
    def build_structure():
        exit()
    def sub_resource():
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
