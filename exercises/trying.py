from turtle import Turtle, colormode, done

colormode(255)
a_turtle: Turtle = Turtle()


def square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1       
    done()


square(a_turtle, 30.0, 40.0, 300)


def only_evens(a: list[int]) -> list:
    evens: list = list()
    for item in a:
        if item % 2 == 0:
            evens.append(item)
    return evens