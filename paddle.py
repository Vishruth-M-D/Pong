from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("Light Yellow")
        self.penup()
        self.goto(position)

    def down(self):
        newy = self.ycor() - 10
        self.goto(self.xcor(), newy)

    def up(self):
        newy = self.ycor() + 10
        self.goto(self.xcor(), newy)
