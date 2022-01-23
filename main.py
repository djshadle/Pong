from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

L_POS = (-350, 0)
R_POS = (350, 0)

screen = Screen()
ball = Ball()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle(L_POS)
r_paddle = Paddle(R_POS)

screen.listen()
screen.onkeypress(r_paddle.r_up, "Up")
screen.onkeypress(r_paddle.r_down, "Down")
screen.onkeypress(l_paddle.l_up_press, "w")
screen.onkeypress(l_paddle.l_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
