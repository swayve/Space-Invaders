from turtle import Turtle
import random


class SpaceShooter(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(0, -320)
        self.shapesize(2, 6)

    def left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, -320)
    
    def right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, -320)
    

    def shoot(self):
        MOVE = 10
        bullet = Turtle(shape="circle")
        bullet.color("red")
        bullet.penup()
        bullet.setpos(0, 0)
        shot = random.randint(1, 4)
        if shot == 1:
            bullet.forward(MOVE)