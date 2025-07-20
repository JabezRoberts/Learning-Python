from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        # self.goto(STARTING_POSITION) replace with function we created in step 6
        self.goto_start()
    
    
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    
    def is_player_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    def goto_start(self):
        self.goto(STARTING_POSITION)