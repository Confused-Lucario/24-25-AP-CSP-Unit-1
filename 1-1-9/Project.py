#Philip Birkland
#jonathon frisco

import turtle as Turtle
global t
t = Turtle.Turtle()
Turtle.colormode(255)
t.speed(0)

t.pensize(10)
#canvase range is 800x800 square

def wave(r,g,b):
    global t
    t.pencolor((r,g,b))
    t.circle(575, extent=-10)
    t.pencolor("black")


#Making the wave of the ocean
t.penup()
t.goto(0,-10000)
t.pendown()
t.begin_fill()
t.color(195, 231, 245)
t.circle(10000,360,360)
t.end_fill()
t.penup()
ypos = -400
t.goto(400, ypos)

for waves in range(1,15):
    for dwaves in range(1,5):
        t.pendown()
        wave(45,84,239)
        t.left(20)
        wave(45, 84, 239)
        t.left(t.heading())
        t.penup()
    ypos += 10
    t.goto(400,ypos)
    for lwave in range(1,5):
        t.pendown()
        wave(101,132,225)
        t.left(20)
        wave(101, 132, 225)
        t.left(t.heading())
        t.penup()
    ypos += 10
    t.goto(400, ypos)



#Sun
t.penup()
t.goto(100,100)
t.color("yellow")
t.pendown()
t.pensize(30)
t.begin_fill()
t.circle(120,360,360)
t.end_fill()
t.pensize(10)
t.penup()



#Sailboat
t.goto(0,-100)
t.color("brown")
t.pendown()
t.pensize(10)
t.begin_fill()
t.right(90)
t.circle(50, 180, 360)
t.end_fill()
t.penup()
t.goto(50,-100)
t.pendown()
t.color("brown")
t.goto(50,-40)
t.left(60)
t.color(201, 205, 212)
t.begin_fill()
t.circle(30,360,3)
t.end_fill()
t.color("brown")
t.goto(50,-100)

#Border
t.color("black")
t.right(t.heading())
t.penup()
t.goto(400,-400)
t.pendown()
t.left(45)
t.circle(565,360,4)

t.left(t.heading()+-90)

while True:
    t.penup()
    t.goto(100, 100)
    t.color("yellow")
    t.pendown()
    t.pensize(30)
    t.begin_fill()
    t.circle(120, 360, 360)
    t.end_fill()
    t.pensize(10)
    t.penup()

    t.penup()
    t.goto(100, 100)
    t.color("orange")
    t.pendown()
    t.pensize(30)
    t.begin_fill()
    t.circle(120, 360, 360)
    t.end_fill()
    t.pensize(10)
    t.penup()

wn = Turtle.Screen()
wn.mainloop()



'''
blue wavy line, with different shades of blue
yellow semicircle as the sun, centered above the wavy line
fish scattered in the ocean
few clouds
'''