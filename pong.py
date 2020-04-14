import turtle
import random


win = turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

speed_l = 0
speed_r = 0
score_a = 0
score_b = 0
#ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball._delay(0)
#ball.speed(0)
ball.goto(0, 0)
ball.penup()
ball.dx = 1
ball.dy = 1

sum = 0

#line 
line = turtle.Turtle()
line.speed(0)
line.shape('square')
line.color('red')
line.shapesize(stretch_wid=20, stretch_len=0.1)
line.penup()
line.goto(-380, 0)
#player1
first_player = turtle.Turtle()
first_player.speed(0)
first_player.shape('square')
first_player.color('white')
first_player.shapesize(stretch_wid=7, stretch_len=1)
first_player.penup()
first_player.goto(-375, 0)


#player2
second_player = turtle.Turtle()
second_player.speed(0)
second_player.shape('square')
second_player.color('white')
second_player.shapesize(stretch_wid=7, stretch_len=1)
second_player.penup()
second_player.goto(375, 0)

#score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color('white')
score.hideturtle()
score.goto(0, 270)
score.write('Player 1: 0  Player 2: 0', align='center',font=('Arial', 16, 'bold'))



#move first player square
def first_player_up():
    y = first_player.ycor()
    y += 20
    first_player.sety(y)

def first_player_down():
    y = first_player.ycor()
    y -= 20
    first_player.sety(y) 

#move second player square
def second_player_up():
    y = second_player.ycor()
    y += 20
    second_player.sety(y)

def second_player_down():
    y = second_player.ycor()
    y -= 20
    second_player.sety(y)



win.listen()
win.onkeypress(first_player_up, 'w')
win.onkeypress(first_player_down, 's')
win.onkeypress(second_player_up, 'Up')
win.onkeypress(second_player_down, 'Down')

while True:
    win.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Top border
    if  ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    #Bottom border
    elif  ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #left border
    if ball.xcor() < -375:
        score_a += 1
        score.clear()
        score.write('Player 1: {} Player 2: {}'.format(score_a, score_b), align='center',font=('Arial', 16, 'bold'))
        ball.goto(0, 0)
        ball.dx *= -1
    #right border
    elif ball.xcor() > 375:
        score_b +=1
        score.clear()
        score.write('Player 1: {} Player 2: {}'.format(score_a, score_b), align='center',font=('Arial', 16, 'bold'))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -360 and (ball.ycor() < first_player.ycor() + 60.1 and ball.ycor() > first_player.ycor() - 60.1):
        ball.dx *= -1
        
    #collisions right
    elif ball.xcor() > 360 and (ball.ycor() < second_player.ycor() + 60.1 and ball.ycor() > second_player.ycor() - 60.1):
        ball.dx *= -1

    #collisions player1:
    if  first_player.ycor() > 227:
        first_player.sety(227)
    elif first_player.ycor() < -225:
        first_player.sety(-225)

    #collisions player2:
    if  second_player.ycor() > 227:
        second_player.sety(227)
    elif second_player.ycor() < -225:
        second_player.sety(-225)