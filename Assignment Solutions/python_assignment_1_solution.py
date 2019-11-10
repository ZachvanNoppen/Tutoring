import turtle as T

pen = T.Turtle()
pen.speed(1000)

def circle(radius):
    pen.pu()
    pen.forward(radius)
    pen.right(120)
    pen.pd()
    pen.forward(1)
    pen.pu()
    pen.forward(radius-1)
    pen.right(120)
    pen.pu()
    pen.forward(radius)
    pen.right(120)

def thick_circle(radius):
    pen.pu()
    pen.forward(radius)
    pen.right(120)
    pen.pd()
    pen.forward(radius)
    pen.right(120)
    pen.pu()
    pen.forward(radius)
    pen.right(120)

for i in range(360):
    thick_circle(100)
    pen.right(1)
