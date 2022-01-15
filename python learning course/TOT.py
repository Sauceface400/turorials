import turtle

dots = turtle.Turtle ()

dot_distance = 20
height = 5
width = 7

for i in range(height):
    for j in range(width):
        dots.dot()
        dots.forward(dot_distance)
    dots.backward(dot_distance*width)
    dots.right(90)
    dots.forward(dot_distance)
    dots.left(90)
    dots.forward(dot_distance)
turtle.done()

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()