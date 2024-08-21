import turtle
screen = turtle.Screen()
mohit= turtle.Turtle() # replace ‘sam’ with your name
screen.onclick(mohit.goto)
# create our screen
screen.bgcolor("black")
# starting with a black screen
a = turtle.Turtle() # making 4 turtles
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
a.shape("turtle") # make them all turtle-shaped
b.shape("turtle")
c.shape("turtle")
d.shape("turtle")
a.color("blue") # they each get a colour
b.color("purple")
c.color("grey")
d.color("red")
a.penup() # we don't need them drawing
b.penup()
c.penup()
d.penup()
a.goto(100,0) # using goto to have them jump around
b.goto(-100,0) # you could also use forward and backward
c.goto(300,0)
d.goto(-300,0)
screen.bgcolor("pink") # change the background colour to make it fun!
a.right(69)
b.right(69)
c.right(69)
d.right(69)
screen.bgcolor("light blue")
a.left(121)
b.left(121)
c.left(121)
d.left(121)
screen.bgcolor("yellow") # repeat the steps to create a dance routine
a.right(69)
b.right(69)
c.right(69)
d.right(69)
screen.bgcolor("blue")
a.left(121)
b.left(121)
c.left(121)
d.left(121)
screen.bgcolor("white")
a.right(69)
b.right(69)
c.right(69)
d.right(69)
screen.bgcolor("orange")
a.left(121)
b.left(121)
c.left(121)
d.left(121)
screen.bgcolor("green")
a.right(6)
b.right(6)
c.right(6)
d.right(6)
screen.bgcolor("light green")
a.left(1)
b.left(1)
c.left(1)
d.left(1)
screen.bgcolor("brown")

