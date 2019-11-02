import tkinter as tk
parent_widget = tk.Tk()

canvas_widget = tk.Canvas(parent_widget, bg = "red",width=1000,height= 500)
canvas_widget.pack()
parent_widget.mainloop()

