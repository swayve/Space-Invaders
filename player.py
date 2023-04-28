from turtle import Turtle



class SpaceShooter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(2, 4)
