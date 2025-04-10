from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.shapesize(0.5)
        self.angle = 80
        self.x_move = 7
        self.y_move = 15
        self.move_speed = 0.05

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self, distance):
        self.x_move *= -1
        self.x_move += distance/360
        self.move_speed *= 0.8
