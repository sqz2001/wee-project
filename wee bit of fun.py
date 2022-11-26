import turtle
turtle.bgcolor("black")

t = turtle.Turtle()
t.reset()
t.pencolor("pink")
t.pensize(2)
t.penup()
t.goto(-300,200)

#h
t.pendown()
t.circle(-30,5)
t.rt(90)
t.fd(100)
t.circle(-30,20)
t.lt(10)
t.bk(50)
t.circle(50,60)

t.penup()
t.goto(-280,100)

#e
t.pendown()
t.circle(5,70)
t.circle(10,50)
t.circle(20,40)
t.circle(10,20)
t.circle(10,10)
t.circle(10,30)
t.circle(10,130)
t.rt(10)
t.fd(10)
t.lt(10)
t.fd(10)
t.lt(50)
t.fd(10)
t.lt(50)
t.fd(10)
t.lt(60)
t.fd(5)

t.penup()
t.goto(-260,120)

#y
t.pendown()
t.circle(-50,-30)
t.rt(30)
t.fd(10)
t.rt(10)
t.fd(5)
t.rt(30)
t.fd(10)
t.rt(10)
t.fd(10)
t.lt(60)
t.bk(60)
t.rt(60)
t.bk(20)
t.rt(60)
t.bk(10)

t.penup()
t.goto(-150,150)

#I
t.pendown()
t.rt(90)
t.fd(60)

t.penup()

#love
turtle.color("pink")
style = ("Courier", 90, "normal")
turtle.write("love", font=style, align='center')
turtle.hideturtle()

#back to "handwriting"
t.goto(170,20)

#u
t.pendown()
t.circle(30,180)
t.fd(20)
t.lt(30)
t.fd(30)

t.penup()
t.goto(-200,-200)

#<3
t.pendown()
t.lt(45)
t.fd(50)
t.setheading(90)
t.rt(45)
t.fd(50)
t.penup()
t.goto(-195,-200)
t.pendown()
t.setheading(-25)
t.circle(20, 230)
t.setheading(-25)
t.circle(20, 230)

turtle.done()

















