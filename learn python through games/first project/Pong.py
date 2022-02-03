import turtle

wn = turtle.Screen()
wn.title("Pong by Sam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.penup()
paddle_a.shapesize(stretch_wid= 5, stretch_len=1)
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.penup()
paddle_b.shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)

#ball movment
ball.dx = .25

ball.dy = -.25

#Functions

def paddle_a_up():
    #moves paddle A Up
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    #moves paddle A Down
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    #moves paddle B Up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    #moves paddle B Down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)




# Keyboard Binding

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'i')
wn.onkeypress(paddle_b_down, 'k')

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() >390 or ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1

    #if ball.xcor() <-390:
    #    ball.goto(0,0)
    #    ball.dx *= -1