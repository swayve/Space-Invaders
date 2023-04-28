from turtle import Turtle
import random



class Shooter(Turtle):
    def __init__(self):
        super().__init__()
        self.SPEED = 20
        self.shape("circle")
        self.color("red")
        self.penup()
    
    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + self.SPEED
        self.goto(new_x, new_y)