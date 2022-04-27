from turtle import*
from random import randint

speed(0)
penup()
goto(-140, 140)

for passo in range(16):
    write(passo, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

bob = Turtle()
bob.color('red')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 100)
bob.pendown()

gigi = Turtle()
gigi.color('blue')
gigi.shape('turtle')

gigi.penup()
gigi.goto(-160, 70)
gigi.pendown()

jojo = Turtle()
jojo.color('black')
jojo.shape('turtle')

jojo.penup()
jojo.goto(-160, 40)
jojo.pendown()

for turn in range(100):
    bob.forward(randint(1, 5))
    gigi.forward(randint(1, 5))
    jojo.forward(randint(1, 5))