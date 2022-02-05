import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by Sam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score 
score_A = 0
score_B = 0


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


#Pen (turtle)
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_A}, PlayerB: {score_B}", align="center", font=("Courier", 24, "normal"))

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

    #ball border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

######
    #player a scores
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score_A +=1
        pen.clear()
        pen.write(f"Player A: {score_A}, PlayerB: {score_B}", align="center", font=("Courier", 24, "normal"))

    #Player b scores
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B +=1
        pen.clear()
        pen.write(f"Player A: {score_A}, PlayerB: {score_B}", align="center", font=("Courier", 24, "normal"))
  
#ball hits the B paddles
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor()-50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce_sound.wav", winsound.SND_ASYNC)


#ball hits the A paddles
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor()-50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce_sound.wav", winsound.SND_ASYNC)