import turtle

t = turtle.Turtle()

t.reset()
t.pencolor('green')
t.pensize(5)
t.penup()
# M
t.goto(-300,-20)
t.pendown()
t.left(90)
t.forward(200)
t.right(150)
t.forward(100)
t.left(120)
t.forward(100)
t.right(150)
t.forward(200)
t.penup()

# A
t.goto(-200, -10)
t.pencolor('blue')
t.pendown()
t.left(160)
t.forward(100)
t.right(45)
t.forward(50)
t.backward(50)
t.left(45)
t.forward(100)
t.right(150)
t.forward(200)
t.penup()

# N
t.goto(-100,-10)
t.pencolor('red')
t.pendown()
t.left(160)
t.forward(200)
t.right(130)
t.forward(100)
t.left(120)
t.forward(100)
t.penup()

# T
t.goto(50, -10)
t.pencolor('green')
t.pendown()
t.left(20)
t.forward(200)
t.right(90)
t.forward(50)
t.backward(100)
t.penup()
# H
t.goto(120, -10)
t.pencolor('green')
t.pendown()
t.left(90)
t.forward(200)
t.backward(100)
t.right(90)
t.forward(75)
t.left(90)
t.forward(100)
t.backward(200)
t.penup()

# A
t.goto(195, -10)
t.pencolor('blue')
t.pendown()
t.right(20)
t.forward(100)
t.right(45)
t.forward(50)
t.backward(50)
t.left(45)
t.forward(100)
t.right(150)
t.forward(200)
t.penup()

# N
t.goto(300,-10)
t.pencolor('red')
t.pendown()
t.left(160)
t.forward(200)
t.right(130)
t.forward(100)
t.left(120)
t.forward(100)
t.penup()

t.goto(-300, -50)
t.pencolor('brown')
t.pendown()
t.right(70)
t.forward(600)
t.right(170)
t.forward(550)
t.left(170)
t.forward(400)
t.right(170)
t.forward(350)
t.left(170)
t.forward(200)
t.right(170)
t.forward(100)
t.penup()