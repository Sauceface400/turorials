from turtle import *
from random import randint 
speed(0)
#==========================this will make the race track filled with numbers to show distance's===============
penup()
goto(-140,140)
pendown()
for step in range(21):#This coding means for every 20 movement of the turtle it'll write 1 to 5
    write(step, align= 'left')
    right(90)
    penup() 
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
#===============================Making the turtles===============================================
t1=Turtle()
t1.color("black")
t1.shape("turtle")
t1.penup()
t1.goto(-160,100)
t1.pendown()

t2=Turtle()
t2.color("green")
t2.shape("turtle")
t2.penup()
t2.goto(-160,80)
t2.pendown()

t3=Turtle()
t3.color("blue")
t3.shape("turtle")
t3.penup()
t3.goto(-160,60)
t3.pendown()

t4=Turtle()
t4.color("red")
t4.shape("turtle")
t4.penup()
t4.goto(-160,40)
t4.pendown()

t5=Turtle()
t5.color("yellow")
t5.shape("turtle")
t5.penup()
t5.goto(-160,20)
t5.pendown()
#===================================Makeing the turtle move at diffrent distance's=========================
for movement in range(135):#the distance that the turtle will move 
    t1.forward(randint(1,5))#the (randint(1,5)) will move the turtle at diffrent speeds
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
    t4.forward(randint(1,5))
    t5.forward(randint(1,5))

done()