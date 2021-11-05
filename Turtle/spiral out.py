import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('black')   

t = turtle.Turtle()
t.width(1)
t.color('red')
t.speed(30)

side_length = 5

def draw_square():
    global side_length
    for i in range(4):
        t.fd(side_length)
        t.rt(90)

for i in range(100):
    draw_square()
    t.rt(15)
    side_length = side_length+2

turtle.done()