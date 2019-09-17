import math





print("STEP 2")

print("Volume of a Cylinder Formula: ")

name = input("What is your name: ")   #takes users name

radius = input("Input radius(cm): ")  #input
radius = (int)(radius)     #cast to int

height = input("Input height(cm): ") #input
height = (int)(height)     #cast to int

volume = math.pi * radius * radius * height

print ("The volume is" + str(volume) )