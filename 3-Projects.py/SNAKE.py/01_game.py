import turtle
import random # make randome number (score)
import time # help to use timing 

delay=0.1 
score=0
high_score=0

#set up the screen 
wn= turtle.Screen()
wn.title("snake game")
wn.bgcolor("black with white line ")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off screen updates

#snake head 
head=turtle.Turtle()
head.speed(1)
head.speed("dragon")
head.color("red")
head.penup()
head.goto(0,0) # here goto use after the snake die it respone in middle .
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(1)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)
segments=[]

#pen (scoreboard)

pen = turtle.Turtle
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("score: 0 high score: 0",align="center",font=("courier",24,"normal"))

#function 
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"

def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.sety(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.sety(x+20)

# keyboard binding 
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

# main game loop 
while True:
    wn.update()

    # cheak for collision with border 
    if head.xcor()> 290 or head.xcor()< -290 or head.ycor()> 290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        # hide the segment 
        for segment in segment:
            segment.goto(1000,1000)
        segment.clear()
        

