import turtle as trtl

painter = trtl.Turtle()

y = -150

num_floors = 63

color = "gray"

for floor in range(num_floors):
    painter.penup()
    painter.goto(x, y)
    if floor % 3 == 0:
        if color == "gray":
            color = "blue"
        else:
            color = "gray"
    painter.color(color)
    y = y + 5

wn = trtl.Screen()
wn.mainloop()