
import turtle
from turtle import *

uae_flag = turtle.Turtle()

uae_flag.speed(4)



# Black lower
uae_flag.color('black')
uae_flag.begin_fill()
uae_flag.fd(500)
uae_flag.lt(90)
uae_flag.fd(120)
uae_flag.lt(90)
uae_flag.fd(500)
uae_flag.lt(90)
uae_flag.fd(120)
uae_flag.end_fill()
uae_flag.lt(180)
uae_flag.up()
uae_flag.fd(240)
uae_flag.rt(90)
uae_flag.down()

# green top
uae_flag.color("green", "green")
uae_flag.begin_fill()
uae_flag.fd(500)
uae_flag.lt(90)
uae_flag.fd(120)
uae_flag.lt(90)
uae_flag.fd(500)
uae_flag.lt(90)
uae_flag.fd(120)
uae_flag.end_fill()
uae_flag.fd(-120)

# red left side
uae_flag.color("Red")
uae_flag.begin_fill()
uae_flag.fd(360)
uae_flag.lt(90)
uae_flag.fd(150)
uae_flag.lt(90)
uae_flag.fd(360)
uae_flag.lt(90)
uae_flag.fd(150)
uae_flag.end_fill()




turtle.done()