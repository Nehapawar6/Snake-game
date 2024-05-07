import turtle
import tkinter as tk
import random

wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0) 

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack() 

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(260, 260)


def go_up(event):
    if head.direction != "down":
        head.direction = "up"

def go_down(event):
    if head.direction != "up":
        head.direction = "down"

def go_left(event):
    if head.direction != "right":
        head.direction = "left"

def go_right(event):
    if head.direction != "left":
        head.direction = "right"

def move():
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

    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()

    
    if head.distance(food) < 20:
    
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        global score
        score += 1
        update_score()

    root.after(100, move)

def game_over():
    score_display.goto(0, 0)
    score_display.write("Game Over", align="center", font=("Courier", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

root.bind("<w>", go_up)
root.bind("<s>", go_down)
root.bind("<a>", go_left)
root.bind("<d>", go_right)

move()

update_score()

while True:
    wn.update()

root.mainloop()
