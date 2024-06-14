import tkinter as tk

class TodoComp(tk.Frame):
    def __init__(self, master=None, text="",  button1_text="Edit", button2_text="Delete", button1_command=None, button2_command=None, completed=False, checkbox_command=None,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.checkbox_var = tk.BooleanVar(value=completed)
        
        self.checkbox = tk.Checkbutton(self, variable=self.checkbox_var, command=checkbox_command)
        self.checkbox.grid(row=0, column=0, padx=5, pady=5)
        
        self.label = tk.Label(self, text=text)
        self.label.grid(row=0, column=1, padx=5, pady=5)
        
        self.button1 = tk.Button(self, text=button1_text, command=button1_command)
        self.button1.grid(row=0, column=2, padx=5, pady=5)
        
        self.button2 = tk.Button(self, text=button2_text, command=button2_command)
        self.button2.grid(row=0, column=3, padx=5, pady=5)

