import turtle as trtl

painter = trtl.Turtle()

painter.speed("fastest")

x = 0
painter.penup()
painter.goto(0,-200)
painter.pendown()
while True:
    painter.forward(x)
    painter.right(20)
    painter.circle(300, 1000, 10)
    x = x + .1

wn = trtl.Screen()
wn.mainloop()