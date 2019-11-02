import tkinter as tk

print("Start Program")
root = tk.Tk() #builds your main window

#Widget (AKA element) is a element in a GUI for example 
#a Button, textbox, slider, dropdown, image
#TKinter can build all them
#Every widget has 3 steps
#step1: Construct the Widget

btn1 = tk.Button(root, width = 50, height = 6)

#step2: Configure the widget
#"text" is what's known as a named parameter 

btn1.config(text = "I am a button")

#step3: Place the widget - pack(), grid()


btn1.pack()

output = tk.Text(root, width = 100, height = 50)

output.config()

output.pack();



root.mainloop()

print("END PROGRAM")

