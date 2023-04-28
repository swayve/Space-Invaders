from turtle import Turtle
from player import SpaceShooter
import random



class Shooter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()


        self.all_bullets = []


    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)