import tkinter

    
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
        self.btn_manufacture["text"] = "{Manufacture = } 0"
        self.btn_manufacture["command"] = self.add_Manufacture
        self.btn_manufacture.pack(side="top")
                    
    def create_Research(self):
        self.btn_research = tk.Button(self)
        self.btn_research["text"] = "{Research = } 0"
        self.btn_research["command"] = self.add_Research
        self.btn_research.pack(side="top")

    def create_Culture(self):
        self.btn_culture = tk.Button(self)
        self.btn_culture["text"] = "{Culture =} 0"
        self.btn_culture["command"] = self.add_Culture
        self.btn_culture.pack(side="top")    
    

    def add_Manufacture(self):
        global manufacture
        manufacture += 1
        print("Manufacture = ", manufacture)
        manufacture_Button = 'Manufacture = ', manufacture
        self.btn_manufacture.configure(text=manufacture_Button)
        
    def add_Research(self):
        global research
        research += 1
        print("Research = ", research)
        research_Button = 'Research = ', research
        self.btn_research.configure(text=research_Button)
        
    def add_Culture(self):
        global culture
        culture += 1
        print("Culture = ", culture)
        culture_Button = 'Culture = ', culture
        self.btn_culture.configure(text=culture_Button)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
