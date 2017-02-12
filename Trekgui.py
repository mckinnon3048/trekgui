#!/usr/bin/python3

import tkinter as tk

manufacture = 0
research = 0
culture = 0
   
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.minsize(width=250, height=100)
        self.pack(side="top")
        self.create_Manufacture()
        self.create_Research()
        self.create_Culture()


    def create_Manufacture(self):
        global manufacture
        self.btn_manufacture = tk.Button(self)
        self.btn_manufacture["text"] = "Manufacture = 0"
        self.btn_manufacture["command"] = self.add_Manufacture
        self.btn_manufacture.pack(side="top")
                    
    def create_Research(self):
        self.btn_research = tk.Button(self)
        self.btn_research["text"] = "Research = 0"
        self.btn_research["command"] = self.add_Research
        self.btn_research.pack(side="top")

    def create_Culture(self):
        self.btn_culture = tk.Button(self)
        self.btn_culture["text"] = "Culture = 0"
        self.btn_culture["command"] = self.add_Culture
        self.btn_culture.pack(side="top")    
    

    def add_Manufacture(self):
        global manufacture
        manufacture += 1
        string = "Manufacture = " + str(manufacture)
        print(string)
        self.btn_manufacture["text"] = string
        
    def add_Research(self):
        global research
        research += 1
        string = "Research = " + str(research)
        print(string)
        self.btn_research["text"] = string
        
    def add_Culture(self):
        global culture
        culture += 1
        string = "Culture = " + str(culture)
        print(string)
        self.btn_culture["text"] = string

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

