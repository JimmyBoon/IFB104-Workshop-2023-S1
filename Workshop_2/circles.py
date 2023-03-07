# Three non-overlapping circles
#
# As a simple exercise in using the Turtle package you are
# required to draw three circles on the screen.  Each circle
# must be of a different size and colour.  Most importantly,
# the circles must not touch or overlap at any point, nor
# can one circle appear inside another.
#
# NB: We want unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# The basic strategy for drawing each circle is to lift
# up the pen, move to a suitable location on the screen,
# choose a colour, put the pen down and walk in a circle.
# Having done this once you can copy your code (with minor
# changes) three times.
#
# Observation: Turtle's "circle" function does NOT draw a
# circle centred at the current location.  Instead it causes
# the turtle to walk in a circle, ending up back where
# it started.

from turtle import *
from random import randint

setup()
title('Three non-overlapping circles')
colormode(255)


def draw_circle(pos_x, pos_y, size):
    colour = (randint(0,255),randint(0,255),randint(0,255))
    pencolor(colour)
    penup()
    pensize(randint(2,10))
    goto(pos_x, pos_y)
    forward(size)
    left(90)
    pendown()
    circle(size)

for i in range(1,11):
    draw_circle(randint(-200,200), randint(-200,200), 5*i)
    

hideturtle()
done()
