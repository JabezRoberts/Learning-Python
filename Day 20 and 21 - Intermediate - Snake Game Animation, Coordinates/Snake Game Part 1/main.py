from turtle import Screen
from mysnake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up") # tie buttons to these functions we create
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Create a snake body ==> 3 squares (turtles) all ligned up behind each other. Each square is 20x20 pixels.
# The first square is at (0, 0), the second at (-20, 0), and the third at (-40, 0). 

# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)
# Written in a more efficient way using a loop


# for position in starting_positions:
#     segment = Turtle("square")
#     segment.color("white")
#     # segment.penup()  # Prevents the turtle from drawing lines
#     segment.goto(position)

# Now to move the snake, we can create a function that moves each segment forward by 20 pixels.
#Create and organize the snake segments into a list for easy management.

snake_segments = []
segments = []


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # Adds a 1 second sleep/pause/delay after all segments have movement
    
    snake.move()
    
    # detect collision with food using distance method from Turtle class
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    
    # Detect collision with tail
    # if head collides with any segment in tail trigger game over sequence
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    # rewrite the above in fewer lines
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
# How to control the snake using the direction keys


screen.exitonclick()# Uncomment the following lines to run the snake game with the initial setup.



# from turtle import Screen
# from snake import Snake
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()


# screen.exitonclick()