from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super(Paddle, self).__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.speed(0)
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setpos(position)

    def l_up_press(self):
        if self.ycor() <= 240:
            self.forward(20)

    def l_down(self):
        if self.ycor() >= -240:
            self.backward(20)

    def r_up(self):
        if self.ycor() <= 240:
            self.forward(20)

    def r_down(self):
        if self.ycor() >= -240:
            self.backward(20)
