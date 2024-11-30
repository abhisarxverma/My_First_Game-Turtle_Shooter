import turtle
import random

class ShooterTurtle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.all_bullets = []
        self.shape('turtle')
        self.color('black')
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.setheading(90)
        self.penup()
        self.x_axis = 0
        self.y_axis = -250
        self.goto(self.x_axis, self.y_axis)

    def left_move(self):
        if self.heading() < 150.0:
            self.setheading(self.heading()+5)

    def right_move(self):
        if self.heading() > 30.0:
            self.setheading(self.heading() - 5)

    def shoot_bullets(self):
        new_bullet = turtle.Turtle(shape='circle')
        new_bullet.shapesize(stretch_len=2,stretch_wid=0.2)
        new_bullet.penup()
        new_bullet.color('black')
        new_bullet.setheading(self.heading()+10)
        new_bullet.goto(0,-210)
        self.all_bullets.append(new_bullet)

    def shoot_pressed_bullets(self):
        no = random.randint(1, 6)
        if no == 1:
            new_bullet = turtle.Turtle(shape='circle')
            new_bullet.shapesize(stretch_len=2,stretch_wid=0.2)
            new_bullet.penup()
            new_bullet.color('black')
            new_bullet.setheading(self.heading()+10)
            new_bullet.goto(0,-210)
            self.all_bullets.append(new_bullet)