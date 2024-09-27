import turtle as trtl

painter = trtl.Turtle()

painter.screensize(5000, 3000)
painter.speed(1000000)
radius = 300
x = 0
painter.penup()
painter.goto(0,0)
painter.pendown()
while True:
    radius *= -1
    painter.forward(x)
    painter.right(20)
    painter.circle(radius, 1360, 360)
    x = x + .05

wn = trtl.Screen()
wn.mainloop()