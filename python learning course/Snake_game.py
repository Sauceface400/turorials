#=========================this is snake game===================================
import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

#Set up the screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

segments = []

#the pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High score: 0", align = "center", font = ("Courier" ,24 , "normal"))

#Functions of the snakes movement
def goto_up():
    if head.direction != "down":
        head.direction = "up"

def goto_down():
    if head.direction != "up":
        head.direction = "down"

def goto_left():
    if head.direction != "right":
        head.direction = "left"

def goto_right():
    if head.direction != "left":
        head.direction = "right"


def control():   
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Controls for the snakes(keybindings)
wn.listen()
wn.onkeypress(goto_up, "w")
wn.onkeypress(goto_down, "s")
wn.onkeypress(goto_left, "d")
wn.onkeypress(goto_right, "a")

#loop for the game
while True:
    wn.update()
    #Collition with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction ="stop"
        #hide the segment of the snake
        for segment in segments:
            segment.goto(1000,1000)
        #clear the list of the segment
        segments.clear()
        #reset the score
        score = 0
        #reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score), align = "center", font = ("Courier" ,24 , "normal"))
#collition with the food
if head.distance(food) < 20:
    #move the food in random position
    x = random.randint(-290,290)
    y = random.randint(-290,290)
    food.goto(x,y)
        
    #Add the segment of the snake
    new_segement = turtle.Turtle()
    new_segement.speed(0)
    new_segement.shape("triangle")
    new_segement.color("blue")
    new_segement.penup()
    segments.append(new_segement)
    #shorten the delay 
    delay -= 0.001
    #increase the score
    score += 10
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write("Score: {} High score: {}".format(score, high_score), align = "center", font = ("Courier" ,24 , "normal"))
    #move the end segment in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)
#move the segemnt 0 to where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

control()

#collition with the body
for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #hide the segment
        for segment in segments:
            segment.goto(1000,1000)
        #clear the list of the segment
        segments.clear()
        #reset the score
        score = 0
        #reset the delay
        delay = 0.1
        #displat and score and update it
        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score), align = "center", font = ("Courier" ,24 , "normal"))
     
    time.sleep(delay)

wn.mainloop()
