import turtle as t

#canvase range is 800x800 square

t.penup()
t.goto(400,400)
t.pendown()
for num in range(1,5):
    t.forward(-800)
    t.left(90)
t.penup()
t.goto(0,0)
for wave in range(1,5):
    t.goto(400,-400)
    t.pendown()


wn = t.Screen()
wn.mainloop()
'''
blue wavy line, with different shades of blue
yellow semicircle as the sun, centered above the wavy line
fish scattered in the ocean
few clouds
thats it


'''