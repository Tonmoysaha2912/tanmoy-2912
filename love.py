import turtle as tur
scr = tur.Screen()
scr.bgcolor("grey")
scr.screensize(3200,2400)
t = tur.Turtle()
t.speed("slow")
t.color("black")
t.penup()
t.goto(-250,0)
t.pendown()
t.backward(100)
t.left(60)
t.forward(200)
# print(t.position())
t.setheading(270)
t.forward(250)
t.circle(-60,120)
# print(t.position())
t.penup()
t.goto(0,-128.76)
t.pendown()
t.right(15)
t.fillcolor("red")
t.begin_fill()
t.forward(230)
t.circle(-90,210)
t.setheading(74.5)
t.circle(-100,210)
t.forward(218)
t.end_fill()
t.penup()
t.goto(250,171.23)
t.pendown()
t.left(46)
t.forward(200)
t.circle(100,180)
t.forward(200)
t.hideturtle()
tur.done()
