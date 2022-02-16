from turtle import Turtle, colormode, done

colormode(255)

leo: Turtle = Turtle()


leo.color(199, 167, 218)

leo.penup()
leo.goto(-300, -300)
leo.pendown()

leo.speed(50)
leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(700)
    leo.left(120)
    i += 1
leo.end_fill()

leo.hideturtle()


bob: Turtle = Turtle()

bob.color(143, 0, 230)
bob.penup()
bob.goto(-300, -300)
bob.pendown()
bob.speed(100)

side_length: int = 700


i: int = 0
while i < 3:
    side_length = side_length * 0.90
    bob.forward(side_length)
    bob.left(123)
    i += 1
done()