from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        
        
        self.shape("square") #make the turtle the shape of a paddle
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # Each turtle is 20 X 20 so stretch the length by 0 and the width by 5 to get it to be 100 X 20
        self.penup()
        self.goto(position)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

