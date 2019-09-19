import math





print("STEP 2")

print("Volume of a Cylinder Formula: ")

name = input("What is your name: ")   #takes users name

radius = input("Input radius(cm): ")  #input
radius = (int)(radius)     #cast to int

height = input("Input height(cm): ") #input
height = (int)(height)     #cast to int

volume = math.pi * radius * radius * height



volume = round(volume,2)



print("Hi " + name + "!")
print("Give a cylinder with:")
print("Radius = "+str(radius))
print("Height = "+str(height))
print("The volume is: "+str(volume))  
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")