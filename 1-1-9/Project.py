import turtle as t
import turtle as Turtle
t.colormode(255)
t = t.Turtle()
t.pensize(5)
#canvase range is 800x800 square

def wave(r,g,b):
    t.pencolor((r,g,b))
    t.circle(575, -10)
    t.pencolor("black")


#Making the wave of the ocean

t.penup()
t.goto(400,-400)
for Waves in range(1,10):
    for waves in range(1,5):
        t.pendown()
        wave(45,84,239)
        t.left(20)
        wave(45, 84, 239)
        t.left(t.heading())
    t.goto(400,-400*)


t.right(t.heading())
t.penup()
t.goto(400,400)
t.pendown()
for num in range(1,5):
    t.forward(-800)
    t.left(90)

num1 = 1
num2 = 2
#while num1 != num2:
#    t.color

wn = Turtle.Screen()
wn.mainloop()
'''
blue wavy line, with different shades of blue
yellow semicircle as the sun, centered above the wavy line
fish scattered in the ocean
few clouds
thats it


'''