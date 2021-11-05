import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('black')   

t = turtle.Turtle()
t.width(1)
t.color('red')
t.speed(30)

side_length = 20

def draw_square():
    global side_length
    for i in range(4):
        t.fd(side_length)
        t.rt(90)

for i in range(100):
    t.penup()
    t.goto(randint(-950,950), randint(-500,500))
    t.pendown()
    side_length = randint(10,100)
    draw_square()

turtle.done()