import turtle

screen = turtle.Screen()
screen.bgcolor('white')

t = turtle.Turtle()

t.shape('turtle')
side_length = 5
for i in range(100):
    t.circle(100)
    t.rt(15)
    side_length = side_length+2

turtle.done()