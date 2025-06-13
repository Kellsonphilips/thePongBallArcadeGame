
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=600)
screen.title("The Pong Game")
screen.tracer(0)
PADDLE_CORD = [(470, 0), (-470, 0)]

scoreboard = Scoreboard()

r_paddle = Paddle(PADDLE_CORD[0])
l_paddle = Paddle(PADDLE_CORD[1])


ball = Ball()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_starts = True

while game_starts:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 270 or ball.ycor() < - 270:
        ball.bounce_vertical()

    # Detect collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 440 or ball.distance(l_paddle) < 50 and ball.xcor() < - 440:
        ball.bounce_horizontal()

    # Detect if the right paddle misses the ball
    if ball.xcor() > 480:
        scoreboard.update_l_score()
        ball.reset_and_move()

    # Detect if the left paddle misses the ball
    if ball.xcor() < -480:
        scoreboard.update_r_score()
        ball.reset_and_move()

screen.exitonclick()
