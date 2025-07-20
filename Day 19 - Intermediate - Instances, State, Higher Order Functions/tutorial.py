from turtle import Turtle, Screen

wartortle = Turtle() # Create a Turtle instance
screen = Screen() # Create a Screen object or instance

def move_forward():
    wartortle.forward(10) # Move the turtle forward by 10 units

screen.listen() # Set the screen to listen for events
# Use an event listener to connect our screen to our keyboard input

screen.onkey(key="space", fun=move_forward) # When the Space key is pressed, call move_forward. When you pass a function as an argument, you don't include the parentheses.
# Parentheses would call the function immediately, which is not what we want here. Instead, we want to pass the function itself as a reference to be called later when the event occurs.

# A Higher Order Function is a function that takes another function as an argument or returns a function as its result. In this case, `screen.onkey` is a higher order function because it takes `move_forward` as an argument.

screen.exitonclick() # Wait for a click on the screen to exit the program
# This allows us to close the turtle graphics window when we're done.