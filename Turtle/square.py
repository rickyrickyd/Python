import turtle
from random import randint


# Set the background color
screen = turtle.Screen()
screen.bgcolor('white')   # black

# Create a turle
t = turtle.Turtle()
t.width(1)
t.color('red')
t.speed(30)

side_length = 50

# t.penup()
t.goto(951,0)
t.pendown()
t.goto(951,-498)
t.goto(-955,-505)
t.goto(-955,505)
t.goto(951,498)
t.goto(951,0)

t.penup()
t.goto(0,0)
t.pendown()

# def draw_square():
#     global side_length
#     global i
#     for i in range(4):
#         t.fd(side_length)
#         t.rt(90)
# def draw_multiple_square():
#     global i
#     global side_length
#     for i in range(4):
#         side_length = 25
#         draw_square()
#         side_length = 50
#         draw_square()
#         side_length = 100
#         draw_square()
#         side_length = 150
#         draw_square()
#         side_length = 200
#         draw_square()
#         t.rt(90)

# for i in range(36):
#     draw_multiple_square()
#     t.left(10)

turtle.done()