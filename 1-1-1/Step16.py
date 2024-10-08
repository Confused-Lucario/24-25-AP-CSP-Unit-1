import turtle as trtl

painter = trtl.Turtle()

painter.speed(1000000)
radius = 300
x = 0
r = 0
s = 1
e = 1
painter.penup()
painter.goto(0,0)
painter.pendown()
while True:
    radius *= -1
    painter.forward(x)
    painter.right(20)
    painter.circle(r, e, s)
    x = x + .05
    r = r + .5
    e = e + 1
    s = 360

wn = trtl.Screen()
wn.mainloop()