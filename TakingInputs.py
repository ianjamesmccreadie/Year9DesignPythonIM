#comments are made with hashtags
#it is essential you comment code.

#this program will take two integers and multiply them

#input
#to change the type of variable, "cast it"
name = input("please input your name:")
a = input("please input first number:")
a = int(a)#self referencing assignment statement
b = input("please input second number:")
b = int(b)
#process
product = a * b
#output
print("Hi, " + name)
print("The product of"+str(a)+ "and" +str(b)+"is" + str(product)+ ".")