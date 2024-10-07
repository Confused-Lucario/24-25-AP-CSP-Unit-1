#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

startx = 0
starty = 0

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

# defines the turtle as t and adds it to the list of "my_turtles"


# defining where the turtle is to return after each shape is drawn
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(45)
  t.forward(50)

# moves the turtle to create a line
  startx = my_turtles.xcor()
  starty = my_turtles.ycor()

wn = trtl.Screen()
wn.mainloop()