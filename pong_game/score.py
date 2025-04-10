from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.win = ''
        self.color('white')
        self.penup()
        self.hideturtle()
        self.p1 = 0
        self.p2 = 0

    def add_score(self, winner):
        if winner == 'p1':
            self.p1 += 1
            self.win = f"Player 1 wins !!!"
        elif winner == 'p2':
            self.p2 += 1
            self.win = f"Player 2 wins !!!"