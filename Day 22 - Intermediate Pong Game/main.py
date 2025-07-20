from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong The Arcade Game")
screen.tracer(0) # removes the animation of the turtle starting at the center then moving back. But because of this function we need to manually update and refresh the 
# screen everytime or the turtle/paddle will not show. use the while loop with game_is_on variable then screen.update() while game-is_on to update screen manually everytime
from scoreboard import Scoreboard
    
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down") # Remember not to use the parenthesis when using a function as a parameter

screen.onkey(l_paddle.move_up, "w") # Move the left paddle up and down. The previous are for the right paddle
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # Let the loop pause between iterations so the ball doesn't just run off screen. Reduce this on each bounce to speed up the ball
    screen.update()
    ball.move()
    
    # Detect bounce when ball hits the top or bottom of the screen left or right of the screen
    if ball.ycor() > 280 or ball.ycor() < -280: # Screen height is 600px
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    
    # Detect if ball goes out of bounds at the edge of the screen. If yes, reset the ball's position to the center of the screen. The ball should then start moving
    # towards the other player
    
    # Detect when right paddle misses - The screen is 800px and the paddle is 350px so if the paddle goes beyond 380 then it's definitely missed the ball.
    # The paddle goes from 340 to 360
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect when the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()