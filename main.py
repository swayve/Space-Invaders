from turtle import Screen, Turtle
from player import SpaceShooter
from bullet import Shooter
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(700, 700)
screen.tracer(0)


player = SpaceShooter()
shooter = Shooter()



screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    shooter.move()










screen.exitonclick()