from turtle import Turtle

score = 0
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            content = data.read()
            if content:
                self.high_score = int(content)
            else:
                self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()
        # self.clear()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    # Rewrite the game over method to instead of stopping the game and writing game over we reset the scoreboard
    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write(f"GAME OVER: {self.score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
    # Open data.txt

    