import tkinter as tk #imports the Tkinter module, which is used to create your Graphical User Interface as "tk" for ease
from PIL import ImageTk, Image #imports the Pillow (PIL) module, which is used to implement images into your tK window
from tkinter import messagebox


root = tk.Tk()
root.configure(background='#5495f0') #sets the background color as defined by the hexcode

dataFile = open("data.txt","w")

#parallel arrays
age = []
submission = []#this is a list of names


def runMe():
  print("run me")
  #STEP 1: STORE THE AGE
  age.append(variable.get())
  submission.append(e.get("1.0",tk.END))

  print(age)
  print(submission)
def on_closing():
  print("closing")
  #STEP 2 - CREATE MESSAGEBOX
  if messagebox.askokcancel("Quit", "Do you want to quit?"):

    for i in range(0,len(age),1) :
      dataFile.write(age[i]+"\n")
      dataFile.write(submission[i]+"\n")


    dataFile.close()
    root.destroy()






#creates the title using the label function

title = tk.Label(text = "Vox Populi", font = ("Bebas", 70), bg = '#5495f0')
title.config()
title.grid(row = 0, column=1, padx = 0)

canvas = tk.Canvas(root, height=100, width=200,background='#5495f0')



#should create a rounded rectangle (see radd.py)



img = tk.PhotoImage(file="voxpopulai.png")      



canvas.create_image(50,50,image=img) 
canvas.config(highlightthickness="0") #configures whats inside the canvas
canvas.grid(row=0, column=2, rowspan = 2) #uses grid style geometry manager

e = tk.Text() #builds a text canvas
e.config()
e.grid(row=2, column=0, columnspan=4)



btn = tk.Button(text = "Submit", bd = 2,width =  20, command = runMe ) # builds a button widget, specifcally for the submission button
btn.config()
btn.grid(row=3, column=2, padx=29)


check = tk.Checkbutton(text = "Night Shift" , bd = 3  ) #creates a checkbutton widget
check.config()
check.grid(row= 3, column=1, pady=29, padx = 30 )

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
w.grid(row=3, column=1, sticky="e", pady=29, padx = 19)

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
w.grid(row= 3, column=3, pady = 29)





root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()



