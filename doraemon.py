#Made by Stefven Torichie, Instagram : @stefventorichie
import turtle
t = turtle.Pen()
t.speed(10)
t.pencolor("black")
t.width(5)
turtle.bgcolor("cyan")
t.up()
t.setpos(0,200)
t.down()
t.write("Made by STEFVEN TORICHIE",  font=("Arial Black",10,"normal"))
t.up()
t.setpos(0,150)
t.down()

t.right(60)
t.fillcolor("white")
t.begin_fill()
t.circle(50,100)
t.circle(25,100)
t.circle(50,90)
t.circle(25,50)
t.up()
t.circle(25,25)
t.down()
t.end_fill()
t.up()
t.setpos(70,130)
t.down()
t.left(140)
for i in range (0,6):
    t.pencolor("cyan")
    t.forward(10)
    t.left(110)
    t.forward(10)
    t.right(110)
t.pencolor("black")
t.up()
t.left(110)
for i in range (0,2):
    t.backward(10)
    t.right(110)
    t.backward(10)
    t.left(110)
#face
t.right(180)
t.fd(7)
t.right(150)
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.circle(5,405)
t.forward(50)
t.left(90)
t.fd(10)
t.left(90)
t.fd(50)
t.end_fill()
t.backward(50)
t.right(90)
t.fillcolor("blue")
t.begin_fill()
t.circle(-130,150)
t.end_fill()
t.fillcolor("blue")
t.begin_fill()
t.circle(-130,-300)
t.end_fill()
t.fillcolor("white")
t.begin_fill()
t.right(8)
t.circle(-110,285)
t.end_fill()
t.circle(-110,-113)
t.left(120)
#eyes
t.fillcolor("white")
t.begin_fill()
for i in range(0,3):
    t.forward(30)
    t.circle(30,180)
t.end_fill()
t.fillcolor("white")
t.begin_fill()
t.circle(-30,-180)
t.backward(30)
t.circle(-30,-180)
t.backward(30)
t.end_fill()
t.up()
t.forward(30)
t.left(90)
t.forward(20)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()
t.up()
t.backward(40)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()
t.up()

t.right(90)
t.forward(20)
t.down()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()
t.circle(20,90)
t.right(90)
t.forward(50)
t.right(90)
t.forward(90)
t.fillcolor("white")
t.begin_fill()
t.circle(-30,230)
t.end_fill()
t.circle(-30,-230)
t.backward(90)
t.right(180)
t.forward(90)
t.fillcolor("white")
t.begin_fill()
t.circle(30,230)
t.end_fill()
t.up()
t.goto(25,-30)
t.down()
t.right(60)
t.forward(60)
t.up()
t.goto(25,-20)
t.down()
t.right(10)
t.forward(60)
t.up()
t.goto(25,-10)
t.down()
t.right(10)
t.forward(60)
t.up()
t.setpos(70,-30)
t.down()
t.right(140)
t.forward(60)
t.up()
t.goto(70,-20)
t.down()
t.left(10)
t.forward(60)
t.up()
t.goto(70,-10)
t.down()
t.left(10)
t.forward(70)
t.up()
t.goto(-30,-46)
t.right(120)
t.down()
t.fillcolor("red")
t.begin_fill()
t.circle(80,180)
t.end_fill()
t.circle(80,-60)
t.fillcolor("orange")
t.begin_fill()
t.circle(80,-60)
t.left(90)
t.circle(-50,115)
t.end_fill()
#lefthand
t.up()
t.goto(-23,-133)
t.down()
t.right(160)
t.fillcolor("blue")
t.begin_fill()
t.circle(-130,50)
t.left(100)
t.forward(50)
t.left(110)
t.forward(200)
t.end_fill()
t.up()
t.backward(160)
t.down()
t.right(310)
t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()
#righthand
t.up()
t.goto(120,-133)
t.down()
t.left(40)
t.fillcolor("blue")
t.begin_fill()
t.circle(130,50)
t.right(100)
t.forward(50)
t.right(110)
t.forward(200)
t.end_fill()
t.up()
t.backward(290)
t.left(310)
t.forward(80)
t.down()
t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()

#body
t.up()
t.setpos(-35,-135)
t.down()
t.fillcolor("blue")
t.begin_fill()
t.right(270)
t.forward(70)
t.circle(80,170)
t.forward(70)
t.end_fill()
t.backward(70)
t.left(45)
t.fillcolor("white")
t.begin_fill()
t.circle(100,105)
t.left(45)
t.circle(80,160)
t.end_fill()
t.up()
t.setpos(26,-220)
t.down()
t.right(80)
t.forward(50)
t.right(90)
t.circle(-25,180)


t.up()
t.setpos(-20,-125)

t.down()
t.right(150)
t.left(9)
t.fillcolor("white")
t.begin_fill()
t.circle(90,100)
t.end_fill()

t.circle(90,-95)
t.fillcolor("red")
t.begin_fill()
t.circle(90,95)
t.circle(-10,180)
t.circle(-110,100)
t.circle(-10,180)
t.end_fill()
t.circle(-10,-180)
t.circle(-110,-50)
t.up()
t.right(90)
t.forward(20)
t.down()
t.left(100)
t.fillcolor("yellow")
t.begin_fill()
t.circle(20)
t.end_fill()
t.circle(20,50)
t.left(120)
t.forward(30)
t.backward(30)
t.right(120)
t.circle(20,30)
t.left(90)
t.forward(40)

t.right(90)
t.up()
t.setpos(-20,-245)
t.down()
t.fillcolor("white")
t.begin_fill()
t.forward(30)
t.circle(30,180)
t.right(100)
t.circle(80,-40)
t.end_fill()

t.circle(80,60)
t.right(100)
t.fillcolor("white")
t.begin_fill()
t.circle(30,180)
t.forward(45)
t.left(150)
t.circle(-80,50)
t.end_fill()
