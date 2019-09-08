"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
"""

import turtle
import math

def golden_spiral1():
    # fibbionaci
    a = 0
    b = 1

    # go up
    turtle.left(90)

    while b < 610:
        b += a
        a = b - a

        # create 90 degrees circle with radius b
        turtle.circle(b, extent = 90)

    turtle.done()

def golden_spiral2():
    # fibbionaci
    a = 0
    b = 1

    # go up
    turtle.left(90)

    while b < 610:
        b += a
        a = b - a

        cir = 2 * b * math.pi / 4

        num_steps = 10
        if cir > 50:
            num_steps = 100
        elif cir > 10:
            num_steps = 50

        step = cir / num_steps
        angle = 90 / num_steps

        i = 0
        while i < num_steps:
            turtle.left(angle)
            turtle.forward(step)
            i += 1

    turtle.done()