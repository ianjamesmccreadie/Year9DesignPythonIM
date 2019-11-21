import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.configure(background='#5495f0')

img = ImageTk.PhotoImage(Image.open("scad3.jpg"))
panel = Label(root, image = img)
panel.grid()


title = tk.Label(text = "Vox Populi")
title.config()
title.grid(row = 0)

canvas = tk.Canvas(root, height=200, width=300,background='#5495f0')
canvas.create_rectangle(4, 0, 10, 20)
canvas.create_text(sticky = "W")


canvas.config()
canvas.grijpg
check = tk.Checkbutton(text = "Night Shift" , bd = 3)
check.config()
check.grid(row= 2, sticky = "W", font = "Roboto")

OPTIONS = [ 
    "Arial",
    "Helvetica",
    "Roboto"
]
variable = tk.StringVar(root) 
variable.set(OPTIONS[0]) 

w = tk.OptionMenu(root, variable, *OPTIONS) 
w.config()
w.grid(row=2, sticky="E")


root.mainloop()