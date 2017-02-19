#!/usr/bin/python3

import tkinter as tk
from functools import partial

manufacture = 0
research = 0
culture = 0
   
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.minsize(width=250, height=100)
        self.pack(side="top")
        self.buttons = {}
        self.resources = {}
        self.create_button("Manufacture")
        self.create_button("Research")
        self.create_button("Culture")
        self.create_button("Ascendency tokens")

    def add_resource(self, resource):
        self.resources[resource] += 1
        self.buttons[resource]["text"] = resource + " = " + str(self.resources[resource])

    def create_button(self, name):
        self.resources[name] = 0
        self.buttons[name] = tk.Button(self)
        self.buttons[name]["text"] = name + " = 0"
        self.buttons[name]["command"] = partial(self.add_resource, name)
        self.buttons[name].pack(side="top")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

