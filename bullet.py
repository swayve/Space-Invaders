from turtle import Turtle
import random

SPEED = 10

class Shooter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.forward(SPEED)
