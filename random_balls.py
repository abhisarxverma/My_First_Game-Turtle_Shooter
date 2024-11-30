import turtle
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "lime", "cyan", "deepskyblue",
    "magenta", "pink", "hotpink", "gold"]


class BallManager(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.all_balls = []

    def create_balls(self):
        no = random.randint(1,6)
        if no == 1:
            new_ball = Turtle(shape='circle')
            new_ball.color(random.choice(COLORS))
            new_ball.penup()
            new_ball.shapesize(stretch_len=2,stretch_wid=2)
            new_ball.setheading(270)
            x_axis = random.randint(-290,290)
            y_axis = random.randint(200,280)
            new_ball.goto(x_axis,y_axis)
            self.all_balls.append(new_ball)
