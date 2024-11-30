import turtle
from turtle import *
import time
from random_balls import BallManager
from shooter_turtle import ShooterTurtle
from scoreboard import Scoreboard



screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen,title('Shooter Game')
screen.listen()


shooter = ShooterTurtle()
ball_manager = BallManager()
ball_manager.hideturtle()
scoreboard = Scoreboard()
scoreboard.show_ball_missed()
scoreboard.show_ball_shot()


keys_pressed = set()

def go_left():
    shooter.left_move()

def go_right():
    shooter.right_move()

def shoot():
    shooter.shoot_pressed_bullets()

def key_press_left(key):
    keys_pressed.add(key)

def key_press_right(key):
    keys_pressed.add(key)

def key_press_shoot(key):
    keys_pressed.add(key)

def key_release_left(key):
    if key in keys_pressed:
        keys_pressed.remove(key)

def key_release_right(key):
    if key in keys_pressed:
        keys_pressed.remove(key)

def key_release_shoot(key):
    if key in keys_pressed:
        keys_pressed.remove(key)

def check_keys():
    if 'Up' in keys_pressed :
        shoot()
    if 'Left' in keys_pressed:
        go_left()
    if 'Right' in keys_pressed:
        go_right()
    turtle.ontimer(check_keys,50)

screen.onkeypress(lambda :key_press_left('Left'),'Left')
screen.onkeyrelease(lambda :key_release_left('Left'),'Left')

screen.onkeypress(lambda :key_press_right('Right'),'Right')
screen.onkeyrelease(lambda :key_release_right('Right'),'Right')

screen.onkeypress(lambda :key_press_shoot('Up'),'Up')
screen.onkeyrelease(lambda :key_release_shoot('Up'),'Up')

check_keys()

# screen.onkeypress(shooter.left_move,'Left')
# screen.onkeypress(shooter.right_move,'Right')
screen.onkey(shooter.shoot_bullets,'Up')

while True:
    time.sleep(0.1)
    screen.update()
    ball_manager.create_balls()

    for ball in ball_manager.all_balls:
        if ball.ycor() < -280 :
            ball.hideturtle()
            ball_manager.all_balls.remove(ball)
            scoreboard.change_ball_missed()
        ball.forward(5)

    for bullet in shooter.all_bullets:
        bullet.forward(50)

    for ball in ball_manager.all_balls:
        for bullet in shooter.all_bullets:
            if bullet.distance(ball)<30:
                scoreboard.change_ball_shot()
                ball.hideturtle()
                bullet.hideturtle()
                if ball in ball_manager.all_balls:
                    ball_manager.all_balls.remove(ball)
                shooter.all_bullets.remove(bullet)

    if scoreboard.ball_passed == 20 :
        scoreboard.game_over()
        break











screen.exitonclick()