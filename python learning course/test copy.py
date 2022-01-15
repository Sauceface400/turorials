from turtle import *
from random import randint

penup()
goto(-60,200)
write("Turtle race sucker\'s",font =("Arial"))
bgcolor("forestgreen")
pendown()

speed(0)
penup()
goto(-140,180)
pendown()

for track in range(11):
    write(track)
    right(90)
    penup()
    forward(17)
    pendown()
    forward(100)
    penup()
    backward(117)
    left(90)
    forward(20)

contestant_1 = Turtle()
contestant_1.color("white")
contestant_1.shape("square")
contestant_1.penup()
contestant_1.goto(-160,140)
contestant_1.pendown()

contestant_2 = Turtle()
contestant_2.color("red")
contestant_2.shape("square")
contestant_2.penup()
contestant_2.goto(-160,90)
contestant_2.pendown()

for accelerate in range(58):
    contestant_1.forward(randint(1,7))
    contestant_2.forward(randint(1,7))

done()
