import tkinter as tk #imports the Tkinter module, which is used to create your Graphical User Interface as "tk" for ease
from PIL import ImageTk, Image #imports the Pillow (PIL) module, which is used to implement images into your tK window
from tkinter import messagebox
import csv


root = tk.Tk()
root.configure(background='#5495f0') #sets the background color as defined by the hexcode

def submission():
  file = open('database.csv', 'a+')
  gradewriter = csv.DictWriter(file, fieldnames = fieldnames)
  gradewriter.writerow({'submission': submission.get(), 'age': age.get()})
  file.close()
  submission.set('')
  age.set('')
  

#parallel arrays
age = []
submission = []#this is a list of names


    root.destroy()






#creates the title using the label function

title = tk.Label(text = "Vox Populi", font = ("Bebas", 50), bg = '#5495f0')
title.config()
title.grid(row = 0, column=1)

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

my_rectangle = round_rectangle(100, 25, 250, 75, radius=20, fill="blue") #sets the paramaters for the size/color


img = tk.PhotoImage(file="voxpopulai.png")      



canvas.create_image(50,50,image=img) 
canvas.config(highlightthickness="0") #configures whats inside the canvas
canvas.grid(row=0, column=0) #uses grid style geometry manager

e = tk.Text(textvariable=submission) #builds a text canvas
e.config()
e.grid(row=2, column=0, columnspan=4)



btn = tk.Button(text = "Submit", bd = 2,width =  20, command = submission) # builds a button widget, specifcally for the submission button
btn.config()
btn.grid(row=3, column=2)


check = tk.Checkbutton(text = "Night Shift" , bd = 3  ) #creates a checkbutton widget
check.config()
check.grid(row= 3, column=0, sticky = "SW")

#defines the options

OPTIONS = [ 
    "Arial",
    "Helvetica",
    "Roboto"
]
variable = tk.StringVar(root) 
variable.set(OPTIONS[0]) 


#defines the options

w = tk.OptionMenu(root, variable, *OPTIONS, textvariable = age) 
w.config()
w.grid(row=3, column=1, sticky="e")

OPTIONS = [ 
    "Year 8",
    "Year 9",
    "Year 10",
    "Year 11",
    "Year 12",
]
variable = tk.StringVar(root) 
variable.set(OPTIONS[0]) 




w = tk.OptionMenu(root, variable, *OPTIONS) 
w.config()
w.grid(row=3, column=3, sticky = "SE" )





root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()



