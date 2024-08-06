from pickle import TRUE
import turtle


wn = turtle.Screen()
wn.title("pong")
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=6,stretch_len=1)

#paddleB

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=6,stretch_len=1)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.shapesize()
ball.penup()
ball.goto(0,0)
#paddleA
def paddle_a_up():
    y=paddle_a.ycor()
    y+=40
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=40
    paddle_a.sety(y)
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,"s")
#paddleB
def paddle_b_up():
    y=paddle_b.ycor()
    y+=40
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=40
    paddle_b.sety(y)
wn.listen()
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,"Down")
#ball_moveme
dx=0.35
dy=0.35
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,270)
score_a=0
score_b=0
pen.write(f"player 1: {score_a} player 2: {score_b}",align="center",font=('courier',10,'normal'))

while TRUE:

    wn.update()
    ball.sety(ball.ycor()+dy)
    ball.setx(ball.xcor()+dx)
    if(ball.ycor()>290):
        dy *= -2
    if(ball.ycor()<-290):
        dy *= -2
    if(ball.xcor()>390):
        ball.goto(0,0)
        dx *= -2
        score_a+=1
        pen.clear()
        pen.write(f"player 1: {score_a} player 2: {score_b}",align="center",font=('courier',10,'normal'))
        if(score_a==5):
            pen.clear()
            pen.write("YOU LOSE PLAYER1")
            score_a=0
            score_b=0
            

    if(ball.xcor()<-390):
        ball.goto(0,0)
        dx *= -1
        score_b+=1
        pen.clear()
        pen.write(f"player 1: {score_a} player 2: {score_b}",align="center",font=('courier',10,'normal'))
        if(score_b==5):
            pen.clear()
            pen.write("YOU LOSE PLAYER2")
            score_b=0
            score_a=0
            

    if(ball.xcor()>340 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50) and ball.xcor()<350) :
        ball.setx(340)
        dx *=-1
    if(ball.xcor()<-340 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50)):
        ball.setx(-340)
        dx *=-1



    
    
    