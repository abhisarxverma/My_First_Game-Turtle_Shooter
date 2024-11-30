import turtle
from turtle import Turtle

from click import clear


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.s = Turtle()
        self.s.penup()
        self.s.hideturtle()
        self.ball_passed = 0
        self.ball_shot = 0
        self.hideturtle()

    def show_ball_missed(self):
        self.penup()
        self.goto(-150,265)
        self.pencolor('black')
        self.pendown()
        self.write(f'Balls passed : {self.ball_passed}',align='center',font = ('Courier',20,'normal'))
        self.penup()

    def show_ball_shot(self):
        self.s.goto(150, 265)
        self.s.pencolor('black')
        self.s.pendown()
        self.s.write(f'Balls shot : {self.ball_shot}', align='center', font=('Courier', 20, 'normal'))
        self.s.penup()

    def change_ball_shot(self):
        self.ball_shot += 1
        self.s.clear()
        self.show_ball_shot()

    def change_ball_missed(self):
        self.ball_passed += 1
        self.clear()
        self.show_ball_missed()

    def game_over(self):
        self.penup()
        self.goto(-10, 0)
        self.pencolor('black')
        self.pendown()
        self.write(f'Game Over.', align='center', font=('Courier', 25, 'normal'))
        self.penup()
