from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score
import time

play_on = True
score_board = Score()
p1_up = p1_down = p2_up = p2_down = False  # Flags for paddle movement


def move_paddles():
    """Moves paddles continuously based on key press flags."""
    if p1_up:
        p1.move_up()
    if p1_down:
        p1.move_down()
    if p2_up:
        p2.move_up()
    if p2_down:
        p2.move_down()


def play_game():
    global is_on, p1, p2, p1_up, p1_down, p2_up, p2_down
    is_on = True
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('PONG')
    screen.listen()
    screen.tracer(0)

    p1 = Paddle(-1)  # Left paddle
    p2 = Paddle(1)  # Right paddle
    ball = Ball()

    # Key press event handlers
    screen.listen()
    screen.onkeypress(lambda: set_paddle_flag("p1_up", True), 'w')
    screen.onkeyrelease(lambda: set_paddle_flag("p1_up", False), 'w')
    screen.onkeypress(lambda: set_paddle_flag("p1_down", True), 's')
    screen.onkeyrelease(lambda: set_paddle_flag("p1_down", False), 's')

    screen.onkeypress(lambda: set_paddle_flag("p2_up", True), 'Up')
    screen.onkeyrelease(lambda: set_paddle_flag("p2_up", False), 'Up')
    screen.onkeypress(lambda: set_paddle_flag("p2_down", True), 'Down')
    screen.onkeyrelease(lambda: set_paddle_flag("p2_down", False), 'Down')

    while is_on:

        score_board.goto(0, 250)
        score_board.write(f" {score_board.p1}        {score_board.p2}", align='center', font=('Arial', 30, 'bold'))
        time.sleep(ball.move_speed)
        move_paddles()
        screen.update()
        ball.move_ball()

        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y()

        if ball.distance(p2) < 50 and ball.xcor() >= 270:
            distance = (ball.distance(p2) * -1) / 100
            print(distance)
            ball.bounce_x(distance)

        if ball.distance(p1) < 50 and ball.xcor() <= -270:
            distance = (ball.distance(p2)) / 100
            print(distance)
            ball.bounce_x(distance)

        if ball.xcor() <= -282:
            score_board.goto(0, 100)
            score_board.add_score('p2')
            score_board.write(arg=f" {score_board.win}", align="center", font=('Arial', 40, 'bold'))
            is_on = False
        elif ball.xcor() >= 282:
            score_board.goto(0, 100)
            score_board.add_score('p1')
            score_board.write(arg=f" {score_board.win}", align="center", font=('Arial', 40, 'bold'))
            is_on = False



        if not is_on:
            restart = screen.textinput('restart', "Restart")
            if restart == 'r':
                screen.clearscreen()
                is_on = True
                play_game()

    screen.exitonclick()




def set_paddle_flag(paddle, state):
    """Sets paddle movement flags for continuous movement."""
    global p1_up, p1_down, p2_up, p2_down
    if paddle == "p1_up":
        p1_up = state
    elif paddle == "p1_down":
        p1_down = state
    elif paddle == "p2_up":
        p2_up = state
    elif paddle == "p2_down":
        p2_down = state


play_game()
