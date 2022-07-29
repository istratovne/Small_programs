import turtle as t

# GLOBAL DEFINES
a = 50
b = a * 2 ** 0.5


def position():
    t.forward(a)
    t.pendown()


def zero():
    for _ in range(2):
        t.forward(a)
        t.right(90)
        t.forward(2 * a)
        t.right(90)
    t.penup()
    t.forward(a)


def one():
    t.right(90)
    t.penup()
    t.forward(a)
    t.pendown()
    t.left(135)
    t.forward(b)
    t.right(135)
    t.forward(a * 2)
    t.penup()
    t.left(180)
    t.forward(a * 2)
    t.right(90)


def two():
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(45)
    t.forward(b)
    t.left(135)
    t.forward(a)
    t.penup()
    t.left(90)
    t.forward(2 * a)
    t.right(90)


def three():
    for _ in range(2):
        t.forward(a)
        t.right(135)
        t.forward(b)
        t.left(135)
    t.penup()
    t.forward(a)
    t.left(90)
    t.forward(2 * a)
    t.left(90)


def four():
    t.right(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.penup()
    t.left(180)
    t.forward(a)
    t.pendown()
    t.forward(a)
    t.right(90)
    t.penup()


def five():
    t.penup()
    t.forward(a)
    t.left(180)
    t.pendown()
    for _ in range(2):
        t.forward(a)
        t.left(90)
    for _ in range(2):
        t.forward(a)
        t.right(90)
    t.forward(a)
    t.penup()
    t.right(90)
    t.forward(2 * a)
    t.right(90)
    t.forward(a)


def six():
    t.penup()
    t.forward(a)
    t.right(135)
    t.pendown()
    t.forward(b)
    t.left(45)
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.left(135)
    t.penup()
    t.forward(b)
    t.right(45)


def seven():
    t.forward(a)
    t.right(135)
    t.forward(b)
    t.left(45)
    t.forward(a)
    t.left(180)
    t.penup()
    t.forward(2 * a)
    t.right(90)
    t.forward(a)


def eight():
    for _ in range(4):
        t.forward(a)
        t.right(90)
    t.penup()
    t.right(90)
    t.forward(a)
    t.pendown()
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.penup()
    t.left(135)
    t.forward(b)
    t.right(45)


def nine():
    for _ in range(4):
        t.forward(a)
        t.right(90)
    t.right(45)
    t.penup()
    t.forward(b)
    t.right(90)
    t.pendown()
    t.forward(b)
    t.penup()
    t.left(180)
    t.forward(b)
    t.left(45)
    t.forward(a)
    t.right(90)


def start_position():
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.speed(10)


def drawing(digit):
    t.pencolor('blue')
    match digit:
        case '0':
            zero()
            position()
        case '1':
            one()
            position()
        case '2':
            two()
            position()
        case '3':
            three()
            position()
        case '4':
            four()
            position()
        case '5':
            five()
            position()
        case '6':
            six()
            position()
        case '7':
            seven()
            position()
        case '8':
            eight()
            position()
        case '9':
            nine()
            position()


if __name__ == '__main__':
    ind = input('Input index ')
    start_position()
    for i in range(6):
        drawing(ind[i])
    t.hideturtle()
    t.done()
