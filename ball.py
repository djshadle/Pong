from turtle import Turtle
import random
Ball_START_POS = (0, 0)
heading = random.choice([random.randrange(315, 360), random.randrange(0, 45), random.randrange(135, 225)])
# heading = random.choice([random.randrange(45, 135), random.randrange(225, 315)])

class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.speed(10)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(heading)

    def ball_move(self):
        self.forward(5)


