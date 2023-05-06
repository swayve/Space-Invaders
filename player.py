from turtle import Turtle
import time
import random


STARTING_POS = (0, -320)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(2, 6)
        self.color("green")
        self.penup()
        self.goto(STARTING_POS)

    
    def left_m(self):
        new_x = self.xcor() - 20
        self.goto(new_x, -320)
    
    def right_m(self):
        new_x = self.xcor() + 20
        self.goto(new_x, -320)


player = Player()

class Bullet(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.color("red")
            self.goto(player.xcor(), player.ycor())

        def shoot(self):
            self.bullet_speed = 15
            self.forward(self.bullet_speed)

            




