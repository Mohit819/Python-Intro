import turtle
from random import randint # this is how we get random numbers
# create a screen object called 'screen'
screen = turtle.Screen()
# set the background colour to black
screen.bgcolor('black')
# create a turtle named 'me' this will be the turtle you control
me = turtle.Turtle()
# set the turtle's colour to your favourite colour
me.color('purple')
# create a new turtle named 'dot', they will draw the stars
dot = turtle.Turtle()
# set dot's speed to 0
dot.speed(0)
# dot needs to lift their pen
dot.penup()
# dot needs to be invisible
dot.hideturtle()
# set dot's colour to white
dot.color('white')
screen.onclick(me.goto)
for i in range(20): # change '20' to a bigger number for more stars!
    dot.goto(randint(-200,200), randint(-200,200)) #random place
    dot.begin_fill()
    dot.circle(randint(3,10)) #dot draws a circle of random size
    dot.end_fill() # the circle is filled in!
