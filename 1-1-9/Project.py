import turtle as t
import turtle as Turtle
t.colormode(255)
t = t.Turtle()
t.pensize(10)
t_height = -400
#canvase range is 800x800 square

def wave(r,g,b):
    t.pencolor((r,g,b))
    t.circle(575,-10)
    t.pencolor("black")


#Making the wave of the ocean

t.penup()
t.goto(400,-400)
for waves in range(1,10):
    for dwaves in range(1,5):
        t.pendown()
        wave(45,84,239)
        t.left(20)
        wave(45, 84, 239)
        t.left(t.heading())
        t.penup()
    t_height =+ 10
    t.goto(400,t_height)
    for lwave in range(1,5):
        t.pendown()
        wave(101,132,225)
        t.left(20)
        wave(101, 132, 225)
        t.left(t.heading())
        t.penup()
    t_height =+ 10
    t.goto(400,t_height)



#Sun
t.penup()
t.goto(100,100)
t.pendown()
t.circle(10,10,10)
t.color("yellow")

#Snake
t.penup()
t.goto(50,0)
t.forward(20)
t.color("green")


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