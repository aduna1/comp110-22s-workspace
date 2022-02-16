"""A pretty field of flowers, a tree, and sun, I call it: High Noon."""

__author__ = "730469821"

from random import randint
from turtle import Turtle, colormode, Screen, done


colormode(255)
Screen().bgcolor(119, 200, 242)


def main() -> None:
    """The entrypoint of my scene."""
    tut: Turtle = Turtle()
    MAX_SPEED = 0
    tut.speed(MAX_SPEED)
    sun_draw(tut, 0, 350, 100)
    treetrunk_draw(tut, -250, -400, 425, 50)
    leaves_draw(tut, -375, -85, 270)
    apples_draw(tut, -300, -70, 8)
    bird_draw(tut, 50, 70, 45)
    bird_draw(tut, 80, 150, 45)
    grass_draw(tut, -775, -400, 100)
    flower_draw_1(tut, -725, -300, 60)
    flower_draw_2(tut, -730, -315, 60)

    done()


def sun_draw(turtle_1: Turtle, x: float, y: float, ray_num: float) -> None:
    """This puts the sun at the highest point in the sky."""
    turtle_1.color(226, 197, 5)
    turtle_1.penup()
    turtle_1.goto(x, y) 
    turtle_1.setheading(0.0)
    turtle_1.pendown()
    turtle_1.begin_fill()
    i: int = 0
    rays: int = 10
    while i < rays:
        turtle_1.forward(ray_num)
        turtle_1.right(100)
        i += 1
    turtle_1.end_fill()       


def treetrunk_draw(turtle_2: Turtle, x: float, y: float, trunk_l: float, trunk_w: float) -> None:
    """Creates a trunk for a tree."""
    turtle_2.color(130, 104, 70)
    turtle_2.penup()
    turtle_2.goto(x, y) 
    turtle_2.setheading(90)
    turtle_2.pendown()
    turtle_2.begin_fill()
    i: int = 0
    trunk_shape: int = 2
    while i < trunk_shape:
        turtle_2.forward(trunk_l)
        turtle_2.right(90)
        turtle_2.forward(trunk_w)
        turtle_2.right(90)
        i += 1
    turtle_2.end_fill()   


def leaves_draw(turtle_3: Turtle, x: float, y: float, leaves: float) -> None:
    """Puts leaves on top of the tree trunk."""
    turtle_3.color(16, 134, 28)
    turtle_3.penup()
    turtle_3.goto(x, y) 
    turtle_3.setheading(75)
    turtle_3.pendown()
    turtle_3.begin_fill()
    i: int = 0
    leaf_num: int = 10
    while i < leaf_num:
        turtle_3.forward(leaves)
        turtle_3.right(100)
        i += 1
    turtle_3.end_fill()       


def grass_draw(turtle_4: Turtle, x: float, y: float, blade: float) -> None:
    """This function provides the scene with grass."""
    turtle_4.color(95, 181, 14)
    turtle_4.penup()
    turtle_4.goto(x, y) 
    turtle_4.setheading(88)
    turtle_4.pendown()
    turtle_4.begin_fill()
    i: int = 0
    blades: int = 176
    while i < blades:
        turtle_4.forward(blade)
        turtle_4.right(175)
        turtle_4.forward(blade)
        turtle_4.left(175)
        i += 1
    turtle_4.end_fill()


def apples_draw(turtle_5: Turtle, x: float, y: float, apple_num: float) -> None:
    """Here I attempt to try something fun and use the turtle.circle and randint functions to draw apples on my tree."""
    turtle_5.color(230, 44, 25)
    turtle_5.penup()
    turtle_5.goto(x, y) 
    turtle_5.setheading(90)
    turtle_5.pendown()
    i: int = 0
    while i < apple_num:
        turtle_5.begin_fill()
        apple_loc_1: int = randint(-350, -50)
        apple_loc_2: int = randint(-85, 100)
        turtle_5.circle(15)
        turtle_5.penup()
        turtle_5.goto(apple_loc_1, apple_loc_2)
        turtle_5.pendown()
        i += 1
        turtle_5.end_fill()


def flower_draw_1(turtle_6: Turtle, x: float, y: float, petals: float) -> None:
    """Decorates the grass with round purple flowers."""
    turtle_6.color(190, 169, 247)
    turtle_6.penup()
    turtle_6.goto(x, y)
    turtle_6.setheading(90)
    turtle_6.pendown()
    i: int = 0
    while i < petals:
        turtle_6.begin_fill()
        turtle_6.circle(10)
        turtle_6.penup()
        x += 25
        turtle_6.goto(x, y)
        turtle_6.pendown()
        i += 1
        turtle_6.end_fill()


def flower_draw_2(turtle_7: Turtle, x: float, y: float, petals: float) -> None:
    """Decorates the grass with round purple flowers."""
    turtle_7.color(107, 57, 242)
    turtle_7.penup()
    turtle_7.goto(x, y)
    turtle_7.setheading(90)
    turtle_7.pendown()
    i: int = 0
    while i < petals:
        turtle_7.begin_fill()
        turtle_7.circle(10)
        turtle_7.penup()
        x += 25
        turtle_7.goto(x, y)
        turtle_7.pendown()
        i += 1
        turtle_7.end_fill()

        
def bird_draw(turtle_8: Turtle, x: float, y: float, wings: float) -> None:
    """Places a bird in the sky."""
    turtle_8.color(0, 0, 0)
    turtle_8.penup()
    turtle_8.goto(x, y)
    turtle_8.setheading(315)
    turtle_8.pendown()
    turtle_8.forward(wings)
    turtle_8.left(90)
    turtle_8.forward(wings)


if __name__ == "__main__":
    main()