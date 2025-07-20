from turtle import Turtle, Screen
import random

timmy = Turtle()  # Create a Turtle instance
tommy = Turtle()  # Create another Turtle instance

timmy.color = "blue" # Set the color of the first turtle to blue
tommy.color = "red" # Set the color of the second turtle to red

# State refers to the current condition or attributes of an object. Here, the state of each turtle is defined by its color.
# Each turtle has its own state, which can be modified independently. They also have their own methods to perform actions like moving forward.

is_race_on = False  # A variable to track if the race is on
# This variable acts as a state indicator
screen = Screen()  # Create a Screen object or instance
screen.setup(width=500, height=400)  # Set the size of the screen
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")  # Prompt the user to enter a color for betting

colors = ["red", "blue", "green", "yellow", "purple", "orange"]  # List of possible turtle colors
y_positions = [-100, -60, -20, 20, 60, 100]  # Y-coordinates for each turtle's starting position
all_turtles = []  # List to hold all turtle instances

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")  # Create a Turtle instance that will be shaped like a turtle

    #tell the turtles to move to the starting position
    new_turtle.penup()  # Lift the pen to avoid drawing while moving
    new_turtle.goto(x=-230, y=y_positions[i])  # Move the first turtle to the starting position
    new_turtle.color(colors[i])  # Set the color of the turtle
    all_turtles.append(new_turtle)  # Add the new turtle to the list of all turtles
    # This loop creates multiple turtles, each with a unique color and starting position.

if user_bet:
    is_race_on = True  # If the user made a bet on a turtle color, set the race to on

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False  # If any turtle crosses the finish line, end the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)  # Generate a random distance for each turtle to move
        turtle.forward(random_distance)  # Move the turtle forward by the random distance

screen.exitonclick()  # Wait for a click on the screen to exit the program