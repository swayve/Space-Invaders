from turtle import Screen, Turtle
from player import Player, Bullet
from bullet import *
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(700, 700)
screen.tracer(0)

player = Player()
bullet = Bullet()


screen.listen()
screen.onkey(player.left_m, "Left")
screen.onkey(player.right_m, "Right")
screen.onkey(bullet.shoot, "space")


while True:
     time.sleep(0.1)
     screen.update()
     








screen.exitonclick()