from turtle import Turtle, Screen
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('PONG')
# screen.listen()

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        # pos will take values '1' (for right paddle) and '-1' (for left paddle)
        self.paddle_len = 15
        self.x_cor = 280 * pos
        self.y_cor = 0
        self.direction = 90
        self.count = 0
        self.penup()
        self.setheading(90)
        self.setx(self.x_cor)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=2, stretch_wid=0.4)
        self.speed('fast')

    def move_up(self):
        self.count = 0
        if not self.ycor() >= 250 and self.count == 0:
            self.setheading(90)
            self.forward(20)
        self.count += 1

    def move_down(self):
        self.count = 0
        if not self.ycor() <= -250 and self.count == 0:
            self.setheading(270)
            self.forward(20)
        self.count += 1

# screen.tracer(0)
# p1 = Paddle(1)
# p2 = Paddle(-1)
#
# screen.onkey(p2.move_up, 'Up')
# screen.onkey(p2.move_down, 'Down')
# screen.onkey(p1.move_up, 'w')
# screen.onkey(p1.move_down, 's')
# screen.update()
# screen.exitonclick()