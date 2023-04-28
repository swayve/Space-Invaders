from turtle import Screen, Turtle
from player import SpaceShooter
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(700, 700)
screen.tracer(0)


player = SpaceShooter()




screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")





game_is_on = True
while game_is_on:
    screen.update()
    player.shoot()










screen.exitonclick()