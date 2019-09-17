#Input
#What inputs are needed to calculate the volume of a cylinder?

#Process
#What formula is used to calculate the volume of a cylinder?

#Output
#What is important about the output?
print("Volume of a Cylinder Formula: ")

name = input("What is your name: ")   #takes users name

radius = input("Input radius(cm): ")  #input
radius = (int)(radius)     #cast to int

height = input("Input height(cm): ") #input
height = (int)(height)     #cast to int

volume = 3.14 * radius * radius * height

print (volume)