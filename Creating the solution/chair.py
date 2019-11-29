import tkinter as tk #imports the Tkinter module, which is used to create your Graphical User Interface as "tk" for ease
from PIL import ImageTk, Image #imports the Pillow (PIL) module, which is used to implement images into your tK window

root = tk.Tk()
root.configure(background='#5495f0') #sets the background color as defined by the hexcode

#creates the title using the label function

title = tk.Label(text = "Vox Populi")
title.config()
title.grid(row = 0)

canvas = tk.Canvas(root, height=100, width=200,background='#5495f0')



#should create a rounded rectangle (see radd.py)

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

my_rectangle = round_rectangle(50, 50, 150, 100, radius=20, fill="blue") #sets the paramaters for the size/color

img = PhotoImage(file="voxpopulai.png")      
canvas.create_image(20,20, anchor=NW, image=img) 



canvas.config() #configures whats inside the canvas
canvas.grid() #uses grid style geometry manager

e = tk.Text(canvas) #builds a text canvas
e.grid()

btn = tk.Button(text = "Submit", bd = 2,width =  40 ) # builds a button widget, specifcally for the submission button
btn.config()
btn.grid(row=3)


check = tk.Checkbutton(text = "Night Shift" , bd = 3, bg ="#5495f0", highlightbackground= "white" ) #creates a checkbutton widget
check.config()
check.grid(row= 2, sticky = "W")

#defines the options

OPTIONS = [ 
    "Arial",
    "Helvetica",
    "Roboto"
]
variable = tk.StringVar(root) 
variable.set(OPTIONS[0]) 


#defines the options

w = tk.OptionMenu(root, variable, *OPTIONS) 
w.config()
w.grid(row=2, sticky="E")

OPTIONS = [ 
    "Year 8",
    "Year 9",
    "Year 10"
    "Year 11"
    "Year 12"
]
variable = tk.StringVar(root) 
variable.set(OPTIONS[0]) 




w = tk.OptionMenu(root, variable, *OPTIONS) 
w.config()
w.grid(row=2, )


root.mainloop()
