import tkinter as tk #imports tkinter module as tk for simplicity




OPTIONS = [ #creates the options for the menu
    "egg",
    "bunny",
    "chicken"
]

master = tk.Tk() #defines master as tk.Tk



variable = tk.StringVar(master) 
variable.set(OPTIONS[0]) 

w = tk.OptionMenu(master, variable, *OPTIONS) # * indicates that each option should be treated 
w.pack()

master.mainloop()