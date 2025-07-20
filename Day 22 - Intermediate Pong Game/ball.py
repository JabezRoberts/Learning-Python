from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("green")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self): # The easiest for it to bounce is to have it go in the opposite direction of where it came
        self.y_move *= -1
        self.move_speed *= 0.9
        
    def bounce_x(self): # The easiest for it to bounce is to have it go in the opposite direction of where it came
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        # now the ball should go in the opposite direction
        self.move_speed = 0.1
        self.bounce_x()