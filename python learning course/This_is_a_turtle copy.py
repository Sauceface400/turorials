import turtle
p = turtle.Turtle()

def sphere(length,width,height): #This is the finishing coordinate so that you dont have to write long codes
    p.circle(length)
    p.circle(50)
    p.right(width)
    p.circle(height)
    
sphere(100,90,100) #make a variable them put the numbers in the bracket 
turtle.done() 
#This is for pausing the monitor so that it wont close everytime a turtle has finish drawing the lines
    

